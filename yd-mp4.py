from __future__ import unicode_literals
import youtube_dl
from tkinter import *


root = Tk()

class Functions():
    
    
    def download(self):
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.entry.get()])
        self.entry.delete(0,END)


class Aplication(Functions):
    
    def __init__(self):
        self.root = root
        self.screen()
        self.frames()
        self.buttons()
        self.labels()
        self.entrys()
        self.root.mainloop()
        
    def screen(self):
        self.root.title("Video Downloader")
        self.root.configure(background = 'blue')
        self.root.geometry("500x300")
        self.root.resizable(False,False)
        self.root.maxsize(width = 600, height = 400)
        self.root.minsize(300,200)
        
    def frames(self):
        self.frame1 = Frame(self.root, bd = 4, highlightbackground = "lightblue", highlightthickness = 4)    
        self.frame1.place(relx = 0.125, rely = 0.2, relwidth = 0.75, relheight = 0.60) 
        
    def buttons(self):
        self.button = Button(self.frame1, text = "baixar", bd = 0.5, bg = "white",fg = "black",command = self.download)
        self.button.place(relx = 0.375,rely = 0.10, relwidth = 0.30, relheight = 0.20)
        
    def labels(self):
        self.label = Label(self.frame1, text = "url",bg = "white",fg = "black")
        self.label.place(relx = 0.050,rely = 0.5, relwidth = 0.15, relheight = 0.20)
        
    def entrys(self):
        self.entry = Entry(self.frame1,bd = 3)
        self.entry.place(relx = 0.20,rely = 0.5, relwidth = 0.65, relheight = 0.20)
        x = self.entry.get()
        print(x)
        
        
        
        
        
        
        
        
        
        
        
        
Aplication()
