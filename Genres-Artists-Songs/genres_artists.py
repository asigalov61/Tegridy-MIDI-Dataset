#! /usr/bin/python3

r'''############################################################################
################################################################################
#
#
#	    Genres Artists Python Module
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
            "artist": "Beyoncé",
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
            "artist": "Tiësto",
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
            "artist": "Howlin’ Wolf",
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
            "artist": "Rosalía",
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
            "artist": "Buena Vista Social Club",
            "description": "Revived Cuba's rich musical heritage with timeless acoustic ensembles that resonate worldwide."
        },
        {
            "artist": "Youssou N'Dour",
            "description": "Senegalese icon blending traditional rhythms with modern global influences."
        },
        {
            "artist": "Angélique Kidjo",
            "description": "Electrifying artist known for her eclectic fusion of diverse world music styles."
        },
        {
            "artist": "Cesária Évora",
            "description": "Known as the 'Barefoot Diva', she brought Cape Verdean morna to the international stage."
        },
        {
            "artist": "Ali Farka Touré",
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
            "artist": "The Clash",
            "description": "Blended punk with reggae, rockabilly, and dub, fearlessly tackling social issues."
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
        }
    ],
    "Alternative/Indie": [
        {
            "artist": "Radiohead",
            "description": "Known for experimental soundscapes and a constantly evolving musical style."
        },
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
        }
    ],
    "Funk": [
        {
            "artist": "James Brown",
            "description": "The 'Godfather of Funk,' acclaimed for dynamic performances and infectious grooves."
        },
        {
            "artist": "Parliament-Funkadelic",
            "description": "Led by George Clinton, they fused funk with psychedelic flair to revolutionize the genre."
        },
        {
            "artist": "Sly & the Family Stone",
            "description": "Brought a vibrant mix of funk, soul, and rock that reshaped the musical landscape."
        },
        {
            "artist": "Earth, Wind & Fire",
            "description": "Iconic for polished performances and a masterful fusion of funk, soul, and R&B."
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
            "artist": "Hans Zimmer",
            "description": "Crafts evocative film scores that have redefined modern cinematic soundscapes."
        },
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
        }
    ]
}

################################################################################
# This is the end of Genres Artists Python module
################################################################################