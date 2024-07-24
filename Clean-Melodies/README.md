# Clean Melodies
## 117659 processed monophonic melodies for MIR and Music AI purposes

***

## Decode with tegridy-tools TMIDIX Python module like so:

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

Please CC BY-NC-SA

***

### Project Los Angeles
### Tegridy Code 2024
