# wikipedia_song_search_module.py

"""
Wikipedia Song Search Module

Efficient, rate-compliant Wikipedia API client for searching song information.
Uses generator-based queries to minimise API calls, disambiguation detection,
relevance scoring, connection pooling, and automatic retries.

Typical API cost: 1 call per song (generator=search + prop=extracts combined),
with automatic fallback for edge cases where extracts are missing.

----------------------------

Vibe-coded with Z AI GLM 5 Turbo LLM
https://chat.z.ai/

License: Apache 2.0

Project Los Angeles
Tegridy Code 2026
"""

import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Callable, Dict, List, Optional, Tuple

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)

WIKI_API = "https://en.wikipedia.org/w/api.php"
USER_AGENT = "ProjectLosangeles/1.0 (alex@tegridycode.com)"

# ── Tunables ──────────────────────────────────────────────────────────────────
MAX_RETRIES          = 3
RETRY_BACKOFF_FACTOR = 0.5        # seconds → 0.5 s, 1 s, 2 s
REQUEST_TIMEOUT      = 15         # seconds
DEFAULT_RATE_LIMIT   = 10.0       # req/s  (≈ 600/min, well within Wikipedia's
                                   #         200 req/min guideline for unregistered
                                   #         bots, with headroom for burst)
MAXLAG              = 5           # seconds – helps the API shed load gracefully
BATCH_MAX_WORKERS   = 4           # concurrent threads (4–8 is polite)
WIKI_EXLIMIT        = 20          # max extracts per non-bot query


# ──────────────────────────────────── Rate Limiter ────────────────────────────

class RateLimiter:
    """Thread-safe sliding-window rate limiter."""

    __slots__ = ("_min_interval", "_lock", "_last")

    def __init__(self, rate: float = DEFAULT_RATE_LIMIT) -> None:
        self._min_interval = 1.0 / rate
        self._lock = threading.Lock()
        self._last = 0.0

    def wait(self) -> None:
        with self._lock:
            now = time.monotonic()
            delta = self._min_interval - (now - self._last)
            if delta > 0:
                time.sleep(delta)
            self._last = time.monotonic()


# ──────────────────────────────────── Session Factory ─────────────────────────

def _create_session(
    rate: float = DEFAULT_RATE_LIMIT,
) -> Tuple[requests.Session, RateLimiter]:
    """Return a pooled, retry-enabled *Session* plus a *RateLimiter*."""
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    retry = Retry(
        total=MAX_RETRIES,
        backoff_factor=RETRY_BACKOFF_FACTOR,
        status_forcelist=[429, 500, 502, 503, 504],
        respect_retry_after_header=True,
        allowed_methods=["GET"],
    )
    adapter = HTTPAdapter(max_retries=retry, pool_connections=10, pool_maxsize=10)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    return session, RateLimiter(rate=rate)


# ──────────────────────────────────── Low-level GET ───────────────────────────

def _wiki_get(
    session: requests.Session,
    limiter: RateLimiter,
    params: Dict[str, Any],
) -> Dict[str, Any]:
    """Rate-limited GET → parsed JSON.  Raises on HTTP / API-level errors."""
    limiter.wait()
    r = session.get(WIKI_API, params=params, timeout=REQUEST_TIMEOUT)
    r.raise_for_status()
    data: Dict[str, Any] = r.json()
    if "error" in data:
        raise ValueError(f"Wikipedia API error: {data['error'].get('info', data['error'])}")
    return data


# ──────────────────────────────────── Core API Helpers ────────────────────────

def _search_with_extracts(
    session: requests.Session,
    limiter: RateLimiter,
    query: str,
    limit: int = 5,
    exintro: bool = False,
    exchars: Optional[int] = None,
) -> List[Dict[str, Any]]:
    """
    Search Wikipedia **and** fetch extracts in **one** API call.

    Uses ``generator=search`` so search results and their full extracts
    (plus categories / page-props for disambiguation detection) come back
    together.  Pages are sorted by search rank via the ``index`` field.
    """
    params: Dict[str, Any] = {
        "action":     "query",
        "generator":  "search",
        "gsrsearch":  query,
        "gsrlimit":   limit,
        "prop":       "extracts|pageprops|categories|info",
        "inprop":     "url",
        "exlimit":    WIKI_EXLIMIT,
        "explaintext": 1,
        "format":     "json",
        "utf8":       1,
        "maxlag":     MAXLAG,
        "cllimit":    10,         # enough to detect disambig categories
    }
    if exintro:
        params["exintro"] = 1
    if exchars:
        params["exchars"] = max(exchars, 1)

    data = _wiki_get(session, limiter, params)
    pages = data.get("query", {}).get("pages", {})
    return sorted(pages.values(), key=lambda p: p.get("index", 999))


def _fetch_extract_fallback(
    session: requests.Session,
    limiter: RateLimiter,
    pageid: int,
    exintro: bool = False,
    exchars: Optional[int] = None,
) -> str:
    """
    Fallback to fetch extract for a single page when generator-based
    query returns empty extract. This handles edge cases where the API
    doesn't return extracts with generator=search (e.g., pages with
    parentheses in titles, complex templates, etc.).
    """
    params: Dict[str, Any] = {
        "action":      "query",
        "pageids":     str(pageid),
        "prop":        "extracts",
        "explaintext": 1,
        "format":      "json",
        "utf8":        1,
        "maxlag":      MAXLAG,
    }
    if exintro:
        params["exintro"] = 1
    if exchars:
        params["exchars"] = max(exchars, 1)

    try:
        data = _wiki_get(session, limiter, params)
        pages = data.get("query", {}).get("pages", {})
        for page in pages.values():
            extract = page.get("extract", "")
            if extract:
                return extract
    except Exception as exc:
        logger.warning("Fallback extract fetch failed for pageid %d: %s", pageid, exc)
    return ""


def _fetch_extracts_batch(
    session: requests.Session,
    limiter: RateLimiter,
    pageids: List[int],
    exintro: bool = False,
    exchars: Optional[int] = None,
) -> Dict[int, Dict[str, Any]]:
    """
    Fetch extracts for up to *WIKI_EXLIMIT* page IDs in one request.

    Useful when you already know the page IDs and want to avoid
    redundant search calls (e.g. second-pass disambiguation resolution).
    """
    batch = pageids[:WIKI_EXLIMIT]
    params: Dict[str, Any] = {
        "action":      "query",
        "pageids":     "|".join(str(pid) for pid in batch),
        "prop":        "extracts|pageprops|categories|info",
        "inprop":      "url",
        "exlimit":     WIKI_EXLIMIT,
        "explaintext": 1,
        "format":      "json",
        "utf8":        1,
        "maxlag":      MAXLAG,
        "cllimit":     10,
    }
    if exintro:
        params["exintro"] = 1
    if exchars:
        params["exchars"] = max(exchars, 1)

    data = _wiki_get(session, limiter, params)
    raw = data.get("query", {}).get("pages", {})
    return {int(k): v for k, v in raw.items()}


# ──────────────────────────────────── Disambiguation ──────────────────────────

_DISAMBIG_PHRASES = ("may refer to:", "could refer to:", "this is a disambiguation")


def _is_disambiguation(page: Dict[str, Any]) -> bool:
    """Heuristic disambiguation-page detection."""
    if "disambiguation" in page.get("pageprops", {}):
        return True

    for cat in page.get("categories", []):
        if "disambiguation" in cat.get("title", "").lower():
            return True

    title = page.get("title", "").lower()
    if "(disambiguation)" in title:
        return True

    head = page.get("extract", "")[:300].lower()
    if any(p in head for p in _DISAMBIG_PHRASES):
        return True

    return False


# ──────────────────────────────────── Relevance Scoring ───────────────────────

_SONG_KEYWORDS = ("song", "single", "track", "ballad", "duet", "cover")


def _score_page(page: Dict[str, Any], artist: str, title: str) -> float:
    """Score how relevant a page is to a *song* query (higher = better)."""
    score  = 0.0
    pt     = page.get("title", "").lower()
    tl     = title.lower()
    al     = artist.lower()

    # Strong signals in the title
    if "(song)"    in pt: score += 10.0
    if "(single)"  in pt: score +=  8.0
    if "(track)"   in pt: score +=  7.0

    # Title / artist match
    if tl in pt:   score += 5.0
    if al in pt:   score += 3.0

    # Non-disambiguation bonus
    if not _is_disambiguation(page):
        score += 2.0

    # Song-related keywords in the lead
    snippet = page.get("extract", "")[:500].lower()
    if any(kw in snippet[:200] for kw in _SONG_KEYWORDS):
        score += 1.5

    return score


# ──────────────────────────────────── Query Building ──────────────────────────

def _build_search_queries(artist: str, title: str) -> List[str]:
    """Query variants from most specific → most general (enables early exit)."""
    a, t = artist.strip(), title.strip()
    if not a and not t:
        return []
    if not a:
        return [
            f'"{t}" (song)',
            f"{t} song",
            f"{t}",
        ]
    if not t:
        return [
            f'"{a}" song',
            f"{a}",
        ]
    return [
        f'"{t}" "{a}" song',       # exact title + artist + song
        f"{t} {a} song",            # loose
        f'"{t}" (song)',            # exact title, song disambiguator
        f"{t} {a}",                 # no "song" keyword
        f"{t} song",                # title only
    ]


# ──────────────────────────────────── Best-Page Selection ─────────────────────

def _format_result(page: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "title":   page.get("title"),
        "pageid":  page["pageid"],
        "url":     page.get("fullurl") or page.get("canonicalurl"),
        "extract": page.get("extract", ""),
    }


def _pick_best_page(
    pages:  List[Dict[str, Any]],
    artist: str = "",
    title:  str = "",
) -> Optional[Dict[str, Any]]:
    """Pick the most relevant, non-disambiguation page from *pages*."""
    valid = [p for p in pages if p.get("pageid", 0) > 0]
    if not valid:
        return None

    scored = sorted(
        ((p, _score_page(p, artist, title)) for p in valid),
        key=lambda x: x[1],
        reverse=True,
    )

    # Prefer non-disambiguation
    for page, _ in scored:
        if not _is_disambiguation(page):
            return _format_result(page)

    # Fallback: highest-scored page even if disambiguation
    return _format_result(scored[0][0])


def _ensure_extract(
    result: Optional[Dict[str, Any]],
    session: requests.Session,
    limiter: RateLimiter,
    exintro: bool = False,
    exchars: Optional[int] = None,
) -> Optional[Dict[str, Any]]:
    """
    Ensure the result has a non-empty extract. If the extract is empty
    (which can happen with generator=search for certain pages), fetch
    it with a dedicated API call.
    """
    if result is None:
        return None
    
    if not result.get("extract") and result.get("pageid"):
        logger.debug(
            "Empty extract for pageid %d ('%s'), fetching fallback",
            result["pageid"],
            result.get("title", ""),
        )
        result["extract"] = _fetch_extract_fallback(
            session, limiter, result["pageid"],
            exintro=exintro, exchars=exchars,
        )
    
    return result


# ──────────────────────────────────── Single-Song API ─────────────────────────

def wikipedia_search_song(
    artist: str,
    title: str,
    session: Optional[requests.Session] = None,
    limiter: Optional[RateLimiter] = None,
    exintro: bool = False,
    exchars: Optional[int] = None,
) -> Optional[Dict[str, Any]]:
    """
    Search Wikipedia for a song by *artist* + *title*.

    Uses ``generator=search`` to fetch results **and** extracts in a single
    API call per query variant.  Tries multiple query strategies with early
    exit, so most songs resolve in exactly **1 API call**.

    If the extract comes back empty (known edge case with certain pages),
    a fallback fetch is performed automatically.

    Args:
        artist:  Artist name.
        title:   Song title.
        session: Optional pre-built ``requests.Session``.
        limiter: Optional ``RateLimiter`` (created automatically if *session*
                 is ``None``).
        exintro: If ``True``, return only the lead section.
        exchars: Cap extract to *N* characters.

    Returns:
        ``{'title', 'pageid', 'url', 'extract'}`` or ``None``.
    """
    own = session is None
    if own:
        session, limiter = _create_session()

    assert limiter is not None  # for type-checker

    try:
        seen: set = set()
        for query in _build_search_queries(artist, title):
            pages = _search_with_extracts(
                session, limiter, query,
                limit=5, exintro=exintro, exchars=exchars,
            )
            new = [p for p in pages if p.get("pageid") not in seen]
            seen.update(p.get("pageid") for p in pages if p.get("pageid", 0) > 0)
            if not new:
                continue
            result = _pick_best_page(new, artist, title)
            if result:
                return _ensure_extract(result, session, limiter, exintro, exchars)
        return None

    except requests.RequestException as exc:
        logger.warning("Request error for '%s' by '%s': %s", title, artist, exc)
        return None
    except (KeyError, ValueError, TypeError) as exc:
        logger.warning("Parse error for '%s' by '%s': %s", title, artist, exc)
        return None
    finally:
        if own:
            session.close()


# ──────────────────────────────────── Batched API ─────────────────────────────

def wikipedia_search_songs_batched(
    queries: List[Tuple[str, str]],
    max_workers: int = BATCH_MAX_WORKERS,
    rate_limit: float = DEFAULT_RATE_LIMIT,
    exintro: bool = False,
    exchars: Optional[int] = None,
    on_progress: Optional[Callable[[int, int], None]] = None,
) -> List[Optional[Dict[str, Any]]]:
    """
    Search Wikipedia for many songs in parallel.

    * Shares one connection-pooled session and one **global** rate limiter
      so the aggregate request rate never exceeds *rate_limit* regardless
      of thread count.
    * Each song uses the single-call ``generator=search`` approach
      (typically **1 API hit** per song).
    * If extracts come back empty, a fallback fetch is performed automatically.
    * Results are returned in the same order as *queries*.

    Args:
        queries:     List of ``(artist, title)`` tuples.
        max_workers: Thread count (4–8 recommended for polite access).
        rate_limit:  Global requests/sec cap across all threads.
        exintro:     Return only the lead section.
        exchars:     Cap extract length.
        on_progress: ``callback(completed, total)`` after each song finishes.

    Returns:
        List of result dicts (or ``None``) matching input order.
    """
    if not queries:
        return []

    session, limiter = _create_session(rate=rate_limit)
    results: List[Optional[Dict[str, Any]]] = [None] * len(queries)
    _completed = [0]
    _lock = threading.Lock()

    def _process(idx: int, artist: str, title: str) -> None:
        try:
            seen: set = set()
            for query in _build_search_queries(artist, title):
                pages = _search_with_extracts(
                    session, limiter, query,
                    limit=5, exintro=exintro, exchars=exchars,
                )
                new = [p for p in pages if p.get("pageid") not in seen]
                seen.update(p.get("pageid") for p in pages if p.get("pageid", 0) > 0)
                if not new:
                    continue
                result = _pick_best_page(new, artist, title)
                if result:
                    results[idx] = _ensure_extract(
                        result, session, limiter, exintro, exchars
                    )
                    break
        except Exception as exc:
            logger.warning("Batch item %d ('%s' by '%s'): %s", idx, title, artist, exc)
        finally:
            with _lock:
                _completed[0] += 1
            if on_progress:
                on_progress(_completed[0], len(queries))

    try:
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            futures = [
                pool.submit(_process, idx, artist, title)
                for idx, (artist, title) in enumerate(queries)
            ]
            for f in as_completed(futures):
                f.result()  # surface any uncaught exceptions
    finally:
        session.close()

    return results


# ──────────────────────────────────── Quick Demo ──────────────────────────────

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # --- Single search ---
    result = wikipedia_search_song("Radiohead", "Creep")
    print("Single result:", result and result["title"], "|", (result["extract"] or "")[:120], "...")

    # --- Batched search ---
    songs = [
        ("Radiohead",   "Creep"),
        ("Nirvana",     "Smells Like Teen Spirit"),
        ("The Beatles", "Yesterday"),
        ("Queen",       "Bohemian Rhapsody"),
        ("Adele",       "Hello"),
    ]

    def progress(done: int, total: int) -> None:
        print(f"  [{done}/{total}]", end="\r")

    batch = wikipedia_search_songs_batched(songs, on_progress=progress)
    print()
    for (artist, title), r in zip(songs, batch):
        label = r["title"] if r else "NOT FOUND"
        extract_preview = (r["extract"] or "")[:80] + "..." if r and r.get("extract") else "[NO EXTRACT]"
        print(f"  {artist} – {title:30s} → {label}")
        print(f"      {extract_preview}")