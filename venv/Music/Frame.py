import ctypes
import threading
import time
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox

from music import *


class Frame:
    top = ""
    playbutton = addbutton = stopbutton = scale = pausebutton = listbox = label = ""
    songs = ""
    files = []

    def startSong(self):
        track = self.listbox.get(ANCHOR)
        print(track)
        if track == "":
            text.set("Item not selected...")
        else:
            self.songs.playTrack(track)
            text.set("")

    def pauseSong(self):
        self.songs.pauseTrack()

    def setVolume(self, vol):
        self.songs.volumeControl(vol)

    def stopSong(self):
        self.songs.stopTrack()

    def addSong(self):
        filename = askopenfilename(initialdir="/", title="Select file",
                                   filetypes=(("Audio Files", ".mp3 .wav .ogg"), ("all files", "*.*")))
        string = str(filename)
        self.listbox.insert(1, string)

    def __init__(self):
        self.songs = MusicFiles()
        self.top = Tk()
        self.top.title("Music player")
        self.top.geometry("350x200")
        self.top.config(bg="cyan")

        self.playbutton = Button(self.top, width=4, text="Play", command=self.startSong)
        self.playbutton.place(x=67, y=20)

        self.stopbtnbutton = Button(self.top, text="Stop", width=4, command=self.stopSong)
        self.stopbtnbutton.place(x=35, y=50)
        global text
        text = StringVar()
        self.label = Label(self.top, textvariable=text).place(x=10, y=160)

        self.pausebutton = Button(self.top, text="Pause", width=4, command=self.pauseSong)
        self.pausebutton.place(x=99, y=50)

        self.addbutton = Button(self.top, text="Add Track", width=10, command=self.addSong)
        self.addbutton.place(x=180, y=150)

        self.listbox = Listbox(self.top, height=8, width=25)
        self.listbox.place(x=180, y=20)

        self.scale = Scale(self.top,
                           from_=0, to=100, orient=HORIZONTAL, command=self.setVolume)
        self.scale.place(x=35, y=85)
        label = Label(self.top, text="Volume").place(x=65, y=125)

        self.top.mainloop()


framebuild = Frame()
