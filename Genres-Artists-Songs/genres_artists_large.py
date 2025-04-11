#! /usr/bin/python3

r'''############################################################################
################################################################################
#
#
#	    Genres Artists Large Python Module
#	    Version 1.0
#
#	    Project Los Angeles
#
#	    Tegridy Code 2025
#
#       https://github.com/asigalov61/Tegridy-MIDI-Dataset
#
#
################################################################################
#
#       Copyright 2025 Project Los Angeles / Tegridy Code
#
#       Licensed under the Apache License, Version 2.0 (the "License");
#       you may not use this file except in compliance with the License.
#       You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
#       Unless required by applicable law or agreed to in writing, software
#       distributed under the License is distributed on an "AS IS" BASIS,
#       WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#       See the License for the specific language governing permissions and
#       limitations under the License.
#
################################################################################
'''

music_genres = {
    
    "Pop": [
        {
            "artist": "Taylor Swift",
            "description": "Known for her masterful storytelling and continual reinvention."
        },
        {
            "artist": "Ariana Grande",
            "description": "Features powerhouse vocals and versatile pop anthems."
        },
        {
            "artist": "Billie Eilish",
            "description": "Offers an innovative sound with moody production."
        },
        {
            "artist": "Michael Jackson",
            "description": "Revolutionized pop with iconic dance moves and timeless hits."
        },
        {
            "artist": "Madonna",
            "description": "The 'Queen of Pop' whose bold reinventions made her a global icon."
        },
        {
            "artist": "Ed Sheeran",
            "description": "Renowned singer-songwriter celebrated for heartfelt lyrics and melodic hooks."
        },
        {
            "artist": "Justin Bieber",
            "description": "Rose to global fame with a blend of pop and R&B influences."
        },
        {
            "artist": "Lady Gaga",
            "description": "Known for theatrical performances and artistic reinventions that redefine pop."
        },
        {
            "artist": "Rihanna",
            "description": "Combines edgy style with a versatile vocal delivery that crosses genres."
        },
        {
            "artist": "Katy Perry",
            "description": "Famous for catchy anthems and vibrant visuals that capture modern pop energy."
        },
        {
            "artist": "Britney Spears",
            "description": "Pop icon famous for catchy hits and stage presence."
        },
        {
            "artist": "Celine Dion",
            "description": "Powerhouse vocalist with emotive pop ballads."
        },
        {
            "artist": "Spice Girls",
            "description": "1990s girl group symbolizing 'Girl Power' and pop anthems."
        },
        {
            "artist": "Abba",
            "description": "Swedish pop legends famous for their infectious melodies and harmonies."
        },
        {
            "artist": "Mariah Carey",
            "description": "Singer-songwriter with powerful vocals and timeless ballads."
        },
        {
            "artist": "Backstreet Boys",
            "description": "Popular boy band known for their harmonies and global hits."
        },
        {
            "artist": "Elton John",
            "description": "Iconic pianist and singer known for his flamboyant style and timeless melodies."
        },
        {
            "artist": "Dua Lipa",
            "description": "Disco-revival pop with modern production."
        },
        {
            "artist": "Bruno Mars",
            "description": "Retro-inspired pop, funk, and R&B showman."
        },
        {
            "artist": "Shawn Mendes",
            "description": "Soft-pop heartthrob with guitar-driven hits."
        },
        {
            "artist": "Olivia Rodrigo",
            "description": "Gen-Z pop-punk and balladry sensation."
        },
        {
            "artist": "Harry Styles",
            "description": "Ex-One Direction member turned eclectic pop-rock star."
        },
        {
            "artist": "Doja Cat",
            "description": "Playful pop-rap with viral appeal."
        },
        {
            "artist": "The Weeknd",
            "description": "Moody pop-R&B with cinematic themes."
        },
        {
            "artist": "Miley Cyrus",
            "description": "Genre-shifting pop and rock rebel."
        }
    ],
    "Rock": [
        {
            "artist": "The Beatles",
            "description": "Groundbreaking songwriting and studio experimentation that revolutionized rock music."
        },
        {
            "artist": "Led Zeppelin",
            "description": "Famed for massive guitar riffs and dynamic live performances that set the stage for hard rock."
        },
        {
            "artist": "Queen",
            "description": "Combines theatrical flair with versatility, creating an enduring legacy in rock."
        },
        {
            "artist": "The Rolling Stones",
            "description": "Rock and roll royalty known for timeless hits and energetic performances."
        },
        {
            "artist": "Nirvana",
            "description": "Defined grunge with raw energy and lasting influence on alternative rock."
        },
        {
            "artist": "Pink Floyd",
            "description": "Pioneers of progressive and psychedelic rock, celebrated for concept albums and immersive soundscapes."
        },
        {
            "artist": "The Who",
            "description": "Renowned for explosive live performances and innovative rock operas."
        },
        {
            "artist": "AC/DC",
            "description": "Iconic for high-energy riffs and a no-frills approach to hard rock."
        },
        {
            "artist": "Jimi Hendrix",
            "description": "Revolutionary guitarist whose innovative techniques redefined electric guitar music."
        },
        {
            "artist": "Foo Fighters",
            "description": "Modern rock stalwarts known for dynamic energy and anthemic, guitar-driven sound."
        },
        {
            "artist": "Elvis Presley",
            "description": "The 'King of Rock and Roll,' pioneer of rock music."
        },
        {
            "artist": "Rolling Stones",
            "description": "Influential rock band with blues-inspired sound."
        },
        {
            "artist": "U2",
            "description": "Irish rock band known for anthemic songs and activism."
        },
        {
            "artist": "Guns N Roses",
            "description": "Hard rock band with gritty, rebellious anthems."
        },
        {
            "artist": "Red Hot Chili Peppers",
            "description": "Funk-rock band known for their dynamic live performances."
        },
        {
            "artist": "Aerosmith",
            "description": "Blues-inspired rock band with iconic riffs and powerful vocals."
        },
        {
            "artist": "Genesis",
            "description": "Prog-rock pioneers with epic storytelling and innovative compositions."
        },
        {
            "artist": "Bon Jovi",
            "description": "Arena rock masters known for their sing-along anthems."
        },
        {
            "artist": "Fleetwood Mac",
            "description": "Blended rock and folk into one of the most influential sounds in history."
        },
        {
            "artist": "Bruce Springsteen",
            "description": "Heartland rock poet of working-class America."
        },
        {
            "artist": "David Bowie",
            "description": "Chameleonic rock icon embracing personas."
        },
        {
            "artist": "The Doors",
            "description": "Psychedelic rock with poetic mystique."
        },
        {
            "artist": "The Clash",
            "description": "Punk-rock rebels with reggae and politics."
        },
        {
            "artist": "Radiohead",
            "description": "Alternative rock innovators."
        }
    ],
    "Hip-Hop/Rap": [
        {
            "artist": "Kendrick Lamar",
            "description": "Noted for complex lyricism, incisive social commentary, and transformative storytelling."
        },
        {
            "artist": "J. Cole",
            "description": "Praised for introspective lyricism and narratives that resonate with many."
        },
        {
            "artist": "Drake",
            "description": "Dominates the charts by blending hip-hop with melodic R&B influences."
        },
        {
            "artist": "Eminem",
            "description": "A lyrical powerhouse with rapid-fire delivery and emotional intensity."
        },
        {
            "artist": "Jay-Z",
            "description": "A mogul in rap, merging business acumen with influential artistry."
        },
        {
            "artist": "Nas",
            "description": "Esteemed for vivid storytelling and a profound impact on hip-hop culture."
        },
        {
            "artist": "Tupac Shakur",
            "description": "An iconic figure whose passionate lyricism and social commentary left an indelible legacy."
        },
        {
            "artist": "The Notorious B.I.G.",
            "description": "Renowned for smooth flow and compelling narratives, emblematic of East Coast rap."
        },
        {
            "artist": "Snoop Dogg",
            "description": "Laid-back flow and charismatic delivery made him a symbol of West Coast hip-hop."
        },
        {
            "artist": "Lil Wayne",
            "description": "A prolific wordsmith known for inventive wordplay and influential style."
        },
        {
            "artist": "Run-D.M.C.",
            "description": "Pioneers of hip-hop who blended rap and rock to define a genre."
        },
        {
            "artist": "Kanye West",
            "description": "Controversial production savant."
        },
        {
            "artist": "OutKast",
            "description": "Southern rap eccentrics."
        },
        {
            "artist": "Missy Elliott",
            "description": "Futuristic rap pioneer."
        }
    ],
    "R&B/Soul": [
        {
            "artist": "Aretha Franklin",
            "description": "The 'Queen of Soul' with impassioned vocals and timeless anthems."
        },
        {
            "artist": "Marvin Gaye",
            "description": "Known for smooth, soulful melodies paired with messages that resonate."
        },
        {
            "artist": "Beyonc\u00e9",
            "description": "Modern icon celebrated for vocal prowess, dynamic performances, and innovative production."
        },
        {
            "artist": "Stevie Wonder",
            "description": "Masters soulful rhythms with intricate musicality and a legacy across decades."
        },
        {
            "artist": "Prince",
            "description": "Blended rock, funk, and R&B into a unique style, captivating audiences with his versatility."
        },
        {
            "artist": "Whitney Houston",
            "description": "A powerhouse vocalist whose emotive delivery redefined soulful ballads."
        },
        {
            "artist": "Otis Redding",
            "description": "An iconic soul singer whose heartfelt performances paved the way for future artists."
        },
        {
            "artist": "Al Green",
            "description": "Renowned for a smooth, sultry voice that revolutionized modern soul music."
        },
        {
            "artist": "Sam Cooke",
            "description": "A pioneering figure with a smooth vocal style that remains timeless in soul."
        },
        {
            "artist": "Luther Vandross",
            "description": "Celebrated for his silky voice and the ability to convey deep emotional narratives."
        },
        {
            "artist": "James Brown",
            "description": "Godfather of soul and funk."
        },
        {
            "artist": "Earth, Wind & Fire",
            "description": "Cosmic funk-disco."
        },
        {
            "artist": "Curtis Mayfield",
            "description": "Civil rights soul poet."
        },
        {
            "artist": "Chaka Khan",
            "description": "Queen of funk-soul."
        },
        {
            "artist": "Barry White",
            "description": "Velvet-voiced love man."
        },
        {
            "artist": "Sly & The Family Stone",
            "description": "Psychedelic funk collective."
        },
        {
            "artist": "Tina Turner",
            "description": "Soul-rock dynamo."
        },
        {
            "artist": "Lionel Richie",
            "description": "Smoky ballad soul."
        }
    ],
    "Electronic/Dance": [
        {
            "artist": "Daft Punk",
            "description": "Pioneered electronic dance with a distinctive blend of house and funk."
        },
        {
            "artist": "Calvin Harris",
            "description": "Crafts infectious club-ready hits and collaborates with many top pop icons."
        },
        {
            "artist": "Avicii",
            "description": "Known for uplifting melodies and bridging the gap between electronic and mainstream music."
        },
        {
            "artist": "Deadmau5",
            "description": "Renowned for progressive house tunes and a signature LED mouse head."
        },
        {
            "artist": "Skrillex",
            "description": "Pioneered modern dubstep with energetic drops and innovative production techniques."
        },
        {
            "artist": "Ti\u00ebsto",
            "description": "Legendary DJ and producer known for his dynamic live performances and anthemic tracks."
        },
        {
            "artist": "David Guetta",
            "description": "Blends electro house with pop sensibilities to deliver international hits."
        },
        {
            "artist": "Martin Garrix",
            "description": "A young prodigy celebrated for high-energy productions that push the boundaries of progressive house."
        },
        {
            "artist": "The Chemical Brothers",
            "description": "Masters of big beat, known for their innovative approach to electronic music."
        },
        {
            "artist": "Armin van Buuren",
            "description": "A key figure in trance music, renowned for mesmerizing DJ sets and uplifting productions."
        },
        {
            "artist": "Depeche Mode",
            "description": "Synth-pop pioneers shaping electronic music."
        },
        {
            "artist": "Pet Shop Boys",
            "description": "Dance-pop duo with witty lyricism."
        },
        {
            "artist": "Jean-Michel Jarre",
            "description": "Pioneering electronic composer known for atmospheric synth landscapes."
        },
        {
            "artist": "The Prodigy",
            "description": "Rave-era big beat anarchists."
        },
        {
            "artist": "Swedish House Mafia",
            "description": "Festival house supergroup."
        },
        {
            "artist": "deadmau5",
            "description": "Progressive house with mouse helmets."
        },
        {
            "artist": "Aphex Twin",
            "description": "IDM experimentalist."
        },
        {
            "artist": "Tiesto",
            "description": "Trance-turned-mainstream DJ."
        },
        {
            "artist": "Fatboy Slim",
            "description": "Big beat party starter."
        },
        {
            "artist": "Underworld",
            "description": "Techno-pop innovators."
        }
    ],
    "Country": [
        {
            "artist": "Luke Combs",
            "description": "A modern country star celebrated for robust storytelling and chart-topping hits."
        },
        {
            "artist": "Carrie Underwood",
            "description": "Commands attention with powerful vocals and anthemic tunes that define modern country."
        },
        {
            "artist": "Garth Brooks",
            "description": "A trailblazer whose live shows and record-breaking albums have defined country music."
        },
        {
            "artist": "Johnny Cash",
            "description": "The iconic 'Man in Black' known for his deep voice and enduring storytelling."
        },
        {
            "artist": "Dolly Parton",
            "description": "Beloved for her distinctive voice, songwriting prowess, and crossover appeal."
        },
        {
            "artist": "George Strait",
            "description": "Known as the 'King of Country', his traditional style and timeless hits set the industry standard."
        },
        {
            "artist": "Kenny Chesney",
            "description": "Celebrated for his breezy, laid-back style that embodies the spirit of island country."
        },
        {
            "artist": "Shania Twain",
            "description": "A crossover superstar whose blend of pop and country reshaped the genre for modern audiences."
        },
        {
            "artist": "Tim McGraw",
            "description": "Renowned for his charismatic stage presence and heartfelt country ballads."
        },
        {
            "artist": "Miranda Lambert",
            "description": "A fierce and authentic voice in country music known for raw, honest lyrical storytelling."
        },
        {
            "artist": "Alan Jackson",
            "description": "Traditional country storytelling."
        },
        {
            "artist": "Brooks Garth",
            "description": "90s country megastar with honky-tonk flair."
        },
        {
            "artist": "Willie Nelson",
            "description": "Outlaw country icon."
        },
        {
            "artist": "Kenny Rogers",
            "description": "Storytelling gambler."
        },
        {
            "artist": "Chris Stapleton",
            "description": "Soulful country powerhouse."
        }
    ],
    "Classical": [
        {
            "artist": "Wolfgang Amadeus Mozart",
            "description": "A prolific genius whose compositions continue to enchant millions."
        },
        {
            "artist": "Ludwig van Beethoven",
            "description": "Famed for dramatic symphonies that bridge classical precision with Romantic expression."
        },
        {
            "artist": "Johann Sebastian Bach",
            "description": "Renowned for intricate counterpoint and timeless musical compositions."
        },
        {
            "artist": "Franz Schubert",
            "description": "Celebrated for lyrical symphonies and influential lieder that move audiences."
        },
        {
            "artist": "Pyotr Ilyich Tchaikovsky",
            "description": "Famous for evocative ballets and sweeping symphonic works that stir deep emotions."
        },
        {
            "artist": "Franz Liszt",
            "description": "A virtuoso pianist and composer, renowned for groundbreaking technical prowess and dramatic pieces."
        },
        {
            "artist": "Antonio Vivaldi",
            "description": "His concertos, most notably 'The Four Seasons', continue to captivate classical audiences worldwide."
        },
        {
            "artist": "Igor Stravinsky",
            "description": "Revolutionized classical music with innovative rhythms and daring orchestral techniques."
        },
        {
            "artist": "Richard Wagner",
            "description": "Known for his epic operas and complex leitmotifs that transformed operatic drama."
        },
        {
            "artist": "Claude Debussy",
            "description": "Pioneered musical impressionism with innovative harmonies that evoke rich, evocative imagery."
        },
        {
            "artist": "Fr\u00e9d\u00e9ric Chopin",
            "description": "Virtuoso pianist and composer known for his expressive and intricate works."
        },
        {
            "artist": "Isaac Alb\u00e9niz",
            "description": "Spanish composer and virtuoso pianist known for his nationalist works, including 'Iberia'."
        },
        {
            "artist": "Mily Balakirev",
            "description": "Russian composer and pianist, a key figure in the Russian Five, known for 'Islamey'."
        },
        {
            "artist": "Alexander Borodin",
            "description": "Russian Romantic composer known for his symphonies and the opera 'Prince Igor'."
        },
        {
            "artist": "Johannes Brahms",
            "description": "Romantic-era composer known for his symphonies, concertos, and 'Hungarian Dances'."
        },
        {
            "artist": "Friedrich Burgm\u00fcller",
            "description": "German composer renowned for his elegant and expressive piano \u00e9tudes."
        },
        {
            "artist": "Christmas Music",
            "description": "Traditional and classical works associated with holiday celebrations, including hymns and carols."
        },
        {
            "artist": "Muzio Clementi",
            "description": "Italian composer and pianist, influential in developing piano technique and compositions."
        },
        {
            "artist": "Mikhail Glinka",
            "description": "The father of Russian classical music, known for his operas and nationalist works."
        },
        {
            "artist": "Leopold Godowsky",
            "description": "Renowned pianist and composer known for complex piano transcriptions and \u00e9tudes."
        },
        {
            "artist": "Enrique Granados",
            "description": "Spanish composer known for his expressive piano music, especially 'Goyescas'."
        },
        {
            "artist": "Edvard Grieg",
            "description": "Norwegian composer famed for 'Peer Gynt' and his nationalist influences."
        },
        {
            "artist": "Joseph Haydn",
            "description": "A father of the symphony and string quartet, a crucial figure in Classical music."
        },
        {
            "artist": "Felix Mendelssohn",
            "description": "German composer known for 'Songs Without Words' and 'A Midsummer Night\u2019s Dream'."
        },
        {
            "artist": "Moritz Moszkowski",
            "description": "German composer and pianist, admired for his lyrical and technical piano compositions."
        },
        {
            "artist": "Modest Mussorgsky",
            "description": "Russian composer known for 'Pictures at an Exhibition' and dramatic orchestral works."
        },
        {
            "artist": "Sergei Prokofiev",
            "description": "20th-century Russian composer famous for 'Peter and the Wolf' and innovative orchestration."
        },
        {
            "artist": "Sergei Rachmaninoff",
            "description": "Russian pianist and composer known for expansive, emotive works like his piano concertos."
        },
        {
            "artist": "Maurice Ravel",
            "description": "French composer renowned for 'Bol\u00e9ro' and exquisite orchestral textures."
        },
        {
            "artist": "Robert Schumann",
            "description": "German composer famous for his lyrical piano works and orchestral pieces."
        },
        {
            "artist": "Alexander Scriabin",
            "description": "Russian composer known for innovative harmonies and mystical musical concepts."
        },
        {
            "artist": "Christian Sinding",
            "description": "Norwegian composer of piano and orchestral music with Romantic influences."
        },
        {
            "artist": "Philip Glass",
            "description": "Minimalist pioneer."
        },
        {
            "artist": "Hans Zimmer",
            "description": "Film score titan."
        },
        {
            "artist": "Yo-Yo Ma",
            "description": "Cellist bridging genres."
        }
    ],
    "Jazz": [
        {
            "artist": "Miles Davis",
            "description": "A transformative innovator who redefined jazz with modal experimentation."
        },
        {
            "artist": "John Coltrane",
            "description": "Celebrated for virtuosic improvisations and soulful explorations on the saxophone."
        },
        {
            "artist": "Louis Armstrong",
            "description": "A foundational figure whose trumpet brilliance and charismatic vocals popularized jazz worldwide."
        },
        {
            "artist": "Duke Ellington",
            "description": "A pioneer of big band jazz, known for sophisticated compositions and timeless arrangements."
        },
        {
            "artist": "Charlie Parker",
            "description": "An emblematic bebop musician whose innovative improvisation set new standards in jazz."
        },
        {
            "artist": "Dizzy Gillespie",
            "description": "A bebop trailblazer renowned for virtuosic trumpet playing and complex, infectious rhythms."
        },
        {
            "artist": "Thelonious Monk",
            "description": "Innovative pianist celebrated for his idiosyncratic improvisations and distinctive compositional style."
        },
        {
            "artist": "Billie Holiday",
            "description": "Her emotive vocal delivery and personal phrasing left an indelible mark on jazz singing."
        },
        {
            "artist": "Ella Fitzgerald",
            "description": "The 'First Lady of Song', celebrated for her impeccable scat singing and crystal-clear tone."
        },
        {
            "artist": "Sarah Vaughan",
            "description": "Distinguished by her rich tone and remarkable technique, influencing generations of vocalists."
        },
        {
            "artist": "Frank Sinatra",
            "description": "Swing-era icon with timeless vocal jazz."
        },
        {
            "artist": "Dave Brubeck",
            "description": "Cool jazz innovator."
        },
        {
            "artist": "Herbie Hancock",
            "description": "Fusion keyboard pioneer."
        },
        {
            "artist": "Wynton Marsalis",
            "description": "Neo-traditional trumpet virtuoso."
        },
        {
            "artist": "Kamasi Washington",
            "description": "Modern jazz epic storyteller."
        }
    ],
    "Blues": [
        {
            "artist": "B.B. King",
            "description": "The 'King of the Blues,' celebrated for expressive guitar work and soulful vocal delivery."
        },
        {
            "artist": "Muddy Waters",
            "description": "A pioneering force who electrified the blues and inspired countless rock musicians."
        },
        {
            "artist": "Etta James",
            "description": "Merged blues, soul, and rock with a powerhouse voice that still resonates today."
        },
        {
            "artist": "Robert Johnson",
            "description": "A Delta blues legend whose haunting recordings have become the stuff of lore."
        },
        {
            "artist": "Buddy Guy",
            "description": "An iconic guitarist known for bridging traditional blues and modern rock influences."
        },
        {
            "artist": "Howlin\u2019 Wolf",
            "description": "Noted for his deep, gravelly vocals and commanding stage presence that defined raw blues."
        },
        {
            "artist": "John Lee Hooker",
            "description": "Renowned for his rhythmic guitar style and soulful, introspective vocals."
        },
        {
            "artist": "T-Bone Walker",
            "description": "A guitar virtuoso credited with shaping the sound of electric blues."
        },
        {
            "artist": "Elmore James",
            "description": "Known for his slide guitar mastery and influential approach to blues phrasing."
        },
        {
            "artist": "Otis Rush",
            "description": "A key architect of the Chicago blues sound with passionate and expressive guitar work."
        },
        {
            "artist": "Eric Clapton",
            "description": "Legendary guitarist blending blues, rock, and soul."
        }
    ],
    "Reggae": [
        {
            "artist": "Bob Marley",
            "description": "The global ambassador of reggae, celebrated for his messages of peace, love, and unity."
        },
        {
            "artist": "Peter Tosh",
            "description": "A leading figure in reggae noted for vibrant rhythms and politically charged lyrics."
        },
        {
            "artist": "Bunny Wailer",
            "description": "A founding member of The Wailers, recognized for soulful, roots-driven contributions."
        },
        {
            "artist": "Jimmy Cliff",
            "description": "Blended reggae with soulful storytelling, garnering international acclaim."
        },
        {
            "artist": "Dennis Brown",
            "description": "Often called the 'Crown Prince of Reggae' for his smooth vocal style and influential work."
        },
        {
            "artist": "Toots and the Maytals",
            "description": "Pioneers who infused ska and reggae with infectious energy and unparalleled rhythm."
        },
        {
            "artist": "Burning Spear",
            "description": "Known for deep, spiritual lyrics and an impassioned commitment to Rastafarian ideals."
        },
        {
            "artist": "Gregory Isaacs",
            "description": "Celebrated for his smooth, velvety voice that earned him the title 'Cool Ruler' of reggae."
        },
        {
            "artist": "Ziggy Marley",
            "description": "Carrying on his father Bob Marley's legacy while blending tradition with a modern twist."
        },
        {
            "artist": "Steel Pulse",
            "description": "A roots reggae band renowned for socially conscious lyrics and dynamic live performances."
        },
        {
            "artist": "UB40",
            "description": "British reggae band known for covers and originals."
        },
        {
            "artist": "Shaggy",
            "description": "Dancehall-pop crossover."
        },
        {
            "artist": "Sean Paul",
            "description": "Dancehall hitmaker."
        },
        {
            "artist": "Damian Marley",
            "description": "Bob's son, blending reggae and hip-hop."
        },
        {
            "artist": "Sizzla",
            "description": "Conscious dancehall firebrand."
        },
        {
            "artist": "Chronixx",
            "description": "Modern roots revivalist."
        }
    ],
    "Metal": [
        {
            "artist": "Black Sabbath",
            "description": "Pioneers of heavy metal, whose dark riffs set the foundation for the genre."
        },
        {
            "artist": "Metallica",
            "description": "Renowned for their aggressive sound and technical proficiency that redefined metal."
        },
        {
            "artist": "Iron Maiden",
            "description": "Celebrated for epic compositions and high-energy performances that have inspired millions."
        },
        {
            "artist": "Slayer",
            "description": "Notable for their intense, thrash metal style that pushed the boundaries of the genre."
        },
        {
            "artist": "Megadeth",
            "description": "Recognized for intricate guitar work and innovative, boundary-pushing metal compositions."
        },
        {
            "artist": "Pantera",
            "description": "Known for a groove metal style that blends ferocious riffs with dynamic vocal delivery."
        },
        {
            "artist": "Judas Priest",
            "description": "Renowned for dual-guitar onslaughts and a signature look that epitomized metal."
        },
        {
            "artist": "Anthrax",
            "description": "A seminal thrash band celebrated for fusing aggression with witty lyricism."
        },
        {
            "artist": "Slipknot",
            "description": "Famous for their intense live shows, theatrical masks, and a fusion of nu-metal elements."
        },
        {
            "artist": "Sepultura",
            "description": "A Brazilian metal band celebrated for merging thrash, death, and tribal influences."
        },
        {
            "artist": "Tool",
            "description": "Progressive metal with polyrhythms."
        },
        {
            "artist": "Motorhead",
            "description": "Speed metal ancestors."
        },
        {
            "artist": "Opeth",
            "description": "Death-prog fusion."
        },
        {
            "artist": "Gojira",
            "description": "Eco-conscious tech-death."
        },
        {
            "artist": "Mastodon",
            "description": "Sludge metal storytellers."
        }
    ],
    "Folk": [
        {
            "artist": "Bob Dylan",
            "description": "A seminal figure whose poetic lyrics redefined folk music and ignited social change."
        },
        {
            "artist": "Woody Guthrie",
            "description": "An influential folk icon known for grassroots storytelling and protest songs."
        },
        {
            "artist": "Joan Baez",
            "description": "Praised for her clear voice and activism that brought folk music to the cultural forefront."
        },
        {
            "artist": "Simon & Garfunkel",
            "description": "Renowned for harmonious melodies and introspective lyrics that defined 60s folk."
        },
        {
            "artist": "Pete Seeger",
            "description": "A legendary folk musician and activist whose music championed social justice."
        },
        {
            "artist": "Cat Stevens",
            "description": "Beloved for reflective songwriting and gentle acoustics that have become timeless."
        },
        {
            "artist": "Joni Mitchell",
            "description": "A visionary lyricist whose poetic imagery and innovative compositions redefined folk."
        },
        {
            "artist": "Neil Young",
            "description": "A prolific artist whose raw, emotional blending of folk and rock epitomizes authenticity."
        },
        {
            "artist": "Nick Drake",
            "description": "Known for introspective, melancholic tunes and delicate acoustic mastery."
        },
        {
            "artist": "Leonard Cohen",
            "description": "Celebrated for his deep, resonant voice and literary songwriting transcending folk boundaries."
        },
        {
            "artist": "Traditional",
            "description": "Rooted in cultural heritage and oral traditions."
        },
        {
            "artist": "Israel Folk",
            "description": "Folk music reflecting Israeli history."
        }
    ],
    "Latin": [
        {
            "artist": "Bad Bunny",
            "description": "A modern sensation transforming Latin music with a fusion of reggaeton and trap."
        },
        {
            "artist": "Shakira",
            "description": "Blends Latin pop with rock and global sounds to captivate diverse audiences."
        },
        {
            "artist": "J Balvin",
            "description": "A leader in reggaeton, known for catchy rhythms and modern urban flair."
        },
        {
            "artist": "Juanes",
            "description": "Merges rock with Latin rhythms and meaningful lyrics, impacting Latin music worldwide."
        },
        {
            "artist": "Rosal\u00eda",
            "description": "Innovative artist merging flamenco traditions with contemporary urban sounds."
        },
        {
            "artist": "Enrique Iglesias",
            "description": "A global pop icon celebrated for romantic ballads and infectious dance tracks."
        },
        {
            "artist": "Luis Fonsi",
            "description": "Gained worldwide fame with passionate performances blending Latin rhythms and pop."
        },
        {
            "artist": "Maluma",
            "description": "A versatile artist whose reggaeton and Latin pop fusion has propelled him into international stardom."
        },
        {
            "artist": "Pitbull",
            "description": "Infuses high-energy rap with Latin rhythms, creating party anthems that command global dance floors."
        },
        {
            "artist": "Selena",
            "description": "Forever cherished for her vibrant voice and cultural impact, she remains an enduring Latin icon."
        },
        {
            "artist": "Santana",
            "description": "Fusion of rock, Latin rhythms, and blues."
        },
        {
            "artist": "Gloria Estefan",
            "description": "Queen of Latin pop and crossover hits."
        },
        {
            "artist": "Ricky Martin",
            "description": "Global Latin pop sensation."
        },
        {
            "artist": "Carlos Santana",
            "description": "Fusion artist blending Latin rhythms with rock guitar wizardry."
        },
        {
            "artist": "Marc Anthony",
            "description": "Salsa rom\u00e1ntica king."
        },
        {
            "artist": "Celia Cruz",
            "description": "Queen of salsa."
        },
        {
            "artist": "Buena Vista Social Club",
            "description": "Cuban son legends."
        },
        {
            "artist": "Los Tigres del Norte",
            "description": "Norte\u00f1o storytellers."
        },
        {
            "artist": "Romeo Santos",
            "description": "Bachata heartthrob."
        }
    ],
    "Gospel": [
        {
            "artist": "Kirk Franklin",
            "description": "An innovative gospel leader who skillfully blends traditional spirituals with modern production."
        },
        {
            "artist": "CeCe Winans",
            "description": "Celebrated for her angelic voice and uplifting performances that touch the soul."
        },
        {
            "artist": "Mahalia Jackson",
            "description": "A historic figure whose soulful delivery helped define the landscape of gospel music."
        },
        {
            "artist": "Donnie McClurkin",
            "description": "Known for inspiring messages and a smooth, emotive vocal style."
        },
        {
            "artist": "Tamela Mann",
            "description": "Renowned for her powerful performances and dynamic vocal presence in gospel."
        },
        {
            "artist": "Yolanda Adams",
            "description": "Captivates with a rich tone and the ability to convey profound spiritual emotion."
        },
        {
            "artist": "The Clark Sisters",
            "description": "A pioneering gospel group celebrated for tight harmonies and dynamic live delivery."
        },
        {
            "artist": "Marvin Sapp",
            "description": "Distinguished for heartfelt sermons expressed through powerful, moving gospel music."
        },
        {
            "artist": "Smokie Norful",
            "description": "Blends rich vocal expression with modern gospel nuances, bridging tradition and innovation."
        },
        {
            "artist": "Tramaine Hawkins",
            "description": "Her soulful voice and uplifting messages have solidified her status as a gospel legend."
        },
        {
            "artist": "Hristianskaya Muzyika",
            "description": "Traditional Christian spiritual music."
        }
    ],
    "World": [
        {
            "artist": "Fela Kuti",
            "description": "Pioneered Afrobeat by fusing traditional Nigerian rhythms with elements of jazz and funk."
        },
        {
            "artist": "Ravi Shankar",
            "description": "Indian virtuoso who introduced global audiences to the sitar and classical traditions."
        },
        {
            "artist": "Youssou N'Dour",
            "description": "Senegalese icon blending traditional rhythms with modern global influences."
        },
        {
            "artist": "Ang\u00e9lique Kidjo",
            "description": "Electrifying artist known for her eclectic fusion of diverse world music styles."
        },
        {
            "artist": "Ces\u00e1ria \u00c9vora",
            "description": "Known as the 'Barefoot Diva', she brought Cape Verdean morna to the international stage."
        },
        {
            "artist": "Ali Farka Tour\u00e9",
            "description": "Blended traditional Malian music with blues, forging a bridge between continents."
        },
        {
            "artist": "Manu Dibango",
            "description": "Renowned for mixing jazz, funk, and African rhythms into a singular, infectious sound."
        },
        {
            "artist": "Tinariwen",
            "description": "A band that channels the soul of the Sahara with hypnotic desert blues and rock influences."
        },
        {
            "artist": "Miriam Makeba",
            "description": "The 'Mama Africa' whose voice and activism introduced African sounds to a global audience."
        },
        {
            "artist": "Narodnaya Muzyika",
            "description": "Russian folk and traditional music."
        },
        {
            "artist": "Chinese Folk",
            "description": "Traditional melodies from Chinese culture."
        }
    ],
    "Punk": [
        {
            "artist": "The Ramones",
            "description": "Often regarded as the godfathers of punk with straightforward, high-energy songs."
        },
        {
            "artist": "Sex Pistols",
            "description": "An explosive band whose rebellious music ignited the British punk movement."
        },
        {
            "artist": "Bad Religion",
            "description": "Known for intellectual lyrics and a distinctive edge in the hardcore punk scene."
        },
        {
            "artist": "Green Day",
            "description": "Revitalized punk for a new generation with catchy, energetic tracks and memorable anthems."
        },
        {
            "artist": "The Stooges",
            "description": "Pioneers of proto-punk whose raw energy laid the groundwork for the genre."
        },
        {
            "artist": "Black Flag",
            "description": "A hardcore punk band celebrated for its aggressive sound and DIY ethos."
        },
        {
            "artist": "The Dead Kennedys",
            "description": "Known for their satirical, provocative lyrics and relentless punk spirit."
        },
        {
            "artist": "Buzzcocks",
            "description": "Fused pop sensibilities with punk's raw energy, influencing countless future bands."
        },
        {
            "artist": "Minor Threat",
            "description": "A seminal hardcore punk band that helped define the straight-edge movement."
        },
        {
            "artist": "The Offspring",
            "description": "Melodic punk rock with rebellious energy."
        },
        {
            "artist": "NOFX",
            "description": "Fast-paced punk with satirical lyrics."
        },
        {
            "artist": "Rancid",
            "description": "Punk fused with ska and streetwise themes."
        },
        {
            "artist": "Ramones",
            "description": "Pioneers of punk rock known for their raw, high-energy sound."
        },
        {
            "artist": "Blink-182",
            "description": "Pop-punk icons blending humor and fast-paced melodies."
        },
        {
            "artist": "The Damned",
            "description": "First UK punk single."
        },
        {
            "artist": "Bad Brains",
            "description": "Hardcore punk meets reggae."
        },
        {
            "artist": "Dead Kennedys",
            "description": "Satirical punk provocateurs."
        },
        {
            "artist": "The Misfits",
            "description": "Horror-punk with B-movie flair."
        },
        {
            "artist": "X-Ray Spex",
            "description": "Feminist punk energy."
        }
    ],
    "Alternative/Indie": [
        {
            "artist": "Arctic Monkeys",
            "description": "Evolved from raw garage rock beginnings to a refined and sophisticated indie sound."
        },
        {
            "artist": "The Smiths",
            "description": "Celebrated for introspective lyrics and distinctive, jangly guitar work."
        },
        {
            "artist": "Florence + The Machine",
            "description": "Marry dramatic vocals with lush instrumentation for a unique indie experience."
        },
        {
            "artist": "Bon Iver",
            "description": "Blends indie folk with experimental production to create ethereal, atmospheric music."
        },
        {
            "artist": "The Cure",
            "description": "Iconic for their moody sound and introspective lyrics that left an indelible mark on indie music."
        },
        {
            "artist": "Pearl Jam",
            "description": "Though rooted in grunge, their emotive storytelling and alternative spirit resonate within indie circles."
        },
        {
            "artist": "Modest Mouse",
            "description": "Known for their eclectic approach and thought-provoking lyricism that defies conventions."
        },
        {
            "artist": "Vampire Weekend",
            "description": "Infuses indie rock with vibrant pop elements and clever, literate lyricism."
        },
        {
            "artist": "Tame Impala",
            "description": "Experiments with psychedelic sounds and innovative production, redefining modern indie rock."
        },
        {
            "artist": "Arcade Fire",
            "description": "Indie rock band with orchestral arrangements."
        },
        {
            "artist": "Coldplay",
            "description": "Alternative rock band known for their emotional and uplifting songs."
        },
        {
            "artist": "Muse",
            "description": "Blended rock, electronic, and classical influences into their unique sound."
        },
        {
            "artist": "Pixies",
            "description": "Indie rock pioneers blending surreal lyrics with raw, dynamic soundscapes."
        },
        {
            "artist": "The Strokes",
            "description": "2000s garage-rock revivalists."
        },
        {
            "artist": "LCD Soundsystem",
            "description": "Dance-punk intellectuals."
        },
        {
            "artist": "The National",
            "description": "Moody baritone indie."
        },
        {
            "artist": "Interpol",
            "description": "Post-punk revivalists."
        },
        {
            "artist": "Beach House",
            "description": "Dream-pop etherealism."
        },
        {
            "artist": "Sufjan Stevens",
            "description": "Orchestral indie folk."
        },
        {
            "artist": "Phoenix",
            "description": "French indie-pop sophisticates."
        }
    ],
    "New Age": [
        {
            "artist": "Enya",
            "description": "Famous for her ethereal vocals and lush, atmospheric soundscapes."
        },
        {
            "artist": "Yanni",
            "description": "Creates sweeping instrumental compositions that blend classical motifs with modern textures."
        },
        {
            "artist": "Kitaro",
            "description": "Japanese composer noted for evocative, meditative pieces and timeless soundscapes."
        },
        {
            "artist": "Vangelis",
            "description": "Renowned for innovative ambient soundtracks and iconic film scores."
        },
        {
            "artist": "Laraaji",
            "description": "A pioneer of ambient music, known for his meditative soundscapes and unique instrumentation."
        },
        {
            "artist": "George Winston",
            "description": "Celebrated for his contemplative piano pieces that evoke serene imagery."
        },
        {
            "artist": "Deuter",
            "description": "Crafts immersive ambient experiences melding nature sounds with mellow instrumentals."
        },
        {
            "artist": "Adiemus Project",
            "description": "Merges classical choral elements with modern production to create ethereal soundscapes."
        },
        {
            "artist": "Loreena McKennitt",
            "description": "Fuses Celtic traditions with world music, creating rich, mystical compositions."
        },
        {
            "artist": "Secret Garden",
            "description": "Known for ornate, minimalist compositions that evoke peaceful and introspective moods."
        },
        {
            "artist": "Jean Michel Jarre",
            "description": "Electronic pioneer creating atmospheric soundscapes."
        }
    ],
    "Funk": [
        {
            "artist": "Parliament-Funkadelic",
            "description": "Led by George Clinton, they fused funk with psychedelic flair to revolutionize the genre."
        },
        {
            "artist": "Sly & the Family Stone",
            "description": "Brought a vibrant mix of funk, soul, and rock that reshaped the musical landscape."
        },
        {
            "artist": "Rick James",
            "description": "Left a lasting impact with raw energy and a distinctive, boundary-pushing funk style."
        },
        {
            "artist": "Chic",
            "description": "Known for crisp guitar riffs and danceable grooves that bridged disco and funk."
        },
        {
            "artist": "Tower of Power",
            "description": "Celebrated for tight horn sections and energetic rhythms that define soulful funk."
        },
        {
            "artist": "Bootsy Collins",
            "description": "A transformative bassist whose quirky style and dynamic presence redefined funk."
        },
        {
            "artist": "Average White Band",
            "description": "Brought a sophisticated blend of funk and soul with an unmistakable groove."
        },
        {
            "artist": "The Meters",
            "description": "Pioneers of funk known for their rhythmic precision and foundational New Orleans sound."
        }
    ],
    "Soundtrack/Film Score": [
        {
            "artist": "John Williams",
            "description": "Renowned for timeless themes and iconic scores that shape our cinematic memories."
        },
        {
            "artist": "Ennio Morricone",
            "description": "Legendary composer whose innovative scores enriched films across countless genres."
        },
        {
            "artist": "Danny Elfman",
            "description": "Known for quirky, memorable film scores, especially in his collaborations with visionary directors."
        },
        {
            "artist": "Howard Shore",
            "description": "Celebrated for epic compositions that defined blockbuster franchises like The Lord of the Rings."
        },
        {
            "artist": "James Horner",
            "description": "Remembered for emotive, adventurous scores that vividly brought cinematic worlds to life."
        },
        {
            "artist": "Alan Silvestri",
            "description": "Crafted iconic themes that have become ingrained in popular culture."
        },
        {
            "artist": "Alexandre Desplat",
            "description": "Renowned for his versatile, innovative compositions that elevate cinematic storytelling."
        },
        {
            "artist": "Randy Newman",
            "description": "Noted for his distinctive blend of Americana and narrative-driven film music."
        },
        {
            "artist": "Carter Burwell",
            "description": "Known for subtle, evocative scoring that enhances the emotional landscape of films."
        },
        {
            "artist": "Movie Themes",
            "description": "Iconic orchestral compositions for cinema."
        },
        {
            "artist": "Video Games",
            "description": "Memorable scores from gaming soundtracks."
        }
    ],
    "K-Pop": [
        {
            "artist": "BTS",
            "description": "Global superstars blending pop, hip-hop, and EDM with Korean influences."
        },
        {
            "artist": "BLACKPINK",
            "description": "High-energy girl group with fierce performances and catchy hooks."
        },
        {
            "artist": "TWICE",
            "description": "Bubblegum pop meets infectious dance tracks."
        },
        {
            "artist": "EXO",
            "description": "SM Entertainment's vocal-dance kings."
        },
        {
            "artist": "IU",
            "description": "Soloist with angelic vocals."
        }
    ],
    "Afrobeats": [
        {
            "artist": "Burna Boy",
            "description": "Nigerian artist fusing Afrobeat, dancehall, and reggae."
        },
        {
            "artist": "Wizkid",
            "description": "Pioneer of modern Afrobeats with global crossover appeal."
        },
        {
            "artist": "Tems",
            "description": "Soulful vocals blending R&B and Afrobeat rhythms."
        },
        {
            "artist": "Davido",
            "description": "Afrobeats hit machine."
        }
    ],
    "Disco": [
        {
            "artist": "Bee Gees",
            "description": "Kings of disco with falsetto harmonies and Saturday Night Fever anthems."
        },
        {
            "artist": "ABBA",
            "description": "Swedish pop-disco legends with timeless melodies."
        },
        {
            "artist": "Donna Summer",
            "description": "Queen of disco with electrifying dancefloor hits."
        }
    ],
    "Grunge": [
        {
            "artist": "Soundgarden",
            "description": "Heavy, psychedelic-tinged grunge pioneers."
        },
        {
            "artist": "Alice in Chains",
            "description": "Dark, harmonized grunge-metal."
        },
        {
            "artist": "Stone Temple Pilots",
            "description": "90s alt-rock radio staples."
        }
    ],
    "Ska": [
        {
            "artist": "The Specials",
            "description": "British ska revivalists with social commentary."
        },
        {
            "artist": "Madness",
            "description": "Upbeat ska-pop with a quirky British charm."
        },
        {
            "artist": "Reel Big Fish",
            "description": "Third-wave ska with humor and brass sections."
        }
    ],
    "Industrial": [
        {
            "artist": "Nine Inch Nails",
            "description": "Fusion of metal, electronic, and abrasive textures."
        },
        {
            "artist": "Marilyn Manson",
            "description": "Shock rock meets industrial theatrics."
        },
        {
            "artist": "Rammstein",
            "description": "German industrial metal with pyrotechnic spectacle."
        },
        {
            "artist": "Ministry",
            "description": "Pioneers of industrial metal."
        },
        {
            "artist": "Skinny Puppy",
            "description": "Canadian industrial innovators."
        },
        {
            "artist": "KMFDM",
            "description": "German industrial dance-rock."
        },
        {
            "artist": "Front 242",
            "description": "Belgian EBM originators."
        }
    ],
    "Bluegrass": [
        {
            "artist": "Bill Monroe",
            "description": "Father of bluegrass and mandolin virtuoso."
        },
        {
            "artist": "Alison Krauss",
            "description": "Angel-voiced fiddler bridging bluegrass and folk."
        },
        {
            "artist": "B\u00e9la Fleck",
            "description": "Banjo innovator pushing bluegrass boundaries."
        },
        {
            "artist": "Earl Scruggs",
            "description": "Banjo pioneer."
        },
        {
            "artist": "The Stanley Brothers",
            "description": "Mountain harmonies."
        }
    ],
    "Soul": [
        {
            "artist": "Adele",
            "description": "Modern soul powerhouse with heart-wrenching ballads."
        }
    ],
    "Progressive Rock": [
        {
            "artist": "Yes",
            "description": "Complex compositions and virtuosic musicianship."
        },
        {
            "artist": "King Crimson",
            "description": "Avant-garde prog-rock with dissonant brilliance."
        },
        {
            "artist": "Rush",
            "description": "Canadian power trio with sci-fi lyrics."
        },
        {
            "artist": "Emerson, Lake & Palmer",
            "description": "Classical-meets-rock virtuosity."
        }
    ],
    "Experimental": [
        {
            "artist": "Bj\u00f6rk",
            "description": "Icelandic avant-pop artist defying genre conventions."
        }
    ],
    "House": [
        {
            "artist": "Frankie Knuckles",
            "description": "Godfather of house music and Chicago club culture."
        },
        {
            "artist": "Disclosure",
            "description": "Modern house-pop with UK garage influences."
        }
    ],
    "Trap": [
        {
            "artist": "Travis Scott",
            "description": "Psychedelic trap with cinematic production."
        },
        {
            "artist": "Migos",
            "description": "Pioneered triplet flows and modern trap aesthetics."
        },
        {
            "artist": "Future",
            "description": "Auto-tuned melancholic trap anthems."
        }
    ],
    "Ambient": [
        {
            "artist": "Brian Eno",
            "description": "Father of ambient music and atmospheric soundscapes."
        },
        {
            "artist": "Sigur R\u00f3s",
            "description": "Ethereal post-rock with Icelandic falsetto."
        },
        {
            "artist": "Stars of the Lid",
            "description": "Drone-heavy ambient for deep meditation."
        }
    ]
}

################################################################################
# This is the end of Genres Artists Large Python module
################################################################################