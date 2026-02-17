# Discover Karaoke
## 42294 English karaoke melodies extracted from all English karaoke MIDIs in [Discover MIDI](https://huggingface.co/datasets/projectlosangeles/Discover-MIDI-Dataset) dataset

<img width="1024" height="1024" alt="Discover-Karaoke" src="https://github.com/user-attachments/assets/ba6c5226-fd4b-4977-ae8e-567a234814ac" />

***

## Convert to MIDI as follows

```python
# https://github.com/asigalov61/tegridy-tools
import TMIDIX

discover_karaoke = TMIDIX.Tegridy_Any_Pickle_File_Reader('Discover_Karaoke_CC_BY_NC_SA')

output_score = []

md5, score = random.choice(discover_karaoke)

time = 0

for e in score:
    
    time += e[0]
    dur = e[1]
    pitch = e[2]
    word = e[3]

    output_score.append(['text_event', time, word])
    output_score.append(['note', time, dur, 3, pitch, 120, 40])
    
detailed_stats = TMIDIX.Tegridy_ms_SONG_to_MIDI_Converter(output_score,
                                                          output_signature = 'Discover Karaoke Melody',
                                                          output_file_name = md5,
                                                          track_name='Project Los Angeles',
                                                          timings_multiplier=32
                                                          )
```

***

### Project Los Angeles
### Tegridy Code 2026
