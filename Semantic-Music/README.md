# [Experimental] [WIP] Semantic Music
## Semantic music datasets, supplemental data and code

***

## Sematic Music Dataset Maker

[![Open In Colab][colab-badge]][colab-notebook1]

[colab-notebook1]: <https://colab.research.google.com/github/asigalov61/Tegridy-MIDI-Dataset/blob/master/Semantic-Music/Semantic_Music_Dataset_Maker.ipynb>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>

### Make your own semantic music dataset

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

## Attribution

### [lyrics dataset](https://huggingface.co/datasets/tsterbak/lyrics-dataset)
### [song lyrics](https://huggingface.co/datasets/amishshah/song_lyrics)
### [POP909 MIDI dataset](https://github.com/music-x-lab/POP909-Dataset)
### [ASAP MIDI dataset](https://github.com/fosfrancesco/asap-dataset)
### [370k English words corpus](https://www.kaggle.com/datasets/ruchi798/part-of-speech-tagging/)
### [google 10000 english](https://github.com/first20hours/google-10000-english)


***

### Project Los Angeles
### Tegridy Code 2024
