# download_audioset

This repository makes it really easy to download [Audioset](https://research.google.com/audioset/), the opensource library released by google for speech object detection research. AudioSet consists of an expanding ontology of 632 audio event classes and a collection of 2,084,320 human-labeled 10-second sound clips drawn from YouTube videos. The ontology is specified as a hierarchical graph of event categories, covering a wide range of human and animal sounds, musical instruments and genres, and common everyday environmental sounds.

When I first tried to download this dataset, I had some troubles because the classes all had odd .csv labels. I also needed to clip the actual audio to the proper lengths if I were to download the videos off of youtube. So, I made a script to make it easy to download this dataset locally on your computer or on a server. 

# what this script does

Downloads and clips all videos on youtube on behalf of the audioset dataset. 

# how to do this 

Type this into your terminal:

    git clone git@github.com:jim-schwoebel/download_audioset.git
    python3 as_download.py 
    
