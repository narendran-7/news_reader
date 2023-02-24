import requests as req
from bs4 import BeautifulSoup as bs
from subprocess import call

# call("start news.mp3 ", shell=True)

url = "https://unita.news/"
agent = {
            "UserAgent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0"
        }
requesting = req.get(url=url,headers=agent)
contManu = requesting.content
resultObject = bs(contManu, 'html.parser')
# print(soupObject)
tags = {"class":"news-title"}
headLine = []
for t in resultObject.find_all("h3",tags)[:5] :
    print("-----> ",t.a.text.strip()+';')


# from textblob import TextBlob as tb

# convertion = tb("Biden Administration Announces New Border Crackdown;")
# out = convertion.translate(from_lang='en',to='ta')

# print("-------------> ", str(out))


# from pydub import AudioSegment
# from pydub.playback import play
# import os
# import pathlib

# ffmpeg_path = "{}\ffmpeg.exe".format(os.getcwd())
# print("-----> ffmpeg ", ffmpeg_path)
# AudioSegment.ffmpeg = ffmpeg_path
# voice_news = AudioSegment.from_mp3("t_news.mp3")
# play(voice_news)

# import vlc
# p = vlc.MediaPlayer("t_news.mp3")
# p.play()

# from pygame import mixer  # Load the popular external library

# mixer.init()
# mixer.music.load('t_news.mp3')
# mixer.music.play()
# while mixer.music.get_busy():  # wait for music to finish playing
#     time.sleep(1)

# import playsound
# playsound.playsound('t_news.mp3', True)