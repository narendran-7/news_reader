from bs4 import BeautifulSoup as bs
from textblob import TextBlob as tb
from gtts import gTTS
from subprocess import call

import playsound

import requests as req
import os

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import sys,time


class Tamil:
        def __init__(self,frame):
            self.label1 = Label(frame, text='LANGUAGE',fg="#d91e18",bg="#95a5a6")
            self.label1.place(x=100, y=80)
            data=("English","Russia","French", "Arab", "Korean","Japnesh","China","Spain")
            self.cb=Combobox(frame, values=data)
            self.cb.place(x=100, y=120)
            
            btn = Button(frame, text="START",bg="#95a5a6",command=self.box)
            btn.place(x=100,y=160)

        def box(self):
            if self.cb.get() == "English":
                print("--------------> ",self.cb.get())
                caller.collection(str(self.cb.get()))
            elif self.cb.get() == "Russia":
                caller.collection(str(self.cb.get()))
            elif self.cb.get() == "China":
                caller.collection(str(self.cb.get()))
            elif self.cb.get() == "Arab":
                caller.collection(str(self.cb.get()))
            elif self.cb.get() == "Hindhi":
                caller.collection(str(self.cb.get()))
            elif self.cb.get() == "Japnesh":
                caller.collection(str(self.cb.get()))
            elif self.cb.get() == "French":
                caller.collection(str(self.cb.get()))
            elif self.cb.get() == "Korean":
                caller.collection(str(self.cb.get()))
            elif self.cb.get() == "Spain":
                caller.collection(str(self.cb.get()))
        
        def HTML_Object(self,baseURL):
            url = baseURL
            agent = {
                        "UserAgent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0"
                    }
            requesting = req.get(
                                    url=url,
                                    headers=agent
                                )
            contManu = requesting.content
            soupObject = bs(contManu, 'html.parser')
            return soupObject

        def english(self):
            url = 'https://www.nytimes.com/section/us'
            resultObject = caller.HTML_Object(url)
            
            headList = []   
            print(headList)
            for tmp in resultObject.findAll("h2")[1:6]:
                headList.append(tmp.text.strip()+';')
            
            return headList    

        def russia(self):
            url = 'https://rt.rs/'
            resultObject = caller.HTML_Object(url)
            tags = { "class":"Link-root" }
            headList = []   
            print(headList)
            for tmp in resultObject.find_all("a",tags)[29:34]:
                # print("-------------> ",tmp.text.strip())
                headList.append(tmp.text.strip()+';')
            
            return headList 
         
        def arabic(self):
            tNews = 'https://aawsat.com/'
            resultObject = caller.HTML_Object(tNews)
            headList = []   
            tags = {
                        "class":"list-group-item"
                    }
            for tmp in resultObject.find_all("a",tags):
                print("----------->>>>>",tmp)
                headList.append(tmp.text.strip()+';')
            return headList

        def french(self):
            tNews = 'https://www.liberation.fr/'
            resultObject = caller.HTML_Object(tNews)
            headList = []   
            tags = {
                        "class":"color_black"
                    }
            for tmp in resultObject.find_all("a",tags)[:5]:
                print("----------->>>>>",tmp)
                headList.append(tmp.text.strip()+';')
            return headList

        def japan(self):
            url = 'https://www.asahi.com/'
            resultObject = caller.HTML_Object(url)
            print(url)
            
            headList = []   
            Tags = {
                         "class":"c-articleModule__link"
                   }
            for tmp in resultObject.find_all('a', "c-articleModule__link")[:5]:
                 headList.append(tmp.span.text.strip()+';')
            return headList 

        def korean(self):
            url = 'https://www.donga.com/'
            resultObject = caller.HTML_Object(url)
            
            tags = {"class":"tit"}
            headList = []   
            for tmp in resultObject.find_all("h3",tags)[:5]:
                 headList.append(tmp.a.text.strip()+';')
            return headList
        
        def spain(self):
            url = 'https://elpais.com/'
            resultObject = caller.HTML_Object(url)
            
            tags = {"class":"c_t"}
            headList = []   
            for tmp in resultObject.find_all("h2",tags)[:5]:
                 headList.append(tmp.a.text.strip()+';')
            return headList

        # def korean(self):
        #     url = 'https://unita.news/'
        #     resultObject = caller.HTML_Object(url)
            
        #     tags = {"class":"news-title"}
        #     headList = []   
        #     for tmp in resultObject.find_all("h3",tags)[:5]:
        #          headList.append(tmp.a.text.strip()+';')
        #     return headList

        def china(self):
            url = 'http://cn.chinadaily.com.cn/'
            resultObject = caller.HTML_Object(url)
            print(url)
            
            headList = []   
            for tmp in resultObject.find_all("h1")[:5]:
                 headList.append(tmp.a.text.strip()+';')
            return headList

        def find_shorcut_language(self):
            if self.cb.get() == "English":
                return "en"
            elif self.cb.get() == "Russia":
                return "ru"
            elif self.cb.get() == "Arab":
                return "ar"
            elif self.cb.get() == "Hindhi":
                return "hi"
            elif self.cb.get() == "Japnesh":
                return "ja"
            elif self.cb.get() == "China":
                return "zh-TW"
            elif self.cb.get() == "French":
                return "fr"
            elif self.cb.get() == "Korean":
                return "ko"
            elif self.cb.get() == "Spain":
                return "es"

        def collection(self,x):
            select = {
                  'English'  : caller.english,
                  'Arab' : caller.arabic,
                  'Japnesh': caller.japan,
                  'Russia': caller.russia,
                  "China": caller.china,
                  "French": caller.french,
                  "Korean": caller.korean,
                  "Spain": caller.spain
                  }
           
            self.rest = select[x]()
            caller.conVert()
            
        def conVert(self):
            lists = self.rest     # original string
            self.sCointain =[]   # converted string
            msource = [] 
            for tmp in lists:
                  convertion = tb(tmp)
                  self.out = convertion.translate(from_lang=caller.find_shorcut_language(),to='ta')
            print(lists)
            for tmp, tm in zip(lists,self.sCointain):
                msource.append("[+] "+tmp)
                msource.append("[-] "+tm+"\n")


            ans = ' \n'.join(msource)
            messagebox.showinfo("Title",ans)

            self.sCointain
            os.chdir(os.getcwd())
            caller.voice()
            caller.player()
                  
        def voice(self):
            lineString = '\','.join(self.sCointain)
            auGen = gTTS(lineString, lang='ta')
            auGen.save('news.mp3')
      
        def player(self):

            call("start news.mp3 ", shell=True)
      

frame = Tk()
caller = Tamil(frame)
frame.configure(bg='#95a5a6')
frame.title("Reader!")
frame.geometry("400x300+10+10")
frame.mainloop()
