import os

from pygame import mixer


class MusicFiles():
    audiolink = []
    stop = ""
    pause = ""

    def __init__(self):
        mixer.init()

    def playTrack(self, track):

        if self.pause == 1:
            mixer.music.unpause()
            print("Resume")
            self.pause = ""

        elif self.stop == 2:
            mixer.music.load(track.strip())
            mixer.music.play()
            print("Play")
            self.stop = ""
        else:

            mixer.music.load(track.strip())
            mixer.music.play()
            print("Play")

    def stopTrack(self):
        self.stop = 2
        mixer.music.stop()
        print("stop")

    def volumeControl(self, vol):
        v = int(vol) / 100
        mixer.music.set_volume(v)

    def pauseTrack(self):
        self.pause = 1
        mixer.music.pause()
        print("pause")
