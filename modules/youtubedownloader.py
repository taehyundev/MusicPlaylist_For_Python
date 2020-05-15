from pytube import YouTube
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import parse
import glob

def downloadYouTube(videourl, path):
    print("Youtube Music Downloading..")
    yt = YouTube(videourl)
    if not os.path.exists(path):
        os.makedirs(path)
    yt.streams.filter(only_audio=True).first().download(path)

    files = glob.glob(path+"/*.mp4")
   # print('a')
    for c in files:
        filename = os.path.splitext(c)[0]
        os.rename(c,filename + '.mp3')
    
    print("Successful processing!!")
