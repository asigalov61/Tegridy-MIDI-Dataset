# Discover Mono Melodies
## 556463 pre-tokenized LRNO monophonic melodies segments from [Discover MIDI](https://huggingface.co/datasets/projectlosangeles/Discover-MIDI-Dataset) dataset

***

## NOTE: All melodies have been transposed to an average C4

***

```python
import TMIDIX

tokens = discover_mono_melodies[0]

time = 0
dur = 1
vel = 90
pitch = 60
channel = 0
patch = 0

song_f = []

for t in tokens:
    
    if 0 <= t < 128:
        time += t * 32

    elif 128 < t < 256:
        pitch = (t-128)

    elif 256 < t < 384:
        dur = (t-256) * 32

        song_f.append(['note', time, dur, 0, pitch, max(40, pitch), 0])
    
TMIDIX.Tegridy_ms_SONG_to_MIDI_Converter(
    song_f,
    output_signature='Discover Mono Melody',
    output_file_name='Discover-Mono-Melody',
    track_name='Project Los Angeles',
)
```

***

### Project Los Angeles
### Tegridy Code 2026
