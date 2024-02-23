import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

root = Tk()
root.title("SIMPLE MUSIC PLAYER")
root.geometry("485x700+290+10")
root.configure(background='#333333')
root.resizable(False, False)
mixer.init()


# Create a function to open a file
def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)


# Create a function to play a music
def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name(ACTIVE))
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


# icon
lower_frame = Frame(root, bg="#FFFFFF", width=485, height=180)
lower_frame.place(x=0, y=400)

image_icon = PhotoImage(file="icons/player_logo.png")
root.iconphoto(False, image_icon)

frameCNT = 30
frames = [PhotoImage(file="icons/turn-around-anime.gif", format='gif - index %i' % i) for i in range(frameCNT)]


def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCNT:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)


label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)

ButtonPlay = PhotoImage(file="icons/play_button.png")
Button(root, image=ButtonPlay, bg="#FFFFFF", bd=0, height=60, width=60,
       command=PlayMusic, cursor="hand2").place(x=215, y=487)

ButtonStop = PhotoImage(file="icons/stop_button.png")
Button(root, image=ButtonStop, bg="#FFFFFF", bd=0, height=60, width=60,
       command=mixer.music.stop, cursor="hand2").place(x=130, y=487)

ButtonPause = PhotoImage(file="icons/pause_button.png")
Button(root, image=ButtonPause, bg="#FFFFFF", bd=0, height=60, width=60,
       command=mixer.music.pause, cursor="hand2").place(x=300, y=487)

Volume = PhotoImage(file="icons/speaker_button.png")
panel = Label(root, image=Volume).place(x=20, y=487)

# Label
Menu = PhotoImage(file="icons/menu.png")
Label(root, image=Menu).place(x=0, y=580, width=485, height=120)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=584, width=485, height=100)
# Frame_Music.place(x=0, y=585, width=485, height=100)

Button(root, text="Browse Music", width=50, height=2, font=("calibri", 12, "bold"), fg="#333333", bg="#FFFFFF",
       command=AddMusic, cursor="hand2").place(x=0, y=550)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("calibri", 10), bg="#333333", fg="grey",
                   selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)

Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

# Execute Tkinter
root.mainloop()
