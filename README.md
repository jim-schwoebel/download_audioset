# download_audioset

This repository makes it really easy to download [Audioset](https://research.google.com/audioset/), the open source library released by Google for speech object detection research. If you're looking for some models built from these folders, check out the [audioset-models](https://github.com/jim-schwoebel/audioset_models) repository.

AudioSet consists of an expanding ontology of 632 audio event classes and a collection of 2,084,320 human-labeled 10-second sound clips drawn from YouTube videos. The ontology is specified as a hierarchical graph of event categories, covering a wide range of human and animal sounds, musical instruments and genres, and common everyday environmental sounds.

![](https://media.giphy.com/media/uQdd4DEKErrlm/giphy.gif)

## Why make this repository?

When I first tried to download this dataset, I had some trouble getting the raw audio files. Google released most of the files as features that they extracted (via the AudioSet Embedding), but did not give access to raw .wav files. So, I made a script to make it easy to download this dataset locally on your computer or on a server. 

## What does this repo do?

The as_download.py script thus downloads and converts all the audio files in the AudioSet dataset from the YouTube to make it easy to do data science and modeling on this data. Specifically, it downloads the audio from the video files and clips these audio files at the designated time points and arranges all the classes into folders. 

## Downloading audio files 

Here are some quick checks 
* Make sure you have roughly 35 GB of free space on your hard disk. You'll need roughly this much space before continuing.
* This section assumes you are on a mac computer. 

If you don't have homebrew installed, type this into the terminal:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Now, type this into your terminal:
    
    cd ~ 
    git clone git@github.com:jim-schwoebel/download_audioset.git
    python3 setup.py
    python3 as_download.py 
    
After you start the script, it will take roughly 1-2 days to fully download the dataset. This is because I implemented a 5 second sleep in between requests of downloading videos to not strain Google's server. 

Note there are some cases where you cannot download the raw audio files, including:
* When a video is removed
* User account deleted
* Not available in country
* Need to sign in to view
* Video no longer exists
* Copyright takedown

## Resulting folder structure 

The result will be a folder structure like this (32,418,497,718 bytes (32.45 GB on disk)):

    Acapella
    Accelerating,revving,vroom
    Accordion
    Acousticguitar
    Afrobeat
    Airbrake
    Airconditioning
    Aircraft
    Aircraftengine
    Airhorn,truckhorn
    Alarm
    Alarmclock
    Ambientmusic
    Ambulance(siren)
    Angrymusic
    Animal
    Applause
    Arrow
    Artilleryfire
    Babbling
    Babycry,infantcry
    Babylaughter
    Backgroundmusic
    Bagpipes
    Bang
    Banjo
    Bark
    Basketballbounce
    Bassdrum
    Bassguitar
    Bathtub(fillingorwashing)
    Battlecry
    Beatboxing
    Bee,wasp,etc.
    Beep,bleep
    Bell
    Bellow
    Bellylaugh
    Bicycle
    Bicyclebell
    Bird
    Birdflight,flappingwings
    Birdvocalization,birdcall,birdsong
    Biting
    Bleat
    Blender
    Bluegrass
    Blues
    Boat,Watervehicle
    Boiling
    Boing
    Boom
    Bouncing
    Bow-wow
    Bowedstringinstrument
    Brassinstrument
    Breaking
    Breathing
    Burping,eructation
    Burst,pop
    Bus
    Busysignal
    Buzz
    Buzzer
    Cacophony
    Camera
    Canidae,dogs,wolves
    Capgun
    Car
    Caralarm
    Carnaticmusic
    Carpassingby
    Cashregister
    Cat
    Caterwaul
    Cattle,bovinae
    Caw
    Cello
    Chainsaw
    Changeringing(campanology)
    Chant
    Chatter
    Cheering
    Chewing,mastication
    Chicken,rooster
    Childrenplaying
    Childrenshouting
    Childsinging
    Childspeech,kidspeaking
    Chime
    Chink,clink
    Chirp,tweet
    Chirptone
    Choir
    Chop
    Chopping(food)
    Choruseffect
    Christianmusic
    Christmasmusic
    Chuckle,chortle
    Churchbell
    Civildefensesiren
    Clang
    Clapping
    Clarinet
    Classicalmusic
    Clatter
    Clickety-clack
    Clicking
    Clip-clop
    Clock
    Cluck
    Coin(dropping)
    Computerkeyboard
    Conversation
    Coo
    Cough
    Country
    Cowbell
    Crack
    Crackle
    Creak
    Cricket
    Croak
    Crow
    Crowd
    Crowing,cock-a-doodle-doo
    Crumpling,crinkling
    Crunch
    Crushing
    Crying,sobbing
    Cupboardopenorclose
    Cutlery,silverware
    Cymbal
    Dancemusic
    Dentaldrill,dentist'sdrill
    Dialtone
    Didgeridoo
    Ding
    Ding-dong
    Disco
    Dishes,pots,andpans
    Distortion
    Dog
    Domesticanimals,pets
    Door
    Doorbell
    Doublebass
    Draweropenorclose
    Drill
    Drip
    Drum
    Drumandbass
    Drumkit
    Drummachine
    Drumroll
    Dubstep
    Duck
    Echo
    Effectsunit
    Electricguitar
    Electricpiano
    Electricshaver,electricrazor
    Electrictoothbrush
    Electronica
    Electronicdancemusic
    Electronicmusic
    Electronicorgan
    Electronictuner
    Emergencyvehicle
    Engine
    Engineknocking
    Enginestarting
    Environmentalnoise
    Eruption
    Excitingmusic
    Explosion
    Fart
    Femalesinging
    Femalespeech,womanspeaking
    Fieldrecording
    Filing(rasp)
    Fill(withliquid)
    Fingersnapping
    Fire
    Firealarm
    Firecracker
    Fireengine,firetruck(siren)
    Fireworks
    Fixed-wingaircraft,airplane
    Flamenco
    Flap
    Flute
    Fly,housefly
    Foghorn
    Folkmusic
    Fowl
    Frenchhorn
    Frog
    Frying(food)
    Funk
    Funnymusic
    Fusillade
    Gargling
    Gasp
    Gears
    Giggle
    Glass
    Glockenspiel
    Goat
    Gobble
    Gong
    Goose
    Gospelmusic
    Groan
    Growling
    Grunge
    Grunt
    Guitar
    Gunshot,gunfire
    Gurgling
    Gush
    Hairdryer
    Hammer
    Hammondorgan
    Hands
    Happymusic
    Harmonic
    Harmonica
    Harp
    Harpsichord
    Heartmurmur
    Heartsounds,heartbeat
    Heavyengine(lowfrequency)
    Heavymetal
    Helicopter
    Hi-hat
    Hiccup
    Hiphopmusic
    Hiss
    Honk
    Hoot
    Horse
    Housemusic
    Howl
    Hubbub,speechnoise,speechbabble
    Hum
    Humming
    Icecreamtruck,icecreamvan
    Idling
    Independentmusic
    Insect
    Inside,largeroomorhall
    Inside,publicspace
    Inside,smallroom
    Jackhammer
    Jazz
    Jetengine
    Jingle,tinkle
    Jingle(music)
    Jinglebell
    Keyboard(musical)
    Keysjangling
    Knock
    Laughter
    Lawnmower
    Lightengine(highfrequency)
    Liquid
    Livestock,farmanimals,workinganimals
    Lullaby
    Machinegun
    Mainshum
    Malesinging
    Malespeech,manspeaking
    Malletpercussion
    Mandolin
    Mantra
    Maraca
    Marimba,xylophone
    Mechanicalfan
    Mechanisms
    Mediumengine(midfrequency)
    Meow
    Microwaveoven
    MiddleEasternmusic
    Moo
    Mosquito
    Motorboat,speedboat
    Motorcycle
    Motorvehicle(road)
    Mouse
    Music
    Musicalinstrument
    Musicforchildren
    MusicofAfrica
    MusicofAsia
    MusicofBollywood
    MusicofLatinAmerica
    Narration,monologue
    Neigh,whinny
    New-agemusic
    Noise
    Ocean
    Oink
    Opera
    Orchestra
    Organ
    Outside,ruralornatural
    Outside,urbanormanmade
    Owl
    Pant
    Patter
    Percussion
    Piano
    Pig
    Pigeon,dove
    Ping
    Pinknoise
    Pizzicato
    Plop
    Pluckedstringinstrument
    Policecar(siren)
    Popmusic
    Pour
    Powertool
    Powerwindows,electricwindows
    Printer
    Progressiverock
    Propeller,airscrew
    Psychedelicrock
    Pulleys
    Pulse
    Pump(liquid)
    Punkrock
    Purr
    Quack
    Racecar,autoracing
    Radio
    Railroadcar,trainwagon
    Railtransport
    Rain
    Raindrop
    Rainonsurface
    Rapping
    Ratchet,pawl
    Rattle
    Rattle(instrument)
    Reggae
    Reverberation
    Reversingbeeps
    Rhythmandblues
    Rimshot
    Ringtone
    Roar
    Roaringcats(lions,tigers)
    Rockandroll
    Rockmusic
    Rodents,rats,mice
    Roll
    Rowboat,canoe,kayak
    Rub
    Rumble
    Run
    Rustle
    Rustlingleaves
    Sadmusic
    Sailboat,sailingship
    Salsamusic
    Sampler
    Sanding
    Sawing
    Saxophone
    Scarymusic
    Scissors
    Scrape
    Scratch
    Scratching(performancetechnique)
    Screaming
    Sewingmachine
    Shatter
    Sheep
    Ship
    Shofar
    Shout
    Shuffle
    Shufflingcards
    Sidetone
    Sigh
    Silence
    Sinewave
    Singing
    Singingbowl
    Single-lensreflexcamera
    Sink(fillingorwashing)
    Siren
    Sitar
    Sizzle
    Ska
    Skateboard
    Skidding
    Slam
    Slap,smack
    Slidingdoor
    Slosh
    Smash,crash
    Smokedetector,smokealarm
    Snake
    Snaredrum
    Sneeze
    Snicker
    Sniff
    Snoring
    Snort
    Sonar
    Song
    Soulmusic
    Soundeffect
    Soundtrackmusic
    Speech
    Speechsynthesizer
    Splash,splatter
    Splinter
    Spray
    Squawk
    Squeak
    Squeal
    Squish
    Static
    Steam
    Steamwhistle
    Steelguitar,slideguitar
    Steelpan
    Stir
    Stomachrumble
    Stream
    Stringsection
    Strum
    Subway,metro,underground
    Swingmusic
    Synthesizer
    Syntheticsinging
    Tabla
    Tambourine
    Tap
    Tapping(guitartechnique)
    Tearing
    Techno
    Telephone
    Telephonebellringing
    Telephonedialing,DTMF
    Television
    Tendermusic
    Thememusic
    Theremin
    Throatclearing
    Throbbing
    Thump,thud
    Thunder
    Thunderstorm
    Thunk
    Tick
    Tick-tock
    Timpani
    Tiresqueal
    Toiletflush
    Tools
    Toot
    Toothbrush
    Traditionalmusic
    Trafficnoise,roadwaynoise
    Train
    Trainhorn
    Trainwheelssquealing
    Trainwhistle
    Trancemusic
    Trickle,dribble
    Trombone
    Truck
    Trumpet
    Tubularbells
    Tuningfork
    Turkey
    Typewriter
    Typing
    Ukulele
    Vacuumcleaner
    Vehicle
    Vehiclehorn,carhorn,honking
    Vibraphone
    Vibration
    Videogamemusic
    Violin,fiddle
    Vocalmusic
    Wail,moan
    Walk,footsteps
    Water
    Waterfall
    Watertap,faucet
    Waves,surf
    Weddingmusic
    Whack,thwack
    Whalevocalization
    Wheeze
    Whimper
    Whimper(dog)
    Whip
    Whir
    Whispering
    Whistle
    Whistling
    Whitenoise
    Whoop
    Whoosh,swoosh,swish
    Wildanimals
    Wind
    Windchime
    Windinstrument,woodwindinstrument
    Windnoise(microphone)
    Wood
    Woodblock
    Writing
    Yell
    Yip
    Yodeling
    Zing
    Zipper(clothing)
    Zither

## Feedback
Any feedback on the book or this repository is greatly appreciated. 
* If you find something that is missing or doesn't work, please consider opening a [GitHub issue](https://github.com/jim-schwoebel/download_audioset/issues).
* If you'd like to be mentored by someone on our team, check out the [Innovation Fellows Program](http://neurolex.ai/research).
* If you want to talk to me directly, please send me an email @ js@neurolex.co. 

## License
This repository is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). 

## References 
* [Audioset](https://research.google.com/audioset/)
