# -*- coding: utf-8 -*-
"""Pitches_Chords_Progressions_Generator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/asigalov61/Tegridy-MIDI-Dataset/blob/master/Chords-Progressions/Pitches_Chords_Progressions_Generator.ipynb

# Pitches Chords Progressions Generator (ver. 1.0)

***

Powered by tegridy-tools: https://github.com/asigalov61/tegridy-tools

***

#### Project Los Angeles

#### Tegridy Code 2024

***

# (SETUP ENVIRONMENT)
"""

# @title Install dependecies
!git clone --depth 1 https://github.com/asigalov61/tegridy-tools
!apt install fluidsynth

# Commented out IPython magic to ensure Python compatibility.
#@title Import all needed modules

print('=' * 70)
print('Loading core modules...')

import os
import random
from collections import Counter

from tqdm import tqdm

import matplotlib.pyplot as plt

from IPython.display import Audio, display

print('=' * 70)
print('Loading NumPy/CuPy...')
print('=' * 70)

try:
  import cupy as np
  print('Will use CuPy with GPU acceleration...')
except:
  import numpy as np
  print('Will use NumPy without GPU acceleration...')

print('=' * 70)
print('Loading TMIDIX module...')

# %cd /content/tegridy-tools/tegridy-tools

import TMIDIX
from midi_to_colab_audio import midi_to_colab_audio

# %cd /content/

print('=' * 70)
print('Done!')
print('=' * 70)

"""# (PREP CHORDS DATASET)"""

# Commented out IPython magic to ensure Python compatibility.
# @title Download and unzip Pitches Chords Progressions dataset
print('=' * 70)
print('Downloading and unzipping Pitches Chords Progressions dataset...')
print('=' * 70)

# %cd /content/

!wget https://github.com/asigalov61/Tegridy-MIDI-Dataset/raw/master/Chords-Progressions/Pitches-Chords-Progressions-CC-BY-NC-SA.zip.001
!wget https://github.com/asigalov61/Tegridy-MIDI-Dataset/raw/master/Chords-Progressions/Pitches-Chords-Progressions-CC-BY-NC-SA.zip.002

!cat Pitches-Chords-Progressions-CC-BY-NC-SA.zip.* > Pitches-Chords-Progressions-CC-BY-NC-SA.zip

!rm Pitches-Chords-Progressions-CC-BY-NC-SA.zip.001
!rm Pitches-Chords-Progressions-CC-BY-NC-SA.zip.002

!unzip Pitches-Chords-Progressions-CC-BY-NC-SA.zip

!rm Pitches-Chords-Progressions-CC-BY-NC-SA.zip

print('=' * 70)
print('Done!')
print('=' * 70)

# @title Load/Reload Pitches Chords Progressions dataset
print('=' * 70)
print('Loading Pitches Chords Progressions dataset...')
print('=' * 70)

good_chords_chunks = TMIDIX.Tegridy_Any_Pickle_File_Reader('/content/pitches_chords_progressions_5_3_15')

print('=' * 70)
print('Total loaded chords progressions:', len(good_chords_chunks))
print('=' * 70)

"""# (GENERATE PROGRESSIONS)

## There are two chords progressions generators to chooses from

* Chord-by-chord progressions generator produces more unique shorter progressions

* Chunk-by-chunk progressions generator produces more structured longer progressions

## (CHORD-BY-CHORD GENERATION)
"""

# @title Load and prep chords

print('=' * 70)
print('Creating chords dictionary...')
print('=' * 70)

tones_chords_dict = set()

for a in tqdm(good_chords_chunks):
  for aa in a:
    tones_chord = tuple(sorted(set([p % 12 for p in aa])))
    tones_chords_dict.add(tones_chord)

tones_chords_dict = list(tones_chords_dict)

print('=' * 70)
print('Resulting chords dictionary size:', len(tones_chords_dict))
print('=' * 70)
print('Preparing chords chunks...')
print('=' * 70)

all_chords_tokens_chunks = []
all_good_chords_chunks = []

for a in tqdm(good_chords_chunks):

  chunk = []

  for aa in a:

    tones_chord = tuple(sorted(set([p % 12 for p in aa])))
    chunk.append(tones_chords_dict.index(tones_chord))

  if chunk:
    all_chords_tokens_chunks.append(chunk)
    all_good_chords_chunks.append(a)

print('Done!')
print('=' * 70)
print('Total chords chunks count:', len(all_good_chords_chunks))
print('=' * 70)

# @title Split chords progressions into chunks

#@markdown Adjust chords chunks length for different generation results

chords_chunk_length = 5 # @param {"type":"slider","min":5,"max":8,"step":1}

print('=' * 70)
print('Preparing chords chunks...')
print('=' * 70)

all_chords = []
all_tokens = []

cidx = 0

for a in tqdm(all_good_chords_chunks):

  if len(a) == chords_chunk_length:
    all_chords.append(a)
    all_tokens.append(all_chords_tokens_chunks[cidx])

  else:
    for i in range(0, len(a)-chords_chunk_length, 2):
      all_chords.append(a[i:i+chords_chunk_length])
      all_tokens.append(all_chords_tokens_chunks[cidx][i:i+chords_chunk_length])

  cidx += 1

print('Done!')
print('=' * 70)
print('Total number of prepared chords chunks:', len(all_chords))
print('=' * 70)
print('Loading chords chunks...')

src_chunks = np.array([a[:-1] for a in all_tokens])

print('=' * 70)
print('Done!')
print('=' * 70)

# @title Generate chord progressions

#@markdown NOTE: You can stop the generation at any time to render partial results

#@markdown Generation options

minimum_song_length_in_chords = 30 # @param {"type":"slider","min":8,"max":50,"step":1}
chords_chunks_memory_length = -1 # @param {"type":"slider","min":-1,"max":30,"step":1}

#@markdown MIDI rendering options

chord_time_step = 500 # @param {"type":"slider","min":100,"max":1000,"step":50}

melody_MIDI_patch_number = 40 # @param {"type":"slider","min":-1,"max":127,"step":1}
chords_progression_MIDI_patch = 0 # @param {"type":"slider","min":0,"max":127,"step":1}
base_MIDI_patch_number = 35 # @param {"type":"slider","min":-1,"max":127,"step":1}

render_MIDI_to_audio = True # @param {"type":"boolean"}

print('=' * 70)
print('Chord-by-Chord Generator')
print('=' * 70)
print('Generating...')
print('=' * 70)

song_length = minimum_song_length_in_chords

tries = 0

song = []

max_song_len = 0

tokens = [0]

while len(song) < song_length:

  try:

    song = []
    tokens = []
    seen = []

    chunk = [[i] for i in range(5)]

    while len(set([p[0] % 12 for p in chunk])) >= 5:
      ridx = random.randint(0, len(all_tokens)-1)

      chunk = all_chords[ridx]

    song.extend(chunk)
    tokens.extend(all_tokens[ridx])

    for i in range(song_length):

      trg_chunk = np.array(tokens[-(chords_chunk_length-1):])

      idxs = np.where((src_chunks == trg_chunk).all(axis=1))[0]

      if len(idxs) > random.randint(0, 2):

        found = False
        cidxs = idxs.tolist()

        if len(cidxs) > 1:
          random.shuffle(cidxs)

        for sidx in cidxs:
          if sidx not in seen:

            song.append(all_chords[sidx][-1])
            tokens.append(all_tokens[sidx][-1])
            seen.append(sidx)

            if chords_chunks_memory_length > 0:
              seen = seen[-chords_chunks_memory_length:]

            elif chords_chunks_memory_length == 0:
              seen = []

            found = True

            break

        if not found:
          break

      else:
        if len(song) > max_song_len:
          print('Current song length:', len(song), 'chords')
          print('=' * 70)
          final_song = song
        max_song_len = max(max_song_len, len(song))

        tries += 1
        break

    if tries % 500 == 0:
      print('Number of passed tries:', tries)
      print('=' * 70)

  except KeyboardInterrupt:
    print('Stopping generation...')
    print('=' * 70)
    break

if len(song) > len(final_song):
  final_song = song

print('Generated final song after', tries, 'tries with', len(final_song), 'chords')
print('=' * 70)
print('Converting song to MIDI...')
print('=' * 70)

output_score = []

time = 0

patches = [0] * 16
patches[0] = chords_progression_MIDI_patch

if base_MIDI_patch_number > -1:
  patches[2] = base_MIDI_patch_number

if melody_MIDI_patch_number > -1:
  patches[3] = melody_MIDI_patch_number

chords_labels = []

for i, s in enumerate(final_song):

  time += chord_time_step

  dur = chord_time_step

  chord_str = str(i+1)

  for t in sorted(set([t % 12 for t in s])):
    chord_str += '-' + str(t)

  chords_labels.append(['text_event', time, chord_str])

  for p in s:
    output_score.append(['note', time, dur, 0, p, max(40, p), chords_progression_MIDI_patch])

  if base_MIDI_patch_number > -1:
    output_score.append(['note', time, dur, 2, (s[-1] %  12)+24, 120-(s[-1] %  12), base_MIDI_patch_number])

if melody_MIDI_patch_number > -1:
  output_score = TMIDIX.add_melody_to_enhanced_score_notes(output_score, melody_patch=melody_MIDI_patch_number)

midi_score = sorted(chords_labels + output_score, key=lambda x: x[1])

detailed_stats = TMIDIX.Tegridy_ms_SONG_to_MIDI_Converter(midi_score,
                                                          output_signature = 'Pitches Chords Progression',
                                                          output_file_name = '/content/Pitches-Chords-Progression-Composition',
                                                          track_name='Project Los Angeles',
                                                          list_of_MIDI_patches=patches
                                                          )

print('=' * 70)
print('Displaying resulting composition...')
print('=' * 70)

fname = '/content/Pitches-Chords-Progression-Composition'

if render_MIDI_to_audio:
  midi_audio = midi_to_colab_audio(fname + '.mid')
  display(Audio(midi_audio, rate=16000, normalize=False))

TMIDIX.plot_ms_SONG(output_score, plot_title=fname)

# @title Print song chords stats

all_song_chords = []

for pc in song:
  tones_chord = tuple(sorted(set([p % 12 for p in pc])))
  all_song_chords.append([pc, tones_chord])

print('=' * 70)
print('Total number of chords:', len(all_song_chords))
print('=' * 70)
print('Most common pitches chord:', list(Counter(tuple([a[0] for a in all_song_chords])).most_common(1)[0][0]), '===', Counter(tuple([a[0] for a in all_song_chords])).most_common(1)[0][1], 'count')
print('=' * 70)
print('Most common tones chord:', list(Counter(tuple([a[1] for a in all_song_chords])).most_common(1)[0][0]), '===', Counter(tuple([a[1] for a in all_song_chords])).most_common(1)[0][1], 'count')
print('=' * 70)
print('Sorted unique songs chords set:', len(sorted(set(tuple([a[1] for a in all_song_chords])))), 'count')
print('=' * 70)
for c in sorted(set(tuple([a[1] for a in all_song_chords]))):
  print(list(c))
print('=' * 70)
print('Grouped songs chords set:', len(TMIDIX.grouped_set(tuple([a[1] for a in all_song_chords]))), ' count')
print('=' * 70)
for c in TMIDIX.grouped_set(tuple([a[1] for a in all_song_chords])):
  print(list(c))
print('=' * 70)
print('All songs chords')
print('=' * 70)
for i, pc_tc in enumerate(all_song_chords):
  print('Song chord #', i)
  print(list(pc_tc[0]), '===', list(pc_tc[1]))
  print('=' * 70)

"""## (CHUNK-BY-CHUNK GENERATION)"""

# @title Select chords chunks

#@markdown Adjust minimum chords chunks length for different generation results

minimum_chords_chunk_length = 4 # @param {"type":"slider","min":4,"max":8,"step":1}
chords_chunks_overlap_value = 4 # @param {"type":"slider","min":2,"max":8,"step":1}

print('=' * 70)
print('Selecting chords chunks...')
print('=' * 70)

chunk_size = minimum_chords_chunk_length

long_chords_chunks = []

for c in tqdm(good_chords_chunks):
  if chunk_size + chords_chunks_overlap_value <= len(c):
    long_chords_chunks.append(c)

print('Done!')
print('=' * 70)
print('Selected chords chunks of minimum length:', minimum_chords_chunk_length+chords_chunks_overlap_value)
print('=' * 70)
print('Total number of selected chord chunks:', len(long_chords_chunks))
print('=' * 70)

# @title Multiply chords chunks

#@markdown Larger multiplication factor produces better results, especially on smaller chords progressions datasets

chords_chunks_multiplicatrion_factor = 6 # @param {"type":"slider","min":1,"max":6,"step":1}

#===============================================================================
# Helper chord function
#===============================================================================

def check_chord(chord):

  tones_chord = sorted(set([p % 12 for p in chord]))

  new_tones_chord = []

  if 0 in tones_chord and 11 in tones_chord:
    tones_chord.remove(11)

  for t in tones_chord:
    if t+1 in tones_chord:
      tones_chord.remove(t+1)
    if t-1 in tones_chord:
      tones_chord.remove(t-1)

  new_chord = tuple()

  for p in chord:
    if p % 12 in tones_chord:
      new_chord += tuple([p])

  if len(new_chord) > 2:
    return new_chord

  else:
    return None

#===============================================================================

print('=' * 70)
print('Multiplying chords chunks...')
print('=' * 70)
print('Chords chunks will be multiplied', chords_chunks_multiplicatrion_factor * 2, 'times' )
print('=' * 70)

long_chords_chunks_mult = set()

for c in tqdm(long_chords_chunks):

  for tv in range(-chords_chunks_multiplicatrion_factor, chords_chunks_multiplicatrion_factor):
    gc = []
    for cc in c:
      chord = [max(1, min(127, p+tv)) for p in cc]
      checked_chord = check_chord(chord)
      if checked_chord is not None:
        gc.append(checked_chord)
    if len(gc) == len(c) or (len(gc) >= chunk_size + chords_chunks_overlap_value and gc == c[:len(gc)]) or (len(gc) >= chunk_size + chords_chunks_overlap_value and gc == c[len(gc):]):
      long_chords_chunks_mult.add(tuple(gc))

print('Done!')
print('=' * 70)
print('Total number of multiplied chords chunks:', len(long_chords_chunks_mult))
print('=' * 70)

# @title Prep and load multiplied chords chunks

print('=' * 70)
print('Creating chords dictionary...')
print('=' * 70)

long_tones_chords_dict = set()

for a in tqdm(long_chords_chunks_mult):
  for aa in a:
    tones_chord = tuple(sorted(set([p % 12 for p in aa])))
    long_tones_chords_dict.add(tones_chord)

long_tones_chords_dict = list(long_tones_chords_dict)

print('=' * 70)
print('Resulting chords dictionary size:', len(long_tones_chords_dict))
print('=' * 70)
print('Preparing chords chunks...')
print('=' * 70)

all_long_chords_tokens_chunks = []
all_long_good_chords_chunks = []

for a in tqdm(long_chords_chunks_mult):

  chunk = []

  for aa in a:

    tones_chord = tuple(sorted(set([p % 12 for p in aa])))
    chunk.append(long_tones_chords_dict.index(tones_chord))

  if chunk:
    all_long_chords_tokens_chunks.append(chunk)
    all_long_good_chords_chunks.append(a)

print('Done!')
print('=' * 70)
print('Loading chords chunks...')

src_long_chunks = np.array([a[:chunk_size] for a in all_long_chords_tokens_chunks])

print('Done!')
print('=' * 70)
print('Total chords chunks count:', len(all_long_good_chords_chunks))
print('=' * 70)

# @title Generate chords progressions

#@markdown NOTE: You can stop the generation at any time to render partial results

#@markdown Generation options

total_song_length_in_chords_chunks = 13 # @param {"type":"slider","min":5,"max":20,"step":1}
chords_chunks_memory_length = -1 # @param {"type":"slider","min":-1,"max":30,"step":1}

#@markdown MIDI rendering options

chord_time_step = 500 # @param {"type":"slider","min":100,"max":1000,"step":50}

melody_MIDI_patch_number = 40 # @param {"type":"slider","min":-1,"max":127,"step":1}
chords_progression_MIDI_patch = 0 # @param {"type":"slider","min":0,"max":127,"step":1}
base_MIDI_patch_number = 35 # @param {"type":"slider","min":-1,"max":127,"step":1}

render_MIDI_to_audio = True # @param {"type":"boolean"}

print('=' * 70)
print('Chunk-by-Chunk Generator')
print('=' * 70)
print('Generating...')
print('=' * 70)

matching_long_chords_chunks = []

ridx = random.randint(0, len(all_long_chords_tokens_chunks)-1)

matching_long_chords_chunks.append(ridx)

max_song_len = 0

tries = 0

while len(matching_long_chords_chunks) < total_song_length_in_chords_chunks:

  try:

    matching_long_chords_chunks = []

    ridx = random.randint(0, len(all_long_chords_tokens_chunks)-1)

    matching_long_chords_chunks.append(ridx)
    seen = [ridx]

    for a in range(16):

      schunk = all_long_chords_tokens_chunks[matching_long_chords_chunks[-1]]
      trg_long_chunk = np.array(schunk[-chunk_size:])
      idxs = np.where((src_long_chunks == trg_long_chunk).all(axis=1))[0].tolist()

      if len(idxs) > 1:
        eidx = random.choice(idxs)
        tr = 0
        while eidx in seen and tr < 5:
          eidx = random.choice(idxs)
          tr += 1

        if eidx not in seen:

          matching_long_chords_chunks.append(eidx)
          seen.append(eidx)

          if chords_chunks_memory_length > 0:
            seen = seen[-chords_chunks_memory_length:]
          elif chords_chunks_memory_length == 0:
            seen = []

        else:
          break

      else:
        break

    if len(matching_long_chords_chunks) > max_song_len:
      print('Current song length:', len(matching_long_chords_chunks), 'chords chunks')
      print('=' * 70)
      final_song = matching_long_chords_chunks

    max_song_len = max(max_song_len, len(matching_long_chords_chunks))

    tries += 1

    if tries % 500 == 0:
      print('Number of passed tries:', tries)
      print('=' * 70)

  except KeyboardInterrupt:
    print('Stopping generation...')
    print('=' * 70)
    break

if len(matching_long_chords_chunks) > max_song_len:
  print(len(matching_long_chords_chunks))
  final_song = matching_long_chords_chunks

f_song = []

for mat in final_song:
  f_song.extend(all_long_good_chords_chunks[mat][:-chunk_size])
f_song.extend(all_long_good_chords_chunks[mat][-chunk_size:])

print('Generated final song after', tries, 'tries with', len(final_song), 'chords chunks and', len(f_song), 'chords')
print('=' * 70)

output_score = []

time = 0

patches = [0] * 16
patches[0] = chords_progression_MIDI_patch

if base_MIDI_patch_number > -1:
  patches[2] = base_MIDI_patch_number

if melody_MIDI_patch_number > -1:
  patches[3] = melody_MIDI_patch_number

chords_labels = []

for i, s in enumerate(f_song):

  time += chord_time_step

  dur = chord_time_step

  chord_str = str(i+1)

  for t in sorted(set([t % 12 for t in s])):
    chord_str += '-' + str(t)

  chords_labels.append(['text_event', time, chord_str])

  for p in s:
    output_score.append(['note', time, dur, 0, p, max(40, p), chords_progression_MIDI_patch])

  if base_MIDI_patch_number > -1:
    output_score.append(['note', time, dur, 2, (s[-1] %  12)+24, 120-(s[-1] %  12), base_MIDI_patch_number])

if melody_MIDI_patch_number > -1:
  output_score = TMIDIX.add_melody_to_enhanced_score_notes(output_score, melody_patch=melody_MIDI_patch_number)

midi_score = sorted(chords_labels + output_score, key=lambda x: x[1])

detailed_stats = TMIDIX.Tegridy_ms_SONG_to_MIDI_Converter(midi_score,
                                                          output_signature = 'Pitches Chords Progression',
                                                          output_file_name = '/content/Pitches-Chords-Progression-Composition',
                                                          track_name='Project Los Angeles',
                                                          list_of_MIDI_patches=patches
                                                          )

print('=' * 70)
print('Displaying resulting composition...')
print('=' * 70)

fname = '/content/Pitches-Chords-Progression-Composition'

if render_MIDI_to_audio:
  midi_audio = midi_to_colab_audio(fname + '.mid')
  display(Audio(midi_audio, rate=16000, normalize=False))

TMIDIX.plot_ms_SONG(output_score, plot_title=fname)

# @title Print song chords stats

all_song_chords = []

for pc in f_song:
  tones_chord = tuple(sorted(set([p % 12 for p in pc])))
  all_song_chords.append([pc, tones_chord])

print('=' * 70)
print('Total number of chords:', len(all_song_chords))
print('=' * 70)
print('Most common pitches chord:', list(Counter(tuple([a[0] for a in all_song_chords])).most_common(1)[0][0]), '===', Counter(tuple([a[0] for a in all_song_chords])).most_common(1)[0][1], 'count')
print('=' * 70)
print('Most common tones chord:', list(Counter(tuple([a[1] for a in all_song_chords])).most_common(1)[0][0]), '===', Counter(tuple([a[1] for a in all_song_chords])).most_common(1)[0][1], 'count')
print('=' * 70)
print('Sorted unique songs chords set:', len(sorted(set(tuple([a[1] for a in all_song_chords])))), 'count')
print('=' * 70)
for c in sorted(set(tuple([a[1] for a in all_song_chords]))):
  print(list(c))
print('=' * 70)
print('Grouped songs chords set:', len(TMIDIX.grouped_set(tuple([a[1] for a in all_song_chords]))), ' count')
print('=' * 70)
for c in TMIDIX.grouped_set(tuple([a[1] for a in all_song_chords])):
  print(list(c))
print('=' * 70)
print('All songs chords')
print('=' * 70)
for i, pc_tc in enumerate(all_song_chords):
  print('Song chord #', i)
  print(list(pc_tc[0]), '===', list(pc_tc[1]))
  print('=' * 70)

"""# Congrats! You did it! :)"""