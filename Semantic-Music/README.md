# [Experimental] [WIP] Semantic Music
## Semantic music datasets, supplemental data and code

***

## Notes:

*
*
*

***

## Easily decode to MIDI with TMIDIX Python module from tegridy-tools

```
!git clone --depth 1 https://github.com/asigalov61/tegridy-tools
```

```
import TMIDIX
import random
import tqdm

semantic_scores, scores_dict, words_dict = TMIDIX.Tegridy_Any_Pickle_File_Reader('Semantic_Music_TP_TPV_Chords_No_Velocity')
```

```
#===============================================================================
print('=' * 70)

semantic_score = random.choice(semantic_scores)
chords_dict = [s[1] for s in scores_dict]

delta_chords_score = []

for s in tqdm.tqdm(semantic_score):
  for ss in s:

    idx = chords_dict.index(ss)
    chord = scores_dict[idx][0]

    delta_chords_score.append(chord)

print('=' * 70)
#===============================================================================

song_f = []

time = 0
dur = 1
vel = 90
pitch = 60
channel = 0

for s in delta_chords_score:

  time += s[0] * 32

  for i in range(1, len(s), 2):
    
    dur = s[i] * 32
    ptc = s[i+1]

    vel = max(40, ptc)

    song_f.append(['note', time, dur, channel, ptc, vel, 0])

data = TMIDIX.Tegridy_ms_SONG_to_MIDI_Converter(song_f,
                                                output_signature = 'Semantic Music',
                                                output_file_name = '/content/Semantic-Music-Composition',
                                                track_name='Project Los Angeles',
                                                )
print('=' * 70)
```

***

### Project Los Angeles
### Tegridy Code 2024
