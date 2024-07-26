# Clean Melodies
## 117659 processed monophonic melodies for MIR and Music AI purposes

## Please CC BY-NC-SA

***

## There are four pickle files in the archive:

* clean_melodies.pickle is a main pickle file which contains all meldoies, along with their pitches and delta pitches
* clean_melodies_select_grouped.pickle is a subset of the main file above and it contains 5158 melodies selected and grouped by similarity and trimmed to the exact music phrases
* clean_melodies_all_most_common_patterns.pickle contains all most common delta pitches patterns extracted from all Clean Melodies
* clean_melodies_select_most_common_patterns.pickle contains actual select melodies chunks matched from all most common Clean Melodies patterns

***

## Easily decode to MIDI with tegridy-tools TMIDIX Python module like so:

```
!git clone --depth 1 https://github.com/asigalov61/tegridy-tools 
```

```
# Import modules

import TMIDIX
import random

# Load melodies...

clean_melodies, clean_melodies_pitches, clean_melodies_delta_pitches = TMIDIX.Tegridy_Any_Pickle_File_Reader('clean_melodies')

# Decode to MIDI...

song = random.choice(clean_melodies)

song_f = []

time = 0
dur = 0
vel = 90
pitch = 60
channel = 0

for ss in song:

    time += ss[0] * 32

    dur = ss[1] * 32

    pitch = ss[2]

    song_f.append(['note', time, dur, channel, pitch, vel, 0])

detailed_stats = TMIDIX.Tegridy_ms_SONG_to_MIDI_Converter(song_f,
                                                          output_signature = 'Clean Melodies',
                                                          output_file_name = 'Clean Melodies Composition',
                                                          track_name='Project Los Angeles'
                                                          )
```

***

### Project Los Angeles
### Tegridy Code 2024
