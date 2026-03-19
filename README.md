# Tegridy MIDI Dataset

## Ultimate Multi-Instrumental MIDI Dataset for MIR and Music AI purposes

![Tegridy-MIDI-Dataset-Logo](https://github.com/user-attachments/assets/3b57ac86-652c-4a74-8966-2d92e0fcaed0)

***

## Please CC BY-NC-SA

***

# Install:

```
!git clone --depth 1 https://github.com/asigalov61/Tegridy-MIDI-Dataset
```

***

# Must-have MIDI datasets:

This list contains a wide variety of MIDI datasets, from massive, processed corpora designed for machine learning to smaller, thematic collections for specific research or hobbies. The descriptions below are based on the content of each provided link. You'll notice a few different "types" of datasets:

* **Massive, Curated Datasets (e.g., Discover, Godzilla, Meta):** These are enormous collections (often millions of files) that have been aggregated, de-duplicated, normalized, and enriched with extensive metadata and pre-computed features. They are typically designed for large-scale Music Information Retrieval (MIR) and training symbolic music AI models, and often come with their own tooling for search and analysis.
* **Specialized Research Datasets (e.g., MAESTRO, GiantMIDI, POP909):** These are smaller, high-quality datasets created for specific research tasks. They often feature precise alignments (e.g., note to performed audio), expert annotations (e.g., emotion, structure), or a focus on a particular genre or instrumentation.
* **Thematic Collections & Archives (e.g., Touhou MIDI Collection, wild-west-midi-2, classical-music-midi):** These are generally smaller, community-driven collections focused on a specific genre, game, or artist. They are often shared on GitHub or Hugging Face and are valuable for fans, hobbyists, and specific analytical tasks.

## [Discover](https://huggingface.co/datasets/projectlosangeles/Discover-MIDI-Dataset)
A massive, production-ready dataset containing **over 6.74 million unique, de-duplicated, and normalized MIDI files**. It is specifically built for large-scale Music Information Retrieval (MIR), music discovery, and symbolic music AI. The dataset includes rich, precomputed metadata (features counts, genre labels, artist/title IDs) and a custom **GPU-accelerated search engine** for rapid similarity searches and filtering across the entire collection. It also comes with supplemental code for tasks like loop extraction.

## [Godzilla](https://huggingface.co/datasets/projectlosangeles/Godzilla-MIDI-Dataset)
An enormous, comprehensive MIDI dataset with **over 5.8 million unique, de-duped, and normalized MIDIs**. Each file has been converted to a proper MIDI specification and integrity-checked. It features extensive metadata, including basic features, mono-melody information, pitches-patches counts, and **text captions** describing the music in each file. Like the Discover dataset, it includes highly optimized, GPU-accelerated search and filter code, making it suitable for large-scale MIR and AI model training.

## [Sourdough](https://huggingface.co/datasets/BreadAi/Sourdough-midi-dataset)
*(Description based on citation within the Discover/Godzilla pages)*
A MIDI dataset from BreadAi. The dataset contains 5M+ raw deduplicated MIDIs.

## [Monster](https://github.com/asigalov61/Monster-MIDI-Dataset)
A large-scale MIDI dataset repository hosted on GitHub by asigalov61 (the creator of the Los Angeles and Discover datasets). It is one of the foundational collections used in building the larger, more processed datasets. It contains a vast number of MIDI files gathered from various sources on the web.

## [GigaMIDI](https://github.com/Metacreation-Lab/GigaMIDI-Dataset)
A dataset from the Metacreation Lab at Simon Fraser University. It is a large collection of MIDI files designed to support research in music generation and MIR. The dataset is notable for its scale and its focus on providing a diverse range of multi-track, multi-instrumental music.

## [Meta](https://github.com/jeffreyjohnens/MetaMIDIDataset)
A large-scale dataset of MIDI files specifically curated for training and evaluating machine learning models for music generation. It emphasizes metadata and organization to facilitate research into meta-learning and other advanced AI techniques for music.

## [Los Angeles](https://github.com/asigalov61/Los-Angeles-MIDI-Dataset)
A foundational, comprehensive MIDI dataset by Alex Lev (asigalov61). It is a large, multi-instrumental dataset that serves as a basis for many subsequent projects (like Discover and Godzilla). It emphasizes normalization and is designed for a wide range of MIR and music AI tasks.

## [LAKH](https://colinraffel.com/projects/lmd/)
The Lakh MIDI Dataset is a well-established and widely-used collection of **over 170,000 unique MIDI files**. It is particularly famous for its alignment with the Million Song Dataset, allowing for cross-referencing of symbolic data with audio features and metadata. It's a cornerstone dataset for many MIR and generative music projects.

## [Aria](https://huggingface.co/datasets/loubb/aria-midi)
A dataset of piano MIDI files intended for symbolic music modeling. As cited in the Discover/Godzilla pages, it was presented at ICLR 2025 by Louis Bradshaw and Simon Colton. It is likely a high-quality, curated collection focused on piano music for tasks like melody generation or accompaniment.

## [PDMX](https://github.com/pnlong/PDMX)
A dataset that provides a large collection of **aligned polyphonic MIDI and lyrics**. This makes it particularly valuable for research in singing voice synthesis, lyrics-to-melody alignment, and other tasks that require a direct relationship between notes and text.

## [X MIDI](https://github.com/xmusic-project/XMIDI_Dataset)
A dataset from the XMusic project. Based on the repository name, it is likely designed for research into explainable or controllable music generation, potentially providing rich annotations or structural information alongside the MIDI data.

## [ATEPP](https://github.com/BetsyTang/ATEPP)
The Aligned Tracks with Expressive Performance (ATEPP) dataset. It focuses on **expressive piano performance**, providing MIDI data that captures the nuances of human playing, such as timing and velocity variations, which are often lost in quantized MIDI files.

## [GiantMIDI](https://github.com/bytedance/GiantMIDI-Piano)
A large-scale, high-quality piano MIDI dataset from ByteDance. It contains over **10,000 solo piano pieces** transcribed from audio recordings, covering a wide range of classical and other genres. It is a key resource for piano-related AI tasks.

## [midi classical music](https://huggingface.co/datasets/elizawhitfield/midi-classical-music)
A dataset focused on classical music MIDI files. It provides a collection suitable for training models on classical forms, composers, and styles.

## [Rock Piano](https://github.com/asigalov61/Rock-Piano-MIDI-Dataset)
A specialized dataset by asigalov61 focusing on piano performances in the rock genre. It's a valuable resource for studying and generating rock music from a keyboard-centric perspective.

## [MAESTRO](https://magenta.tensorflow.org/datasets/maestro)
The MAESTRO (MIDI and Audio Edited for Synchronous Tracks and Organization) dataset is a premier resource for piano research. It consists of over **200 hours of virtuosic piano performances**, captured via a Yamaha Disklavier, which provides **precisely aligned audio and MIDI data**. It is essential for tasks like automatic music transcription and performance analysis.

## [adl piano](https://github.com/lucasnfe/adl-piano-midi)
A dataset of piano MIDI files, likely sourced from the internet and organized for research. It provides a broad collection of piano music in a symbolic format.

## [POP909](https://github.com/music-x-lab/POP909-Dataset)
A dataset of **909 popular songs** with professional, multi-track annotations. It includes separate tracks for melody, accompaniment, and the main vocal, as well as tempo and key annotations. It is highly valuable for research in popular music structure, arrangement, and performance.

## [POP1k7](https://zenodo.org/records/13167761)
A large-scale dataset of popular music, containing over **1,700 songs** with professionally transcribed MIDI files. It likely provides rich annotations for chords, melody, and structure, serving as a significant resource for popular music analysis.

## [PiJAMA](https://zenodo.org/records/8354955)
A dataset designed for **piano jazz solo transcription and analysis**. It provides high-quality MIDI alignments of jazz piano performances, which is crucial for research into jazz harmony, improvisation, and swing feel.

## [Nottingham](https://github.com/jukedeck/nottingham-dataset)
A classic, smaller dataset of **over 1,000 British and American folk tunes**. It is often used as a benchmark for sequence modeling and melody generation due to its simple, homophonic structure and clear melodic lines.

## [ASAP](https://github.com/fosfrancesco/asap-dataset)
The Aligned Scores and Performances (ASAP) dataset. It bundles **2229 piano performances (MIDI) aligned with 284 musical scores (in symbolic format)**. This alignment is a powerful feature for studying expressive performance, score following, and music synchronization.

## [lead sheet](https://github.com/wayne391/lead-sheet-dataset)
A dataset specifically for **lead sheets**, which contain the melody, harmony (chords), and lyrics of a song. It's an important resource for research in harmonic analysis, melody-chord relationships, and automatic lead sheet generation.

## [Yin-Yang](https://github.com/keshavbhandari/yinyang)
A dataset likely focused on **cross-cultural music analysis**, possibly comparing elements of Western and Eastern (e.g., Chinese) music. The name suggests a duality, which could refer to different musical attributes or cultural origins.

## [MTC](https://www.liederenbank.nl/mtc)
The Meertens Tune Collections (MTC) is a dataset of **Dutch folk songs**. It provides a rich, curated collection of melodies with associated metadata, useful for ethnomusicological studies and folk music generation.

## [Kern Scores](https://kern.humdrum.org)
This is not a single dataset but a massive, online library of musical scores in the **Humdrum **kern format**. It contains thousands of high-quality, scholarly encoded scores, primarily of classical and early music. It is an invaluable resource for music theory and computational musicology.

## [EMOPIA](https://github.com/annahung31/EMOPIA)
A dataset of **pop piano music with emotion annotations**. It provides MIDI files of pop piano performances, each labeled with a quadrant from the arousal-valence emotion model, enabling research into emotion recognition and emotion-conditioned music generation.

## [chords melody](https://github.com/shiehn/chord-melody-dataset)
A dataset focused on the relationship between chords and melody. It provides paired data, which is ideal for training models for tasks like melody harmonization or chord-conditioned melody generation.

## [Groove](https://magenta.tensorflow.org/datasets/groove)
The Groove MIDI Dataset is a large-scale, high-quality dataset of **drum performances**. It contains over 13 hours of recorded drumming with detailed annotations, making it the go-to resource for modeling, generating, and analyzing drum patterns and "groove."

## [Expanded Groove](https://magenta.tensorflow.org/datasets/e-gmd)
An expansion of the original Groove MIDI Dataset, adding even more performances, drummers, and stylistic variety. It further solidifies the Groove dataset as the primary resource for data-driven drum research.

## [Annotated](https://huggingface.co/datasets/asigalov61/Annotated-MIDI-Dataset)
A dataset curated by asigalov61 that provides MIDI files with **added annotations**. This likely includes metadata such as key, tempo, chord progressions, or structural boundaries, making it useful for supervised learning tasks.

## [Music Text Alignment](https://github.com/shtdbb/MusicTextAlignment)
A dataset specifically created for the task of **aligning music (MIDI) with corresponding text**. This is a key resource for research in lyrics transcription, lyrics-to-audio alignment, and multimodal music understanding.

## [MidiCaps](https://github.com/AMAAI-Lab/MidiCaps)
A dataset designed to link MIDI files with **textual descriptions (captions)** . It pairs symbolic music with natural language, which is essential for developing text-to-music retrieval systems and multimodal generative models.

## [mono midi transposition](https://github.com/sebasgverde/mono-midi-transposition-dataset)
A dataset focusing on **monophonic MIDI and the task of transposition**. It can be used to train or evaluate models that can transpose melodies or monophonic lines to different keys while maintaining musicality.

## [ComMU](https://github.com/POZAlabs/ComMU-code)
A dataset for **conditional music generation**. It provides MIDI data along with a rich set of performance instructions (e.g., genre, tempo, instruments, mood), allowing for fine-grained control over the output of generative models.

## [MID FiLD](https://github.com/POZAlabs/MID-FiLD_code)
A dataset likely focused on **fine-grained music editing or inpainting**. "FiLD" could stand for Fill In the middle or a similar concept, providing data and tasks for models that can intelligently insert or replace musical sections within a piece.

## [Melody Track Identification](https://github.com/maxichu/MelodyTrackIdentification)
A dataset designed specifically for the task of **identifying which track in a multi-track MIDI file carries the main melody**. This is a crucial pre-processing step for many MIR and generative music systems.

## [SymphonyNet](https://symphonynet.github.io/)
The dataset associated with the SymphonyNet model for **symphonic music generation**. It contains a large collection of multi-instrumental, orchestral MIDI files, enabling research into large-scale, structured music generation.

## [Casio](https://github.com/nicholasopunii31/casio-music-data)
A small, specific dataset likely containing MIDI data from Casio keyboards or related to Casio's music data format. It might be useful for hardware interoperability or analyzing preset music from these devices.

## [popular hook](https://huggingface.co/datasets/NEXTLab-ZJU/popular-hook)
A dataset focused on identifying and extracting "hooks"—the catchy, memorable parts of popular songs. It provides MIDI data with annotations marking these sections, which is valuable for music information retrieval and analysis of popular music structure.

## [Pub Piano](https://huggingface.co/datasets/asigalov61/Pub-Piano-MIDI-Dataset)
A collection of piano MIDI files, likely sourced from public online repositories ("pub" as in public). It provides a broad, uncurated set of piano music for various tasks.

## [ACPAS](https://github.com/cheriell/ACPAS-dataset)
The Automated Counterpoint and Polyphonic Arrangement Synthesis dataset. It is likely designed for research into **counterpoint and polyphonic writing**, providing examples of well-formed polyphonic music for training generative models.

## [MuseSyn](https://zenodo.org/records/4527460)
A dataset likely related to **synthesizer or electronic music**. The name suggests it contains synthesized music or is designed for use with synthesizers, possibly including parameter settings alongside MIDI data.

## [SMD](https://zenodo.org/records/13753319)
The Salzburg MIDI Dataset (SMD). It is a collection of MIDI files, likely with a focus on classical music, curated by a research institution. The Zenodo link points to a specific version of this dataset.

## [DeepOrchestration](https://github.com/brianmodel/DeepOrchestration)
A dataset for the task of **orchestration**—taking a piano reduction and expanding it into a full orchestral arrangement. It likely contains pairs of piano scores and their corresponding multi-track orchestral MIDI versions.

## [midi classical music](https://huggingface.co/datasets/drengskapur/midi-classical-music)
Another classical music MIDI collection on Hugging Face. It serves as a readily accessible source of classical music in symbolic format for various machine learning and analysis projects.

## [GAPS](https://zenodo.org/records/13962272)
A dataset with the acronym "GAPS". Without further context, it is a specialized collection hosted on Zenodo, likely for a specific MIR task. The name might hint at its content, such as "Guitar and Piano Scores" or "Genre-Annotated Polyphonic Set".

## [BPSD](https://zenodo.org/records/12783403)
The Bach Piano Scores Dataset (BPSD). A specialized collection of J.S. Bach's piano works encoded in MIDI, providing a high-quality, focused resource for studying and modeling Baroque counterpoint and structure.

## [midi data](https://github.com/nightingale-ai/midi-data/)
A repository from Nightingale AI containing MIDI data. It likely serves as a resource for their internal models or as a general collection for the AI music community.

## [Personal MIDI Collection](https://github.com/Perkedel/Personal_MIDI-Collection)
A personal, hobbyist collection of MIDI files shared on GitHub. It likely contains arrangements and transcriptions gathered by the user, possibly with a focus on video game or chiptune music.

## [midi Archive](https://github.com/dirkncl/midiArchive)
A general-purpose archive of MIDI files. As a user-maintained archive, it aims to collect and preserve a wide variety of MIDI files from across the internet.

## [Moon Antonio](https://github.com/fossabot/MoonAntonio.github.io)
A GitHub repository likely containing MIDI files, possibly related to a specific project or game. "Moon Antonio" could be a username or project name.

## [Transform Music Project](https://github.com/lemduc/CSCI599-TransformMusicProject)
A project repository from a university course (CSCI599). It contains the dataset and code used for a project applying Transformers to music generation or analysis.

## [midi demo data](https://github.com/ltgcgo/midi-demo-data)
A small repository of MIDI files intended for demonstration or testing purposes, likely for software development or simple examples.

## [Music Generator](https://github.com/prnvpwr2612/Music-Generator)
A project repository for a music generation model. It likely includes a dataset of MIDI files used to train the model, along with the generation code.

## [music generation](https://github.com/JavierPalomares90/music-generation)
A repository for a music generation project. It contains the dataset and code used by the author for their work on algorithmic music composition.

## [artificial intelligence](https://github.com/luizcartolano2/mc906-artificial-intelligence)
A university course repository (MC906) that likely includes a MIDI dataset component for a project on AI and music, alongside other AI topics.

## [midi archive](https://github.com/reubenson/midi-archive)
Another general-purpose, user-maintained archive of MIDI files collected from various online sources.

## [WoWDiff](https://github.com/WowDevs/WoWDiff)
A repository likely containing MIDI files related to the **World of Warcraft** game. These are probably transcriptions of the game's soundtrack or user-created arrangements for the in-game music system.

## [dataprojects](https://github.com/tianhuil/dataprojects)
A personal repository containing various data projects, which may include a small collection of MIDI files as part of one of those projects.

## [Bread's midis](https://github.com/monsterjd95/Bread-s-midis)
A personal collection of MIDI files shared by a user named "monsterjd95". The name suggests a casual, hobbyist collection.

## [Midi Jamboree](https://github.com/JamiMyst/MidiJamboree)
A user repository that likely contains a collection of MIDI files, possibly for a game modding project or a personal music archive.

## [Midimancy Hubworld](https://github.com/salorarainriver/Midimancy-Hubworld)
A repository for a project called "Midimancy Hubworld." It likely contains the MIDI files associated with that project, which may be a game, interactive experience, or music tool.

## [Trentorial Piano](https://github.com/TrentorialPiano/TrentorialPiano)
A repository dedicated to piano MIDI files, possibly created or arranged by a user named Trentorial.

## [wild west midi 2](https://github.com/ProSkittles/wild-west-midi-2)
A GitHub repository containing a collection of MIDI files, primarily focused on **rock and alternative music** (e.g., Foo Fighters, Linkin Park, Radiohead). It appears to be a user's personal archive of song transcriptions or arrangements.

## [classical music midi](https://huggingface.co/datasets/xenon111/classical-music-midi)
A Hugging Face dataset of classical music MIDI files. The file viewer shows a list of files with classical composer-style names (e.g., "ballade2", "beethoveenrondo"), suggesting a collection of classical piano works.

## [touhou midi collection](https://github.com/AyHa1810/touhou-midi-collection)
A comprehensive, community-driven collection of MIDI files from the **TouHou Project game series and its related music**. It is meticulously organized by game era (shooters, fighting games, music CDs) and includes fan arrangements. The repository provides detailed information on the original sound hardware (Roland Sound Canvas) used by the composer ZUN, which is crucial for achieving authentic playback.

## [The Nuker Series Black MIDIs](https://archive.org/details/the-nuker-series-including-tn3)
This Internet Archive page hosts "The Nuker Series," a collection of **Black MIDI** files. Black MIDIs are characterized by an extremely high number of notes, often pushing the limits of the MIDI format.

***

# Must-have Audio-MIDI datasets

## [MusicNet](https://doi.org/10.5281/zenodo.5120004)
## [Maestro](https://magenta.tensorflow.org/datasets/maestro#dataset)
## [GuitarSet](https://guitarset.weebly.com/)
## [URMP](https://labsites.rochester.edu/air/projects/URMP.html)
## [Slakh2100](https://doi.org/10.5281/zenodo.4599666)

***

# Additional Tegridy MIDI datasets on Hugging Face

## [Project Los Angeles Hugging Face](https://huggingface.co/projectlosangeles/datasets)
## [Alex Hugging Face](https://huggingface.co/asigalov61/datasets)

***

# Curated list of GitHub repos with MIDIs

## [awesome midi repos](https://github.com/asigalov61/awesome-midi-repos)

***

# Must-have software:

## The one and only open-source MIDI editor! Its awesome :)
## [midieditor](https://github.com/markusschwenk/midieditor)

## OmniMIDI synthesizer and SF2 driver
## [OmniMIDI](https://github.com/KeppySoftware/OmniMIDI)

## Sound Font 2 banks to render MIDIs
## [soundfonts4u](https://huggingface.co/datasets/projectlosangeles/soundfonts4u)
## [Internet Archive 500 Sound Fonts Collection](https://archive.org/details/500-soundfonts-full-gm-sets)

***

# Audio separation

## [Online] [Vocal Separation](https://huggingface.co/spaces/JacobLinCool/vocal-separation)

***

# Audio captioninig

## [Online] [Music Flamingo](https://huggingface.co/spaces/nvidia/music-flamingo)
## [Online] [Sonic Verse](https://huggingface.co/spaces/amaai-lab/SonicVerse)
## [Online] [GAMA IT](https://huggingface.co/spaces/sonalkum/GAMA-IT)

***

# Audio to MIDI transcription

## [Colab] [ByteDance Solo Piano with Pedals Audio-to-MIDI Transcription](https://colab.research.google.com/github/asigalov61/tegridy-tools/blob/main/tegridy-tools/notebooks/ByteDance_Piano_Transcription.ipynb)

## [Online] [ByteDance Solo Piano with Pedals Audio-to-MIDI Transcription](https://huggingface.co/spaces/asigalov61/ByteDance-Solo-Piano-Audio-to-MIDI-Transcription)

## [Online] [YourMT3 Multi-Instrumental Audio-to-MIDI Transcription](https://huggingface.co/spaces/mimbres/YourMT3)

## [Online] [Google MT3 Multi-Instrumental Audio-to-MIDI Transcription](https://huggingface.co/spaces/Hmjz100/MT3)

## [Colab] [Google Multi-Instrumental and Solo Piano Audio-to-MIDI Transcription](https://colab.research.google.com/github/magenta/mt3/blob/main/mt3/colab/music_transcription_with_transformers.ipynb)

***

# MIDI captioning

## [Online] [MIDI Music Flamingo]([https://huggingface.co/spaces/nvidia/music-flamingo](https://huggingface.co/spaces/projectlosangeles/MIDI-music-flamingo))

***

# MIDI rendering

## [Online] [Tegridy Code Advanced MIDI Renderer](https://huggingface.co/spaces/asigalov61/Advanced-MIDI-Renderer)
## [Online[ [Audio to MIDI and Advanced Renderer](https://huggingface.co/spaces/avans06/Audio-To-MIDI-And-Advanced-Renderer)
## [GitHub] [fluidsynth](https://github.com/FluidSynth/fluidsynth)
## [GitHub] [SpessaSynth](https://github.com/spessasus/SpessaSynth)
## [GitHub] [midirenderer](https://github.com/ryzhakar/midirenderer)

***

# MIDI visualization

## [Software] [MIDITrail](https://github.com/wdmss/MIDITrail) 
## [Software] [midis2jam2](https://github.com/wyskoj/midis2jam2)
## [Software] [MIDIVisualizer](https://github.com/kosua20/MIDIVisualizer)
## [Software] [MIDIFall](https://github.com/Gawehold/MIDIFall)
## [GitHub] [euphony](https://github.com/qiao/euphony)
## [GitHub] [midi picasso](https://github.com/Elvenson/midi_picasso)

***

# MIDI identification

## [Online] [MIDI Identification](https://huggingface.co/spaces/asigalov61/MIDI-Identification)

***

# MIDI search

## [Online] [Los Angeles MIDI Dataset Search](https://huggingface.co/spaces/asigalov61/Los-Angeles-MIDI-Dataset-Search)
## [Online] [LAKH MIDI Dataset Search](https://huggingface.co/spaces/asigalov61/LAKH-MIDI-Dataset-Search)
## [Online] [Advanced MIDI Search](https://huggingface.co/spaces/asigalov61/MIDI-Search)
## [Online] [Karaoke MIDI Search](https://huggingface.co/spaces/asigalov61/Karaoke-MIDI-Search)

***

# MIDI classification

## [Online] [MIDI Genre Classifier](https://huggingface.co/spaces/asigalov61/MIDI-Genre-Classifier)
## [Online] [Ultimate MIDI Classifier](https://huggingface.co/spaces/asigalov61/Ultimate-MIDI-Classifier)
## [Online] [Advanced MIDI Classifier](https://huggingface.co/spaces/asigalov61/Advanced-MIDI-Classifier)

***

# MIDI comparison

## [Online] [Orpheus MIDI Comparator](https://huggingface.co/spaces/projectlosangeles/Orpheus-MIDI-Comparator)
## [Online] [Intelligent MIDI Comparator](https://huggingface.co/spaces/asigalov61/Intelligent-MIDI-Comparator)

***

# MIDI repair

## [Online] [MIDI Doctor](https://huggingface.co/spaces/asigalov61/MIDI-Doctor)

***

# MIDI alignment

## [Online] [MIDI Aligner](https://huggingface.co/spaces/asigalov61/MIDI-Aligner)

***

# MIDI bridging/infliling

## [Online] [Orpheus Bridge Music Transformer](https://huggingface.co/spaces/projectlosangeles/Orpheus-Bridge-Music-Transformer)
## [Online] [Oprheus Pitches Inpainter](https://huggingface.co/spaces/projectlosangeles/Orpheus-Pitches-Inpainter)

***

# MIDI mixing

## [Online] [Orpheus MIDI Loops Mixer](https://huggingface.co/spaces/projectlosangeles/Orpheus-MIDI-Loops-Mixer)
## [Online] [Orpheus MIDI Mono Melodies Mixer](https://huggingface.co/spaces/projectlosangeles/Orpheus-Mono-Melodies-Mixer)
## [Online] [MIDI Remixer](https://huggingface.co/spaces/asigalov61/MIDI-Remixer)
## [Online] [MIDI Loops Mixer](https://huggingface.co/spaces/asigalov61/MIDI-Loops-Mixer)
## [Online] [MIDI Chords Mixer](https://huggingface.co/spaces/asigalov61/MIDI-Chords-Mixer)

***

# MIDI humanization

## [Online] [Orpheus Humanizing Transformer](https://huggingface.co/spaces/projectlosangeles/Orpheus-Humanizing-Transformer)

***

# Miscellaneous MIDI applications

## [Online] [Awesome Drums Transformer](https://huggingface.co/spaces/projectlosangeles/Awesome-Drums-Transformer)
## [Online] [Godzilla Piano Chords Texturing Transformer](https://huggingface.co/spaces/projectlosangeles/Godzilla-Piano-Chords-Texturing-Transformer)
## [Online] [MIDI Melody](https://huggingface.co/spaces/asigalov61/MIDI-Melody)
## [Online] [Harmonic Melody MIDI Mixer](https://huggingface.co/spaces/asigalov61/Harmonic-Melody-MIDI-Mixer)
## [Online] [Chords Progressions Generator](https://huggingface.co/spaces/asigalov61/Chords-Progressions-Generator)
## [Online] [Melody Harmonizer Transformer](https://huggingface.co/spaces/asigalov61/Melody-Harmonizer-Transformer)
## [Online] [Mono Melodies Generator](https://huggingface.co/spaces/asigalov61/Mono-Melodies-Generator)
## [Online] [Parsons Code Melody Generator](https://huggingface.co/spaces/asigalov61/Parsons-Code-Melody-Transformer)
## [Online] [MuseCraft Chords Progressions](https://huggingface.co/spaces/projectlosangeles/MuseCraft-Chords-Progressions)
## [Online] [MuseCraft AlgoPOP](https://huggingface.co/spaces/projectlosangeles/MuseCraft-AlgoPOP)

***

# Lyrics applications

## [Online] [Lyrics Morpher](https://huggingface.co/spaces/projectlosangeles/Lyrics-Morpher)

***

### Project Los Angeles
### Tegridy Code 2026
