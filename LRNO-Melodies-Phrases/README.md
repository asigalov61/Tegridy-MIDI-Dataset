# LRNO Melodies Phrases
## 154344 longest repeating non-overlapping monophonic melodies phrases

***

### Archive files descriptions

* LRNO_Melodies_Phrases_CC_BY_NC_SA pickle file contains 154344 longest repeating non-overlapping monophonic melodies phrases 24-64 notes each
* LRNO_Melodies_Phrases_Transposed_CC_BY_NC_SA pickle file contains the same melodies phrases transposed to average C4

***

## Easily decode to MIDI with tegridy-tools TMIDIX Python module like so:

```sh
!git clone --depth 1 https://github.com/asigalov61/tegridy-tools 
```

```python
# Import modules

import TMIDIX
import random

# Load melodies...

lrno_melodies_phrases = TMIDIX.Tegridy_Any_Pickle_File_Reader('LRNO_Melodies_Phrases_CC_BY_NC_SA.pickle')

# Decode to MIDI...

song = random.choice(lrno_melodies_phrases)

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
                                                          output_signature = 'LRNO Melody Phrase',
                                                          output_file_name = 'LRNO-Melody-Phrase-Composition',
                                                          track_name='Project Los Angeles'
                                                          )
```

***

### Source MIDI datasets:

### [Godzilla](https://huggingface.co/datasets/projectlosangeles/Godzilla-MIDI-Dataset)
### [popular hook](https://huggingface.co/datasets/NEXTLab-ZJU/popular-hook)

***

### Project Los Angeles
### Tegridy Code 2025
