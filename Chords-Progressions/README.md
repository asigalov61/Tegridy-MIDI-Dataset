# Chords Progressions
## 1.25M+ pitches chords progressions for MIR and Music AI purposes

***

## Pitches Chords Progressions Generator (GPU/CPU)

[![Open In Colab][colab-badge]][colab-notebook1]

[colab-notebook1]: <https://colab.research.google.com/github/asigalov61/Tegridy-MIDI-Dataset/blob/master/Chords-Progressions/Pitches_Chords_Progressions_Generator.ipynb>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>

### Generate complete unique songs from pitches chords progressions

***

## 🤗 [Pitches Chords Progression Generator LIVE demo on Hugging Face](https://huggingface.co/spaces/asigalov61/Chords-Progressions-Generator) 🤗

***

## 🎧 Listen to [Pitches Chords Progression Generator Samples on SoundCloud](https://soundcloud.com/aleksandr-sigalov-61/sets/pitches-chords-progressions) 🎧

***

## Notes:

* For the sake of practicality provided pickle file contains only select chords progressions
* All chords progressions have at least 5 pitches chords
* All chords in each chord progression are between 3 and 15 pitches long
* All pitches chords in all chords progressions are unique
* Most of the chords progressions were sourced from [Los Angeles MIDI dataset](https://github.com/asigalov61/Los-Angeles-MIDI-Dataset)

***

## 45778 Times-Chords-Drums Songs Addendum

***

* This archive contains a pickle file with 45778 select songs from Los Angeles MIDI Dataset
* Each song score contains 128-256 chords progresion and a drum track
* Each song score is in the format (delta start time, tones chord, drums pitches)
* This is useful for chords mixing, chords analysis and for other purposes

***

### You can easily decode each score with TMIDIX module from tegridy-tools as follows:

```
import TMIDIX

times_chords_drums_songs = TMIDIX.Tegridy_Any_Pickle_File_Reader('45778_times_chords_drums_songs_128_256')

song = random.choice(times_chords_drums_songs)

fn = song[0]
score = song[1]

output_score = []

time = 0

for i, s in enumerate(score):

  time += s[0][0] * 16
  dur = 4 * 16

  tchord = s[1]

  for t in tchord:

    output_score.append(['note', time, dur, 0,  60+t, 90, 0])

  drums = s[2]

  for d in drums:
    output_score.append(['note', time, dur, 9, d, 110, 128])

detailed_stats = TMIDIX.Tegridy_ms_SONG_to_MIDI_Converter(output_score,
                                                          output_signature = fn,
                                                          output_file_name = 'Times-Chords-Drums-Composition',
                                                          track_name='Project Los Angeles'
                                                          )
```

***

### Project Los Angeles
### Tegridy Code 2024
