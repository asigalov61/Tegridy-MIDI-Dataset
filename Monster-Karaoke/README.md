# Monster Karaoke
## 13k+ English Karaoke Melodies from [Monster MIDI Dataset](https://github.com/asigalov61/Monster-MIDI-Dataset)

![Monster-Karaoke-Logo](https://github.com/user-attachments/assets/69008f1c-fe9c-41c2-8087-ce6860865c97)

***


### Easily decode with TMIDIX module from tegridy-tools

```sh
!git clone --depth 1 https://github.com/asigalov61/tegridy-tools
```

```python
#======================================================

import TMIDIX

#======================================================

monster_karaoke = TMIDIX.Tegridy_Any_Pickle_File_Reader('Monster_Karaoke_CC_BY_NC_SA.pickle')

#======================================================

melody_index = 2

#======================================================

monster_midi_dataset_md5_hash = monster_karaoke[melody_index][0]
orig_patch = monster_karaoke[melody_index][1]
kar_mel = monster_karaoke[melody_index][2]

#======================================================

patches = [0] * 16
patches[0] = orig_patch

dtime = 0

output_score = []

for e in kar_mel:

    word = e[0]
    dtime += e[1] * 16
    dur = e[2] * 16
    ptc = e[3]

    output_score.append(['text_event', dtime, word])
    output_score.append(['note', dtime, dur, 0, ptc, ptc, orig_patch])


detailed_stats = TMIDIX.Tegridy_ms_SONG_to_MIDI_Converter(output_score,
                                                          output_signature = 'Monster Karaoke Melody',
                                                          output_file_name = 'Monster-Karaoke-Melody-'+str(melody_index),
                                                          track_name='Project Los Angeles',
                                                          list_of_MIDI_patches=patches
                                                          )
```

***

### Project Los Angeles
### Tegridy Code 2025
