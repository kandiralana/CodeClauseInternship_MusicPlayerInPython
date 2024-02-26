from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageSequence
from pygame import mixer
import os
from screeninfo import get_monitors
from constants import *



def get_center(p_width=500, p_height=400):
    monitors = get_monitors()
    if monitors:
        primary_monitor = monitors[0]
        width, height = primary_monitor.width, primary_monitor.height
        center_x = int(width / 2 - p_width / 2)
        center_y = int(height / 2 - p_height / 1.3)
        return center_x, center_y
    else:
        return None


class SimpleMusicPlayer:
    def __init__(self):
        self.player_width = PLAYER_WIDTH
        self.player_height = PLAYER_HEIGHT

        self.frames = None
        self.label = None
        self.songlist = None
        self.songs = []
        self.current_song = ""
        self.paused = False
        self.paused_position = 0

        self.initialize_gui()

        mixer.init()

        self.create_frames()

        self.add_animation()

        self.play_button_image = self.load_image(PLAY_BUTTON)
        self.pause_button_image = self.load_image(PAUSE_BUTTON)
        self.stop_button_image = self.load_image(STOP_BUTTON)
        self.next_button_image = self.load_image(NEXT_SONG_BUTTON)
        self.previous_button_image = self.load_image(PREVIOUS_SONG_BUTTON)
        self.create_control_buttons()

        self.create_songlist()

    def initialize_gui(self):
        self.root = Tk()
        self.root.title("SIMPLE MUSIC PLAYER")
        self.set_window_properties()

    def set_window_properties(self):
        self.root.geometry(f"{self.player_height}x{self.player_width}+{get_center()[0]}+{get_center()[1]}")
        self.root.configure(background='#F5FCFF')
        self.root.resizable(False, False)
        self.root.iconphoto(False, PhotoImage(file="icons/player_logo.png"))

    def create_frames(self):
        animation = self.create_animation_frame()
        self.animation_frame = animation[0]
        self.animation_frame_size = animation[1]

        control = self.create_control_frame(self.animation_frame_size)
        self.control_frame = control[0]
        self.control_frame_size = control[1]

        music = self.create_frame_songlist(self.control_frame_size)
        self.music_frame = music[0]
        self.music_frame_size = music[1]

    def __del__(self):
        mixer.quit()

    def add_animation(self):
        gif = Image.open(GIF)
        self.frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(gif)]

        self.label = Label(self.animation_frame)
        self.label.place(x=-10, y=-50)
        self.root.after(0, self.update, 0)

    def update(self, ind):
        frame = self.frames[ind]
        ind += 1
        if ind == len(self.frames):
            ind = 0
        self.label.configure(image=frame)
        self.root.after(120, self.update, ind)

    def create_animation_frame(self):
        start_point_x = 0
        start_point_y = 0

        frame_height = int(self.player_height / 5 * 2.5)
        frame_weight = self.player_width

        animation_frame = Frame(self.root, bg='#F5FCFF', width=frame_weight, height=frame_height)
        animation_frame.place(x=start_point_x, y=start_point_y)
        return animation_frame, frame_height

    def create_control_frame(self, animation_frame_size):
        start_point_x = 0
        start_point_y = animation_frame_size

        frame_height = int(self.player_height / 5 * 2)
        frame_weight = self.player_width

        control_frame = Frame(self.root, bg="#F3F4F4", width=frame_weight, height=frame_height)
        control_frame.place(x=start_point_x, y=start_point_y)
        return control_frame, frame_height

    def create_frame_songlist(self, control_frame_size):
        start_point_x = 0
        start_point_y = control_frame_size + self.animation_frame_size

        frame_height = int(self.player_height / 5 * 2)
        frame_weight = self.player_width

        songlist_frame = Frame(self.root, bg="#333333", width=frame_weight, height=frame_height)
        songlist_frame.place(x=start_point_x, y=start_point_y)
        return songlist_frame, frame_height

    def create_songlist(self):
        self.songlist = Listbox(self.music_frame, width=PLAYER_WIDTH, height=100, selectbackground="grey",
                                background='#333333', fg='#F0F0F0')
        self.songlist.place(x=0, y=10)
        self.songlist.pack(side=RIGHT, fill=BOTH)

    @staticmethod
    def load_image(path):
        return ImageTk.PhotoImage(Image.open(path))

    def create_control_buttons(self):
        browse_music_bt = Button(self.control_frame, text="Browse Music", width=40, height=2, borderwidth=4,
                                 font=("calibri", 12, "bold"), fg="#333333", bg="#F0F0F0",
                                 command=self.add_music, cursor="hand2")

        play_button = Button(self.control_frame, image=self.play_button_image, borderwidth=0, highlightthickness=0,
                             command=self.play_music, padx=0, pady=0, cursor="hand2", relief='flat', height=60, width=40)
        pause_button = Button(self.control_frame, image=self.pause_button_image, borderwidth=0, highlightthickness=0,
                              command=self.pause_music, padx=0, pady=0, cursor="hand2", height=60, width=40)
        stop_button = Button(self.control_frame, image=self.stop_button_image, borderwidth=0, highlightthickness=0,
                             command=self.stop_music, padx=0, pady=0, cursor="hand2", height=60, width=40)
        next_button = Button(self.control_frame, image=self.next_button_image, borderwidth=0, highlightthickness=0,
                             command=self.next_song, padx=0, pady=0, cursor="hand2", height=60, width=40)
        previous_button = Button(self.control_frame, image=self.previous_button_image, borderwidth=0, highlightthickness=0,
                                 command=self.previous_song, padx=0, pady=0, cursor="hand2", height=60, width=40)

        previous_button.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=20)
        play_button.grid(row=0, column=1, sticky="nsew", padx=(5, 0), pady=20)
        pause_button.grid(row=0, column=2, sticky="nsew", padx=(5, 0), pady=20)
        stop_button.grid(row=0, column=3, sticky="nsew", padx=(5, 5), pady=20)
        next_button.grid(row=0, column=4, sticky="nsew", padx=(0, 10), pady=20)

        browse_music_bt.grid(row=3, column=0, sticky="nsew", columnspan=5, pady=10)

    def add_music(self):
        try:
            self.root.directory = filedialog.askdirectory()
            if self.root.directory:
                for song in os.listdir(self.root.directory):
                    song_name, ext = os.path.splitext(song)
                    if ext == '.mp3':
                        self.songs.append(song)

                for song in self.songs:
                    self.songlist.insert(END, song)

                self.songlist.selection_set(0)
                self.current_song = self.songs[self.songlist.curselection()[0]]

        except Exception as e:
            print(f"Error adding music: {e}")

    def play_music(self):
        try:
            if not self.paused:
                selected_index = self.songlist.curselection()[0]
                selected_song = self.songs[selected_index]

                mixer.music.load(os.path.join(self.root.directory, selected_song))
                mixer.music.play()

                self.current_song = selected_song
                self.paused = False
            else:
                mixer.music.unpause()
                mixer.music.play(start=self.paused_position)  # Resume from the paused position
                self.paused = False

        except Exception as e:
            print(f"Error playing music: {e}")

    def pause_music(self):
        try:
            self.paused = True
            self.paused_position = mixer.music.get_pos() // 1000  # Get position in seconds
            mixer.music.pause()

        except Exception as e:
            print(f"Error pausing music: {e}")

    def stop_music(self):
        try:
            self.paused = False
            mixer.music.stop()

        except Exception as e:
            print(f"Error stopping music: {e}")

    def next_song(self):
        try:
            selected_index = self.songlist.curselection()[0]
            selected_index = (selected_index + 1) % len(self.songs)  # Get the next index, circular
            self.songlist.selection_clear(0, END)
            self.songlist.selection_set(selected_index)
            self.current_song = self.songs[selected_index]
            self.play_music()

        except Exception as e:
            print(f"Error selecting next song: {e}")

    def previous_song(self):
        try:
            selected_index = self.songlist.curselection()[0]
            selected_index = (selected_index - 1) % len(self.songs)  # Get the previous index, circular
            self.songlist.selection_clear(0, END)
            self.songlist.selection_set(selected_index)
            self.current_song = self.songs[selected_index]
            self.play_music()

        except Exception as e:
            print(f"Error selecting previous song: {e}")

    def run(self):
        self.root.mainloop()



