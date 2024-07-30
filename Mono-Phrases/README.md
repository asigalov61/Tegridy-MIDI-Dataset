# Mono Phrases
## 35474 multi-instrumental music phrases with lead mono melodies

***

## Notes:

* Lead mono melodies are within 24-64 notes count range
* Phrases were algorithmically extracted so there may be some inconsistencies
* Each pickle file entry has format: [original MIDI md5 hash, mono melody patch number, delta score]
* Source MIDI dataset: [Monster MIDI Dataset](https://github.com/asigalov61/Monster-MIDI-Dataset)

***

## Easily decode to MIDI with TMIDIX Python module from tegridy-tools

```
!git clone --depth 1 https://github.com/asigalov61/tegridy-tools
```

```
import TMIDIX
import random

mono_phrases = TMIDIX.Tegridy_Any_Pickle_File_Reader('mono_phrases')
```

```
song = random.choice(mono_phrases)

print('=' * 70)
print('Source MIDI MD5 hash:', song[0])
print('Melody patch-instrument:', song[1], ' --- ', TMIDIX.Number2patch[song[1]])
print('=' * 70)

delta_score = song[2]

abs_score = []
abs_time = 0

for e in delta_score:
  abs_time += e[0]
  ee = ['note'] + copy.deepcopy(e)
  ee[1] = abs_time
  abs_score.append(ee)

output_score, patches, overflow_patches = TMIDIX.patch_enhanced_score_notes(abs_score)

detailed_stats = TMIDIX.Tegridy_ms_SONG_to_MIDI_Converter(abs_score,
                                                          output_signature = song[0],
                                                          output_file_name = 'Mono-Phrases-Composition',
                                                          track_name='Project Los Angeles',
                                                          list_of_MIDI_patches=patches,
                                                          timings_multiplier=16,
                                                          )
print('=' * 70)
```

***

### Project Los Angeles
## Tegridy Code 2024
