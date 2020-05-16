from pytube import YouTube
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import parse
import glob
from modules import youtubedownloader
from modules import getmusicdata
from modules import filelist
def init():
    while(True):
        print("1. Music Download")
        print("2. Music playlist")
        print("3. Play Music")
        sw = int(input(" >> "))
        if sw==1:
            Searchtitle = input("musicTitle: ")
            crawlingMusic = getmusicdata.crawling(Searchtitle)
            urlYoutue = 'https://www.youtube.com'+crawlingMusic
            print(urlYoutue)

            youtubedownloader.downloadYouTube(urlYoutue, './playlist')
        elif sw == 2:
            fl = filelist.fileList()
            for i in fl:
                print("> "+ i)

        elif sw == 3:
            print("3")
        else:
            print("Nop")
init()