from pytube import YouTube
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import parse
import glob
from modules import youtubedownloader
from modules import getmusicdata

Searchtitle = input("musicTitle: ")
crawlingMusic = getmusicdata.crawling(Searchtitle)
urlYoutue = 'https://www.youtube.com'+crawlingMusic
print(urlYoutue)

youtubedownloader.downloadYouTube(urlYoutue, './playlist')