import re
import unicodedata
from difflib import SequenceMatcher

class MIDIMusicSanitizer:
    # Pre-compile all regexes at class level for O(1) lookup speed
    _MIDI_EXT = re.compile(r'\.(mid|midi|kar|rmi|mp3|wav|flac)$', re.IGNORECASE)
    _TRACK_NUM = re.compile(r'^\d{1,3}[\s\.\-_]*[-\s]?')
    _URL_GARBAGE = re.compile(r'[\[\{\<\("](?:www\.|http|\.com|\.net|midi|download)[^)\]\}\>"\)]*[\]\}\>\)"\)]?', re.IGNORECASE)
    
    # FIXED: Added `_` to both opening and closing boundary brackets!
    _TITLE_MODIFIERS = re.compile(
        r'[\(\[\{~\*_-]?\s*(?:remix|remastered|remaster|radio\s*edit|album\s*version|single\s*version|'
        r'explicit|clean|dirty|acoustic|live|instrumental|cover|karaoke|backing\s*track|demo|'
        r'extended|short\s*edit|mix|original|version|final|v\d+|rev\d+|edit|lyrics|video|audio|'
        r'official|performance|reprise|interlude|outro|intro|skit)\s*[\)\]\}~\*_-]?',
        re.IGNORECASE
    )
    
    # FIXED: Made `(?:[vV]\d+|\d+)` optional with `?` to clean up orphaned trailing separators like ` _`
    _TRAILING_SEQ = re.compile(r'[\s\.\-_]+(?:[vV]\d+|\d+)?$')
    
    # "Axe" approach for Titles. Splits on "feat" and takes ONLY the left side.
    _TITLE_FEAT_SPLIT = re.compile(r'\s*[\(\[\{\-]?\s*(?:feat\.?|featuring|ft\.?)\s*', re.IGNORECASE)
    
    # "Axe" approach for Artists. Completely destroys everything after "feat".
    _ARTIST_FEAT_SPLIT = re.compile(r'\s+(?:feat\.?|featuring|ft\.?|pres\.?|presentation)\s*', re.IGNORECASE)
    
    # SPLIT (do not strip) primary collaboration delimiters like &, x, vs, and
    _ARTIST_SPLIT = re.compile(r'\s*(?:x|vs\.?|&|,|\band\b)\s*', re.IGNORECASE)
    
    # Strip prefixes, but PROTECT names like "The The" using negative lookahead
    _ARTIST_PREFIXES = re.compile(r'^(?:the|a|an)\s+(?!the\b)', re.IGNORECASE)
    
    # Universal punctuation (keep spaces, remove everything else)
    _PUNCTUATION = re.compile(r'[^\w\s]')
    # CamelCase splitter (e.g., "JohnLennon" -> "John Lennon")
    _CAMEL_SPLIT = re.compile(r'(?<=[a-z])(?=[A-Z])')

    @classmethod
    def _normalize_unicode(cls, text: str) -> str:
        """NFKD decomposes characters like é -> e, then drops the accent."""
        return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')

    @classmethod
    def _base_clean(cls, text: str) -> str:
        """Strips MIDI file system artifacts and normalizes encoding."""
        text = cls._normalize_unicode(text)
        text = cls._MIDI_EXT.sub('', text)
        text = cls._TRACK_NUM.sub('', text)
        text = cls._URL_GARBAGE.sub('', text)
        return text.strip()

    @classmethod
    def sanitize_title(cls, raw_title: str) -> str:
        """Reduces a title to its canonical core fingerprint."""
        text = cls._base_clean(raw_title)
        # Chop off anything after "feat."
        text = cls._TITLE_FEAT_SPLIT.split(text, maxsplit=1)[0]
        text = cls._TITLE_MODIFIERS.sub('', text) 
        text = cls._TRAILING_SEQ.sub('', text)    
        text = re.sub(r'\s+', ' ', text).strip()
        return cls._PUNCTUATION.sub('', text).lower()

    @classmethod
    def _sanitize_single_artist(cls, artist_str: str) -> str:
        """Processes a single artist entity (sorts words alphabetically)."""
        text = cls._ARTIST_PREFIXES.sub('', artist_str)
        text = cls._PUNCTUATION.sub('', text)
        text = cls._CAMEL_SPLIT.sub(' ', text)
        text = text.lower().strip()
        
        words = text.split()
        words.sort()
        return " ".join(words)

    @classmethod
    def sanitize_artist(cls, raw_artist: str) -> str:
        """Reduces an artist string to a permutation-proof, multi-artist fingerprint."""
        text = cls._base_clean(raw_artist)
        
        # Step 1: Chop off everything after "feat." (takes only index 0)
        text = cls._ARTIST_FEAT_SPLIT.split(text, maxsplit=1)[0].strip()
        
        # Step 2: Split by primary collaboration delimiters ("&", ",", "x")
        artist_chunks = cls._ARTIST_SPLIT.split(text)
        
        # Step 3: Sanitize each chunk individually
        sanitized_chunks = [cls._sanitize_single_artist(chunk) for chunk in artist_chunks if chunk]
        
        # Step 4: Sort the array of artists!
        sanitized_chunks.sort()
        
        return " ".join(sanitized_chunks)

    @classmethod
    def _fast_fuzzy_match(cls, s1: str, s2: str, threshold: float) -> bool:
        """Optimized fuzzy matcher."""
        if not s1 or not s2:
            return False
        len1, len2 = len(s1), len(s2)
        max_len = max(len1, len2)
        
        if (max_len - min(len1, len2)) / max_len > (1.0 - threshold):
            return False
            
        return SequenceMatcher(None, s1, s2).ratio() >= threshold

    @classmethod
    def is_same_title(cls, title1: str, title2: str, fuzzy_threshold: float = 0.85) -> bool:
        fp1, fp2 = cls.sanitize_title(title1), cls.sanitize_title(title2)
        if fp1 == fp2:
            return True
        return cls._fast_fuzzy_match(fp1, fp2, fuzzy_threshold)

    @classmethod
    def is_same_artist(cls, artist1: str, artist2: str, fuzzy_threshold: float = 0.88) -> bool:
        fp1, fp2 = cls.sanitize_artist(artist1), cls.sanitize_artist(artist2)
        if fp1 == fp2:
            return True
        return cls._fast_fuzzy_match(fp1, fp2, fuzzy_threshold)

    @classmethod
    def split_filename(cls, filename: str, sep: str = '') -> tuple[str, str]:
        """Attempts to split 'Artist - Title' formats."""
        text = cls._base_clean(filename)
        if sep:
            parts = text.split(sep)
        else:    
            parts = re.split(r'\s*[-_]\s*', text, maxsplit=1)
        if len(parts) == 2:
            return parts[0].strip(), parts[1].strip()
        return "", text.strip()


# === DEBUG PROOF ===
if __name__ == "__main__":
    print(MIDIMusicSanitizer.is_same_title("Summer", "[www.midi.com] Summer (Radio Edit) _v2.mid")) # Now safely returns True
    
    a1 = "Taylor Swift"
    a2 = "Swift Taylor feat. Ed Sheeran"
    
    print(f"\nFingerprint 1: '{MIDIMusicSanitizer.sanitize_artist(a1)}'")
    print(f"Fingerprint 2: '{MIDIMusicSanitizer.sanitize_artist(a2)}'")
    print(f"Exact Match: {MIDIMusicSanitizer.sanitize_artist(a1) == MIDIMusicSanitizer.sanitize_artist(a2)}")
    print(f"Result: {MIDIMusicSanitizer.is_same_artist(a1, a2)}")