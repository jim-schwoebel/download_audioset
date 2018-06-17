# download_audioset

This repository makes it really easy to download [Audioset](https://research.google.com/audioset/), the opensource library released by google for speech object detection research. AudioSet consists of an expanding ontology of 632 audio event classes and a collection of 2,084,320 human-labeled 10-second sound clips drawn from YouTube videos. The ontology is specified as a hierarchical graph of event categories, covering a wide range of human and animal sounds, musical instruments and genres, and common everyday environmental sounds.

## why make this repository?

When I first tried to download this dataset, I had some troubles because the classes all had odd .csv labels. I also needed to clip the actual audio to the proper lengths if I were to download the videos off of youtube. So, I made a script to make it easy to download this dataset locally on your computer or on a server. 

## what does this repo do?

The as_download.py script thus downloads all the audio files from the [audioset dataset](https://research.google.com/audioset/) to make it easy to do data science and modeling on this data. Specifically, it downloads the audio from the video files and clips these audio files at the designated time points and arranges all the classes into folders. 

# quick checks

Make sure you have roughly 30 GB of free space on your hard disk. You'll need roughly this much space before continuing.

# how to do this 

This assumes you are on a mac computer. 

If you don't have homebrew installed, type this into the terminal:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Now, type this into your terminal:
    
    cd ~ 
    git clone git@github.com:jim-schwoebel/download_audioset.git
    python3 setup.py
    python3 as_download.py 
    
# references 
* [Audioset](https://research.google.com/audioset/)
