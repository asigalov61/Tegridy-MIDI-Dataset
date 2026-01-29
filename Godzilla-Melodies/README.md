# Godzilla Melodies
## 356460 raw select melodies from [Godzilla MIDI Dataset](https://huggingface.co/datasets/projectlosangeles/Godzilla-MIDI-Dataset)

![Godzilla-Melodies](https://cdn-uploads.huggingface.co/production/uploads/5f57ea2d3f32f12a3c0692e6/z6xrjgvl--qlwGHgte5Mi.png)

***

## Each dataset entry contains the following

* MIDI name (md5 hash)
* MIDI instrument number
* MIDI instrument name
* Tokenized melody score
* LRNO pitches pattern (if present)

***

## 🤗 Download [Godzilla Melodies](https://huggingface.co/datasets/asigalov61/Godzilla-Melodies) dataset from Hugging Face 🤗

***

## Basic use guide

### Load dataset

```python
# Load dataset
import TMIDIX

godzilla_melodies = TMIDIX.read_jsonl('DATA/Godzilla_Melodies_CC_BY_NC_SA.jsonl')
```

### Decode to MIDI

```python
# Helper decoder function
def tokens_to_score(tokens):

    time = 0
    dur = 1
    vel = 90
    pitch = 60
    channel = 0
    patch = 0

    score = []

    for m in tokens:

        if 0 <= m < 128:
            time += m * 32

        elif 128 < m < 256:
            dur = (m-128) * 32

        elif 256 < m < 384:
            pitch = (m-256)

            score.append(['note', time, dur, channel, pitch, vel, patch])

    return score

# Decode to MIDI
melody_index = 0

tokenized_melody_score = godzilla_melodies[melody_index]['score']

melody_score = tokens_to_score(tokenized_melody_score)

detailed_stats = TMIDIX.Tegridy_ms_SONG_to_MIDI_Converter(melody_score,
                                                          output_signature = 'Godzilla Melodies',
                                                          output_file_name = 'Godzilla-Melodies-Composition',
                                                          track_name='Project Los Angeles'
                                                          )
```

### Project Los Angeles
### Tegridy Code 2026
