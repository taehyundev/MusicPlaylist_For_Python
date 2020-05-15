from flask import Flask,render_template,request

from modules import youtubedownloader
from modules import getmusicdata
from modules import filelist

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('findmusic.html')

@app.route('/playlist')
def filelist():
    file_list = filelist.fileList()
    print(file_list)
    return render_template('musiclist.html')

@app.route('/data', methods =['POST'])
def data():
    result = request.form
    crawlingMusic = getmusicdata.crawling(result['music'])
    urlYoutue = 'https://www.youtube.com'+crawlingMusic
    youtubedownloader.downloadYouTube(urlYoutue, './playlist')
    return "Success"

app.run()