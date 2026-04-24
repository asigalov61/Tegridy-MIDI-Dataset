#! /usr/bin/python3

r'''############################################################################
################################################################################
#
#
#	    Top Genres Artists Songs Python Module
#	    Version 1.0
#
#	    Project Los Angeles
#
#	    Tegridy Code 2026
#
#       https://github.com/asigalov61/Tegridy-MIDI-Dataset
#
#
################################################################################
#
#       Copyright 2026 Project Los Angeles / Tegridy Code
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

top_genres_artists_songs = {
    "Classic Rock": {
        "The Beatles": ["Hey Jude", "Let It Be", "Come Together", "Yesterday"],
        "Elvis Presley": ["Jailhouse Rock", "Can't Help Falling in Love", "Suspicious Minds", "Hound Dog"],
        "U2": ["With or Without You", "One", "Beautiful Day", "Sunday Bloody Sunday"],
        "The Beach Boys": ["God Only Knows", "Good Vibrations", "Kokomo", "Surfin' U.S.A."],
        "The Rolling Stones": ["(I Can't Get No) Satisfaction", "Paint It Black", "Sympathy for the Devil", "Gimme Shelter"],
        "Bon Jovi": ["Livin' on a Prayer", "You Give Love a Bad Name", "It's My Life", "Wanted Dead or Alive"],
        "Oasis": ["Wonderwall", "Don't Look Back in Anger", "Champagne Supernova", "Some Might Say"],
        "Deep Purple": ["Smoke on the Water", "Highway Star", "Perfect Strangers", "Burn"],
        "Toto": ["Africa", "Rosanna", "Hold the Line", "I'll Be Over You"],
        "Fleetwood Mac": ["Dreams", "The Chain", "Go Your Own Way", "Everywhere"],
        "The Police": ["Every Breath You Take", "Roxanne", "Message in a Bottle", "Don't Stand So Close to Me"],
        "David Bowie": ["Space Oddity", "Heroes", "Ziggy Stardust", "Let's Dance"],
        "Roy Orbison": ["Pretty Woman", "Crying", "Only the Lonely", "In Dreams"],
        "Rod Stewart": ["Maggie May", "Da Ya Think I'm Sexy?", "Sailing", "Have I Told You Lately"],
        "Queen": ["Bohemian Rhapsody", "We Will Rock You", "Don't Stop Me Now", "Somebody to Love"],
        "Bee Gees": ["Stayin' Alive", "How Deep Is Your Love", "Night Fever", "To Love Somebody"],
        "The Kinks": ["Lola", "Waterloo Sunset", "All Day and All of the Night", "You Really Got Me"],
        "Eric Clapton": ["Tears in Heaven", "Layla", "Wonderful Tonight", "Cocaine"],
        "Electric Light Orchestra": ["Mr. Blue Sky", "Don't Bring Me Down", "Livin' Thing", "Sweet Talkin' Woman"],
        "Kiss": ["Rock and Roll All Nite", "I Was Made for Lovin' You", "Detroit Rock City", "Beth"],
        "Lynyrd Skynyrd": ["Sweet Home Alabama", "Free Bird", "Simple Man", "Tuesday's Gone"],
        "Ac-Dc": ["Back in Black", "Highway to Hell", "Thunderstruck", "You Shook Me All Night Long"],
        "Billy Joel": ["Piano Man", "Uptown Girl", "Just the Way You Are", "We Didn't Start the Fire"],
        "Aerosmith": ["I Don't Want to Miss a Thing", "Dream On", "Sweet Emotion", "Walk This Way"],
        "Santana": ["Smooth", "Maria Maria", "Oye Como Va", "Black Magic Woman"],
        "Dire Straits": ["Sultans of Swing", "Money for Nothing", "Brothers in Arms", "Walk of Life"],
        "Led Zeppelin": ["Stairway to Heaven", "Whole Lotta Love", "Immigrant Song", "Kashmir"],
        "George Harrison": ["My Sweet Lord", "Here Comes the Sun", "While My Guitar Gently Weeps", "Got My Mind Set on You"],
        "Kansas": ["Dust in the Wind", "Carry On Wayward Son", "Point of Know Return", "Wayward Son"],
        "Foreigner": ["I Want to Know What Love Is", "Juke Box Hero", "Hot Blooded", "Cold as Ice"],
        "Def Leppard": ["Pour Some Sugar on Me", "Photograph", "Love Bites", "Animal"],
        "Van Halen": ["Jump", "Eruption", "Panama", "Hot for Teacher"],
        "Creedence Clearwater Revival": ["Fortunate Son", "Have You Ever Seen the Rain?", "Proud Mary", "Bad Moon Rising"],
        "The Everly Brothers": ["All I Have to Do Is Dream", "Wake Up Little Susie", "Cathy's Clown", "Bye Bye Love"],
        "Gary Moore": ["Parisienne Walkways", "Still Got the Blues", "Over the Hills and Far Away", "Empty Rooms"],
        "Bryan Adams": ["Summer of '69", "(Everything I Do) I Do It for You", "Heaven", "Run to You"],
        "Extreme": ["More Than Words", "Hole Hearted", "Get the Funk Out", "Decadence Dance"],
        "Paul Mccartney": ["Maybe I'm Amazed", "Band on the Run", "Live and Let Die", "Silly Love Songs"],
        "Chuck Berry": ["Johnny B. Goode", "Roll Over Beethoven", "Maybellene", "Rock and Roll Music"],
        "America": ["A Horse with No Name", "Sister Golden Hair", "Ventura Highway", "Tin Man"],
        "Simon & Garfunkel": ["The Sound of Silence", "Mrs. Robinson", "Bridge over Troubled Water", "Cecilia"],
        "Joe Cocker": ["With a Little Help from My Friends", "You Are So Beautiful", "Unchain My Heart", "Up Where We Belong"],
        "Lenny Kravitz": ["Are You Gonna Go My Way", "Fly Away", "American Woman", "It Ain't Over 'til It's Over"]
    },
    "Pop": {
        "Madonna": ["Like a Prayer", "Material Girl", "Vogue", "Hung Up"],
        "Mariah Carey": ["Fantasy", "We Belong Together", "Hero", "All I Want for Christmas Is You"],
        "Michael Jackson": ["Billie Jean", "Thriller", "Beat It", "Smooth Criminal"],
        "Taylor Swift": ["Love Story", "Shake It Off", "Blank Space", "Anti-Hero"],
        "Maroon 5": ["Sugar", "Moves Like Jagger", "This Love", "Memories"],
        "Prince": ["Purple Rain", "When Doves Cry", "Kiss", "1999"],
        "Elton John": ["Rocket Man", "Your Song", "Tiny Dancer", "Crocodile Rock"],
        "Lady Gaga": ["Bad Romance", "Poker Face", "Shallow", "Born This Way"],
        "Britney Spears": ["...Baby One More Time", "Toxic", "Oops!... I Did It Again", "Circus"],
        "Robbie Williams": ["Angels", "Rock DJ", "Feel", "Millennium"],
        "Avril Lavigne": ["Complicated", "Sk8er Boi", "I'm with You", "Girlfriend"],
        "Ed Sheeran": ["Shape of You", "Perfect", "Thinking Out Loud", "Photograph"],
        "Whitney Houston": ["I Will Always Love You", "I Wanna Dance with Somebody", "Greatest Love of All", "How Will I Know"],
        "Abba": ["Dancing Queen", "Mamma Mia", "Waterloo", "Gimme! Gimme! Gimme!"],
        "The Corrs": ["Breathless", "Runaway", "What Can I Do", "So Young"],
        "Katy Perry": ["Firework", "Roar", "Teenage Dream", "Dark Horse"],
        "Twenty One Pilots": ["Stressed Out", "Heathens", "Ride", "Blurryface"],
        "Tina Turner": ["What's Love Got to Do with It", "Proud Mary", "Simply the Best", "Private Dancer"],
        "Barry Manilow": ["Mandy", "Copacabana (At the Copa)", "I Write the Songs", "Can't Smile Without You"],
        "Backstreet Boys": ["I Want It That Way", "Everybody (Backstreet's Back)", "As Long as You Love Me", "Larger Than Life"],
        "Justin Bieber": ["Baby", "Sorry", "Love Yourself", "Peaches"],
        "Kate Bush": ["Running Up That Hill", "Wuthering Heights", "Hounds of Love", "Babooshka"],
        "Rihanna": ["Umbrella", "Diamonds", "We Found Love", "Work"],
        "The Weeknd": ["Blinding Lights", "Can't Feel My Face", "Starboy", "The Hills"],
        "Roxette": ["Listen to Your Heart", "It Must Have Been Love", "The Look", "Joyride"],
        "Sting": ["Fields of Gold", "Englishman in New York", "Shape of My Heart", "If I Ever Lose My Faith in You"],
        "Ariana Grande": ["Thank U, Next", "7 Rings", "Problem", "Into You"],
        "Miley Cyrus": ["Wrecking Ball", "Party in the U.S.A.", "Flowers", "We Can't Stop"],
        "Jewel": ["Who Will Save Your Soul", "You Were Meant for Me", "Foolish Games", "Hands"],
        "Christina Aguilera": ["Genie in a Bottle", "Beautiful", "Fighter", "Dirrty"],
        "Adele": ["Rolling in the Deep", "Someone Like You", "Hello", "Set Fire to the Rain"],
        "Diana Ross": ["Ain't No Mountain High Enough", "I'm Coming Out", "Upside Down", "Endless Love"],
        "Kelly Clarkson": ["Since U Been Gone", "Because of You", "Stronger (What Doesn't Kill You)", "Breakaway"],
        "Boney M.": ["Rasputin", "Daddy Cool", "Ma Baker", "Nightflight to Venus"],
        "Enrique Iglesias": ["Hero", "Bailando", "Escape", "I Like It"],
        "Barbra Streisand": ["Woman in Love", "The Way We Were", "Evergreen", "People"],
        "Kylie Minogue": ["Can't Get You out of My Head", "Locomotion", "Spinning Around", "I Should Be So Lucky"],
        "Bread": ["Make It with You", "Everything I Own", "Baby I'm-A Want You", "If"],
        "Carpenters": ["Close to You", "Yesterday Once More", "Top of the World", "We've Only Just Begun"],
        "Michael Bolton": ["When a Man Loves a Woman", "How Am I Supposed to Live Without You", "Said I Loved You... But I Lied", "Time, Love and Tenderness"],
        "Engelbert Humperdinck": ["Release Me", "The Last Waltz", "A Man Without Love", "Quando Quando Quando"],
        "George Michael": ["Careless Whisper", "Faith", "Freedom! '90", "Last Christmas"],
        "Bruno Mars": ["Just the Way You Are", "Uptown Funk", "Grenade", "24K Magic"],
        "Dua Lipa": ["Levitating", "Don't Start Now", "New Rules", "Dance the Night"],
        "Take That": ["Back for Good", "Relight My Fire", "Pray", "Patience"],
        "Anastacia": ["I'm Outta Love", "Left Outside Alone", "Paid My Dues", "One Day in Your Life"],
        "Aqua": ["Barbie Girl", "Doctor Jones", "My Oh My", "Roses Are Red"],
        "Donna Summer": ["Hot Stuff", "I Feel Love", "Last Dance", "Bad Girls"],
        "Mika": ["Grace Kelly", "Love Today", "Happy Ending", "Relax, Take It Easy"],
        "Olivia Newton-John": ["Physical", "Hopelessly Devoted to You", "You're the One That I Want", "Summer Nights"],
        "James Blunt": ["You're Beautiful", "Goodbye My Lover", "1973", "Bonfire Heart"],
        "Sarah Mclachlan": ["Angel", "Building a Mystery", "Adia", "Possession"],
        "Modern Talking": ["You're My Heart, You're My Soul", "Cheri Cheri Lady", "Brother Louie", "You Can Win If You Want"],
        "Sia": ["Chandelier", "Cheap Thrills", "Elastic Heart", "The Greatest"],
        "Ellie Goulding": ["Lights", "Love Me Like You Do", "Burn", "Anything Could Happen"],
        "Air Supply": ["Making Love Out of Nothing at All", "Lost in Love", "All Out of Love", "Even the Nights Are Better"],
        "Meghan Trainor": ["All About That Bass", "Lips Are Movin", "Dear Future Husband", "Like I'm Gonna Lose You"],
        "Lana Del Rey": ["Summertime Sadness", "Born to Die", "Young and Beautiful", "Video Games"],
        "Olly Murs": ["Dance with Me Tonight", "Heart Skips a Beat", "Troublemaker", "Dear Darlin'"],
        "Norah Jones": ["Don't Know Why", "Come Away with Me", "Sunrise", "Turn Me On"],
        "Billie Eilish": ["Bad Guy", "Happier Than Ever", "Therefore I Am", "Everything I Wanted"],
        "Neil Diamond": ["Sweet Caroline", "Cracklin' Rosie", "Song Sung Blue", "America"],
        "Frank Sinatra": ["My Way", "Fly Me to the Moon", "New York, New York", "Strangers in the Night"],
        "Simply Red": ["Stars", "If You Don't Know Me by Now", "Fairground", "Holding Back the Years"],
        "Level 42": ["Lessons in Love", "Something About You", "Running in the Family", "The Sun Goes Down"],
        "Sparks": ["This Town Ain't Big Enough for the Both of Us", "Amateur Hour", "The Number One Song in Heaven", "When I'm with You"],
        "Gloria Estefan": ["Conga", "Rhythm Is Gonna Get You", "Anything for You", "Get on Your Feet"]
    },
    "Alternative Rock": {
        "Red Hot Chili Peppers": ["Californication", "Under the Bridge", "Snow (Hey Oh)", "Otherside"],
        "Muse": ["Supermassive Black Hole", "Uprising", "Knights of Cydonia", "Hysteria"],
        "Linkin Park": ["In the End", "Numb", "Crawling", "Breaking the Habit"],
        "Incubus": ["Drive", "Wish You Were Here", "Pardon Me", "Megalomaniac"],
        "Radiohead": ["Creep", "Karma Police", "No Surprises", "Fake Plastic Trees"],
        "Coldplay": ["Yellow", "The Scientist", "Fix You", "Viva la Vida"],
        "Nirvana": ["Smells Like Teen Spirit", "Come as You Are", "Lithium", "Heart-Shaped Box"],
        "R.E.M.": ["Losing My Religion", "Everybody Hurts", "It's the End of the World as We Know It", "Man on the Moon"],
        "They Might Be Giants": ["Birdhouse in Your Soul", "Boss of Me", "Istanbul (Not Constantinople)", "Don't Let's Start"],
        "Smashing Pumpkins": ["1979", "Today", "Bullet with Butterfly Wings", "Disarm"],
        "Soundgarden": ["Black Hole Sun", "Spoonman", "Outshined", "Rusty Cage"],
        "Foo Fighters": ["Everlong", "The Pretender", "Best of You", "My Hero"],
        "Live": ["Lightning Crashes", "I Alone", "All Over You", "Selling the Drama"],
        "Weezer": ["Buddy Holly", "Island in the Sun", "Say It Ain't So", "Beverly Hills"],
        "The Cranberries": ["Zombie", "Linger", "Dreams", "Ode to My Family"],
        "Pearl Jam": ["Alive", "Jeremy", "Even Flow", "Black"],
        "Keane": ["Somewhere Only We Know", "Everybody's Changing", "Is It Any Wonder?", "Bend and Break"],
        "Garbage": ["Stupid Girl", "Only Happy When It Rains", "I Think I'm Paranoid", "Why Do You Love Me"],
        "Staind": ["It's Been Awhile", "Outside", "So Far Away", "Right Here"],
        "Audioslave": ["Like a Stone", "Cochise", "Show Me How to Live", "Be Yourself"],
        "311": ["Amber", "Down", "All Mixed Up", "Love Song"],
        "Alice In Chains": ["Man in the Box", "Rooster", "Would?", "No Excuses"],
        "The White Stripes": ["Seven Nation Army", "Icky Thump", "Fell in Love with a Girl", "We're Going to Be Friends"],
        "Nickelback": ["How You Remind Me", "Photograph", "Rockstar", "Someday"],
        "Faith No More": ["Epic", "Midlife Crisis", "We Care a Lot", "Falling to Pieces"],
        "Alanis Morissette": ["Ironic", "You Oughta Know", "Hand in My Pocket", "Thank U"],
        "The Strokes": ["Last Nite", "Reptilia", "Someday", "Hard to Explain"],
        "Manic Street Preachers": ["A Design for Life", "If You Tolerate This", "Motorcycle Emptiness", "Everything Must Go"],
        "Snow Patrol": ["Chasing Cars", "Run", "Open Your Eyes", "Just Say Yes"],
        "Primus": ["Jerry Was a Race Car Driver", "My Name Is Mud", "Wynona's Big Brown Beaver", "Tommy the Cat"],
        "Thrice": ["The Artist in the Ambulance", "Image of the Invisible", "Red Sky", "Black Honey"],
        "The Smashing Pumpkins": ["Today", "Disarm", "Bullet with Butterfly Wings", "1979"],
        "Brand New": ["The Quiet Things That No One Ever Knows", "Sic Transit Gloria", "Jesus Christ", "Play Crack the Sky"],
        "Mumford & Sons": ["I Will Wait", "Little Lion Man", "The Wolf", "Believe"],
        "Arctic Monkeys": ["Do I Wanna Know?", "R U Mine?", "505", "I Bet You Look Good on the Dancefloor"],
        "Jack Johnson": ["Better Together", "Banana Pancakes", "Flake", "Upside Down"],
        "The Goo Goo Dolls": ["Iris", "Slide", "Black Balloon", "Name"],
        "Rem": ["Stand", "Pop Song 89", "It's the End of the World as We Know It", "The One I Love"],
        "The Smiths": ["There Is a Light That Never Goes Out", "This Charming Man", "How Soon Is Now?", "Please, Please, Please, Let Me Get What I Want"]
    },
    "Heavy Metal": {
        "Megadeth": ["Holy Wars", "Symphony of Destruction", "Hangar 18", "Trust"],
        "Iron Maiden": ["The Trooper", "Fear of the Dark", "Run to the Hills", "Number of the Beast"],
        "Slayer": ["Raining Blood", "Angel of Death", "South of Heaven", "Seasons in the Abyss"],
        "Korn": ["Freak on a Leash", "Blind", "Got the Life", "Falling Away from Me"],
        "Judas Priest": ["Breaking the Law", "Living After Midnight", "You've Got Another Thing Comin'", "Painkiller"],
        "Black Sabbath": ["Paranoid", "Iron Man", "War Pigs", "Heaven and Hell"],
        "Avenged Sevenfold": ["Hail to the King", "So Far Away", "Nightmare", "Afterlife"],
        "Deftones": ["Change (In the House of Flies)", "My Own Summer (Shove It)", "Digital Bath", "Be Quiet and Drive"],
        "Metallica": ["Enter Sandman", "Master of Puppets", "Nothing Else Matters", "One"],
        "Scorpions": ["Rock You Like a Hurricane", "Wind of Change", "Still Loving You", "No One Like You"],
        "Mudvayne": ["Dig", "Happy?", "Death Blooms", "Not Falling"],
        "System Of A Down": ["Chop Suey!", "Toxicity", "B.Y.O.B.", "Aerials"],
        "Hammerfall": ["Hearts on Fire", "Let the Hammer Fall", "Legacy of Kings", "Renegade"],
        "Nightwish": ["Nemo", "Amaranth", "Wish I Had an Angel", "Ghost Love Score"],
        "Disturbed": ["Down with the Sickness", "The Sound of Silence", "Stricken", "Indestructible"],
        "Helloween": ["I Want Out", "Eagle Fly Free", "Future World", "Dr. Stein"],
        "Marilyn Manson": ["The Beautiful People", "Sweet Dreams (Are Made of This)", "Personal Jesus", "This Is the New Shit"],
        "Slipknot": ["Psychosocial", "Duality", "Wait and Bleed", "Spit It Out"],
        "Manowar": ["Warriors of the World United", "Hail and Kill", "Kings of Metal", "Battle Hymns"],
        "Sabaton": ["Ghost Division", "The Price of a Mile", "To Hell and Back", "Primo Victoria"],
        "Death": ["Zombie Ritual", "Pull the Plug", "Symbolic", "Flattening of Emotions"],
        "Blind Guardian": ["Mirror Mirror", "And Then There Was Silence", "The Bard's Song", "Battlefield"],
        "In Flames": ["Only for the Weak", "Take This Life", "The Jester Race", "Clayman"],
        "Alice Cooper": ["Poison", "School's Out", "No More Mr. Nice Guy", "Feed My Frankenstein"],
        "Godsmack": ["I Stand Alone", "Voodoo", "Straight Out of Line", "Awake"],
        "Anthrax": ["Indians", "Madhouse", "Bring the Noise", "Among the Living"],
        "Therion": ["To Mega Therion", "Ginnungagap", "Son of the Sun", "Lemuria"],
        "Kreator": ["Pleasure to Kill", "Enemy of God", "Phantom Antichrist", "Extreme Aggression"],
        "Meshuggah": ["Bleed", "New Millennium Cyanide Christ", "Rational Gaze", "I"],
        "Children Of Bodom": ["Hatecrew Deathroll", "Everytime I Die", "Are You Dead Yet?", "Needled 24/7"],
        "Annihilator": ["Alice in Hell", "King of the Kill", "Human Insecticide", "Alison Hell"],
        "Opeth": ["Blackwater Park", "The Drapery Falls", "Harvest", "Deliverance"],
        "Hatebreed": ["I Will Be Heard", "Perseverance", "Live for This", "Destroy Everything"],
        "Sonata Arctica": ["FullMoon", "Wolf & Raven", "Paid in Full", "Don't Say a Word"],
        "Limp Bizkit": ["Break Stuff", "Nookie", "Rollin' (Air Raid Vehicle)", "My Way"],
        "Angra": ["Carry On", "Nova Era", "Angels Cry", "Spread Your Fire"],
        "Pantera": ["Cowboys from Hell", "Walk", "Cemetery Gates", "This Love"]
    },
    "Progressive Rock": {
        "Rush": ["Tom Sawyer", "Limelight", "Closer to the Heart", "The Spirit of Radio"],
        "Genesis": ["Invisible Touch", "Land of Confusion", "I Can't Dance", "That's All"],
        "Pink Floyd": ["Comfortably Numb", "Wish You Were Here", "Money", "Time"],
        "Peter Gabriel": ["Sledgehammer", "In Your Eyes", "Big Time", "Don't Give Up"],
        "Porcupine Tree": ["Trains", "Lazarus", "Blackest Eyes", "Anesthetize"],
        "Dream Theater": ["Pull Me Under", "Metropolis Part 1", "Octavarium", "Panic Attack"],
        "Supertramp": ["Breakfast in America", "The Logical Song", "Goodbye Stranger", "Take the Long Way Home"],
        "Marillion": ["Kayleigh", "Lavender", "Incommunicado", "Script for a Jester's Tear"],
        "Jethro Tull": ["Aqualung", "Living in the Past", "Locomotive Breath", "Bungle in the Jungle"],
        "The Moody Blues": ["Nights in White Satin", "Tuesday Afternoon", "Question", "Ride My See-Saw"],
        "Anathema": ["Deep", "Untouchable, Part 1", "Judgement", "A Natural Disaster"]
    },
    "Country": {
        "George Strait": ["Amarillo by Morning", "All My Ex's Live in Texas", "Check Yes or No", "Carrying Your Love with Me"],
        "Carrie Underwood": ["Before He Cheats", "Jesus, Take the Wheel", "Something in the Water", "Blown Away"],
        "Shania Twain": ["Man! I Feel Like a Woman!", "You're Still the One", "That Don't Impress Me Much", "Any Man of Mine"],
        "Merle Haggard": ["Mama Tried", "Okie from Muskogee", "The Fightin' Side of Me", "Sing Me Back Home"],
        "Alabama": ["Mountain Music", "Dixieland Delight", "Song of the South", "Love in the First Degree"],
        "Patsy Cline": ["Crazy", "I Fall to Pieces", "Walkin' After Midnight", "Sweet Dreams"],
        "Willie Nelson": ["On the Road Again", "Blue Eyes Crying in the Rain", "Always on My Mind", "Mammas Don't Let Your Babies Grow Up to Be Cowboys"],
        "Alan Jackson": ["Chattahoochee", "Remember When", "Good Time", "Where Were You (When the World Stopped Turning)"],
        "Don Williams": ["Tulsa Time", "Lord, I Hope This Day Is Good", "I Believe in You", "You're My Best Friend"],
        "John Denver": ["Take Me Home, Country Roads", "Annie's Song", "Leaving on a Jet Plane", "Rocky Mountain High"],
        "Tim Mcgraw": ["Live Like You Were Dying", "Humble and Kind", "Something Like That", "Don't Take the Girl"],
        "Toby Keith": ["Courtesy of the Red, White and Blue", "Should've Been a Cowboy", "As Good as I Once Was", "How Do You Like Me Now?!"],
        "Kenny Rogers": ["The Gambler", "Islands in the Stream", "Lucille", "Coward of the County"],
        "Hank Williams": ["I'm So Lonesome I Could Cry", "Your Cheatin' Heart", "Hey, Good Lookin'", "Jambalaya (On the Bayou)"],
        "Brooks & Dunn": ["Boot Scootin' Boogie", "Neon Moon", "My Maria", "Red Dirt Road"],
        "Brad Paisley": ["Whiskey Lullaby", "She's Everything", "Ticks", "Water"],
        "Johnny Cash": ["Ring of Fire", "Hurt", "Folsom Prison Blues", "Walk the Line"],
        "Jimmy Buffett": ["Margaritaville", "Cheeseburger in Paradise", "Come Monday", "Changes in Latitudes"],
        "George Jones": ["He Stopped Loving Her Today", "The Grand Tour", "Walk Through This World with Me", "White Lightning"]
    },
    "Hip Hop": {
        "Eminem": ["Lose Yourself", "Stan", "The Real Slim Shady", "Without Me"],
        "Kanye West": ["Stronger", "Gold Digger", "Power", "Touch the Sky"],
        "Drake": ["Hotline Bling", "God's Plan", "One Dance", "In My Feelings"]
    },
    "Punk Rock": {
        "Green Day": ["Basket Case", "Boulevard of Broken Dreams", "American Idiot", "Holiday"],
        "Blink 182": ["All the Small Things", "What's My Age Again?", "Adam's Song", "Dammit"],
        "Bad Religion": ["Infected", "21st Century (Digital Boy)", "American Jesus", "Sorrow"],
        "Fall Out Boy": ["Sugar, We're Goin Down", "Centuries", "Thnks fr th Mmrs", "Dance, Dance"],
        "The Offspring": ["Pretty Fly (For a White Guy)", "Self Esteem", "The Kids Aren't Alright", "You're Gonna Go Far, Kid"],
        "Nofx": ["Linoleum", "Don't Call Me White", "The Brews", "Bob"],
        "Ramones": ["Blitzkrieg Bop", "I Wanna Be Sedated", "Sheena Is a Punk Rocker", "Beat on the Brat"],
        "Blink-182": ["I Miss You", "Feeling This", "The Rock Show", "First Date"],
        "Millencolin": ["No Cigar", "Kemp", "Punk Rock Rebel", "Fox"],
        "Simple Plan": ["I'm Just a Kid", "Welcome to My Life", "Perfect", "Addicted"],
        "New Found Glory": ["My Friends Over You", "Head on Collision", "Hit or Miss", "All Downhill from Here"],
        "Alkaline Trio": ["Stupid Kid", "Radio", "Private Eye", "We've Had Enough"],
        "Misfits": ["Last Caress", "Skulls", "Die, Die My Darling", "Hybrid Moments"]
    },
    "New Wave": {
        "Blondie": ["Heart of Glass", "Call Me", "One Way or Another", "Rapture"],
        "A-Ha": ["Take On Me", "The Sun Always Shines on T.V.", "Hunting High and Low", "Cry Wolf"],
        "Simple Minds": ["Don't You (Forget About Me)", "Alive and Kicking", "Belfast Child", "Waterfront"],
        "Duran Duran": ["Hungry Like the Wolf", "Rio", "Ordinary World", "Come Undone"],
        "The Cure": ["Just Like Heaven", "Boys Don't Cry", "Friday I'm in Love", "Lovesong"],
        "Madness": ["Our House", "It Must Be Love", "Baggy Trousers", "My Girl"],
        "Devo": ["Whip It", "Jocko Homo", "Freedom of Choice", "Uncontrollable Urge"],
        "The Stranglers": ["Golden Brown", "No More Heroes", "Peaches", "Always the Sun"]
    },
    "Electronic": {
        "Depeche Mode": ["Enjoy the Silence", "Just Can't Get Enough", "Personal Jesus", "Never Let Me Down Again"],
        "Avicii": ["Wake Me Up", "Levels", "Hey Brother", "Waiting for Love"],
        "David Guetta": ["Titanium", "Without You", "When Love Takes Over", "Sexy Bitch"],
        "New Order": ["Blue Monday", "Bizarre Love Triangle", "True Faith", "Regret"],
        "Nine Inch Nails": ["Hurt", "Closer", "Head Like a Hole", "March of the Pigs"]
    },
    "R&B/Soul": {
        "Stevie Wonder": ["Superstition", "Isn't She Lovely", "I Just Called to Say I Love You", "Sir Duke"],
        "Aretha Franklin": ["Respect", "Natural Woman", "Think", "Chain of Fools"],
        "The Temptations": ["My Girl", "Just My Imagination", "Papa Was a Rollin' Stone", "Ain't Too Proud to Beg"],
        "Alicia Keys": ["Fallin'", "No One", "If I Ain't Got You", "Girl on Fire"],
        "Lionel Richie": ["Hello", "All Night Long", "Endless Love", "Say You, Say Me"],
        "Otis Redding": ["Try a Little Tenderness", "(Sittin' On) The Dock of the Bay", "Hard to Handle", "I've Been Loving You Too Long"],
        "Ray Charles": ["Hit the Road Jack", "Georgia on My Mind", "I Got a Woman", "What'd I Say"]
    },
    "Reggae": {
        "Bob Marley": ["No Woman, No Cry", "Three Little Birds", "Redemption Song", "One Love"],
        "Ub40": ["Red Red Wine", "Can't Help Falling in Love", "Kingston Town", "I Got You Babe"]
    },
    "Soundtrack/Musical": {
        "Andrew Lloyd Webber": ["The Phantom of the Opera", "Memory", "Don't Cry for Me Argentina", "Jesus Christ Superstar"]
    }
}

################################################################################
# This is the end of Top Genres Artists Songs Python module
################################################################################