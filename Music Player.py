import pygame
import tkinter as tkr
import os

#create the player
player = tkr.Tk()

#edit window
player.title("Audio Player")
player.geometry("205x340")

#playlist register
os.chdir("C:/Users/44770/Documents/Music Player/my song list")
print(os.getcwd)
songList = os.listdir()

#volume input
VolumeLevel = tkr.Scale(player, from_=0.0, to_=1.0, orient = tkr.HORIZONTAL, resolution = 0.01)

#playlist input
playlist = tkr.Listbox(player, highlightcolor="blue", selectmode = tkr.SINGLE)
print(songList)
for item in songList:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

#pygame
pygame.init()
pygame.mixer.init()

#action interface
def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(VolumeLevel.get())
    print(pygame.mixer.music.set_volume())
    print(VolumeLevel.get())
    
def ExitPlayer():
    pygame.mixer.music.stop()

def Pause():
    pygame.mixer.music.pause()
    
def UnPause():
    pygame.mixer.music.unpause()

#register buttons
Button1 = tkr.Button(player, width=5, height=3, text="PLAY", command=Play)
Button2 = tkr.Button(player, width=5, height=3, text="STOP", command=ExitPlayer)
Button3 = tkr.Button(player, width=5, height=3, text="PAUSE", command=Pause)
Button4 = tkr.Button(player, width=5, height=3, text="UNPAUSE", command=UnPause)

#song names
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable=var)

#place widgets
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
songtitle.pack()
VolumeLevel.pack(fill="both", expand="yes")
playlist.pack(fill="both", expand="yes")

#activate
player.mainloop()
