from pytube import YouTube
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import parse
import glob

def crawling(searchT):
    print("Crawling Proceeding..")
    crawlingMusic = str()
    searchT = searchT.strip()
    url = 'https://www.youtube.com/results?search_query='+parse.quote(searchT)
    i = 0
    with urlopen(url) as response:
        soup = BeautifulSoup(response, 'html.parser')
        musicInfo = soup.find('a', class_='yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link')
        crawlingMusic = musicInfo.get('href','/')
    print('Successful processing.')
    return crawlingMusic