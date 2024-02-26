"""
Simple Music Player Application

This module defines a SimpleMusicPlayer class and a utility function for centering windows using Tkinter, PIL,
and pygame.

Classes:
- SimpleMusicPlayer: A simple music player application using tkinter and pygame.

Functions:
- get_center(p_width=500, p_height=400): Calculate the center coordinates for a window based on the primary monitor's
dimensions.

Constants (Imported from 'constants' module):
- PLAYER_WIDTH (int): Width of the music player window.
- PLAYER_HEIGHT (int): Height of the music player window.
- APP_LOGO (str): Path to the application logo image file.
- PLAY_BUTTON (str): Path to the play button image file.
- PAUSE_BUTTON (str): Path to the pause button image file.
- STOP_BUTTON (str): Path to the stop button image file.
- PREVIOUS_SONG_BUTTON (str): Path to the previous song button image file.
- NEXT_SONG_BUTTON (str): Path to the next song button image file.
- GIF (str): Path to an animated GIF used for visual elements.

Note:
- Ensure that the specified image files exist in the designated paths before using them in the music player application.
"""

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageSequence
from pygame import mixer
import os
from screeninfo import get_monitors
from constants import *


def get_center(p_width=500, p_height=400):
    """
    Calculate the center coordinates for a window based on the primary monitor's dimensions.

    :param p_width: Width of the window (int).
    :param p_height: Height of the window (int).

    :return: Tuple[int, int] or None: Center coordinates (x, y) or None if no monitors are available.
    """
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
    """
    A simple music player application using tkinter and pygame.

    Attributes:
    - player_width (int): Width of the music player window.
    - player_height (int): Height of the music player window.
    - frames (list): List to store frames for animation.
    - label (Label): Label widget for displaying animation frames.
    - songlist (Listbox): Listbox widget for displaying the list of songs.
    - songs (list): List to store the names of songs.
    - current_song (str): Name of the currently playing song.
    - paused (bool): Flag indicating whether the music is paused.
    - paused_position (int): Position in seconds where the music was paused.

    Methods:
    - initialize_gui(): Initialize the main Tkinter window.
    - set_window_properties(): Set properties for the main window.
    - create_frames(): Create different frames for animation, controls, and songlist.
    - __del__(): Destructor to clean up the mixer when the object is deleted.
    - add_animation(): Add an animated GIF to the GUI.
    - update(ind): Update the animation frames.
    - create_animation_frame(): Create the frame for displaying animation.
    - create_control_frame(animation_frame_size): Create the frame for control buttons.
    - create_frame_songlist(control_frame_size): Create the frame for displaying the songlist.
    - create_songlist(): Create and configure the Listbox for displaying songs.
    - load_image(path): Load an image from the given path and return a PhotoImage object.
    - create_control_buttons(): Create and configure control buttons for the music player.
    - add_music(): Open a file dialog to add music to the songlist.
    - play_music(): Play the selected or paused music.
    - pause_music(): Pause the currently playing music.
    - stop_music(): Stop the currently playing music.
    - next_song(): Play the next song in the songlist.
    - previous_song(): Play the previous song in the songlist.
    - run(): Run the main loop of the Tkinter application.
    """

    def __init__(self):
        """
        Initialize the main elements of the class.
        """
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
        """
        Initialize the main Tkinter window.
        :return: None
        """
        self.root = Tk()
        self.root.title("SIMPLE MUSIC PLAYER")
        self.set_window_properties()

    def set_window_properties(self):
        """
        Set properties for the main window
        :return: None
        """

        self.root.geometry(f"{self.player_height}x{self.player_width}+{get_center()[0]}+{get_center()[1]}")
        self.root.configure(background='#F5FCFF')
        self.root.resizable(False, False)
        self.root.iconphoto(False, PhotoImage(file="icons/player_logo.png"))

    def create_frames(self):
        """
        Create different frames for animation, controls, and songlist.
        :return: None
        """
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
        """
        Destructor to clean up the mixer when the object is deleted.
        :return: None
        """
        mixer.quit()

    def create_animation_frame(self):
        """
        Create the frame for displaying animation.
        :return: Tuple[Frame, int]: Tuple containing the animation frame and its height.
        """
        start_point_x = 0
        start_point_y = 0

        frame_height = int(self.player_height / 5 * 2.5)
        frame_weight = self.player_width

        animation_frame = Frame(self.root, bg='#F5FCFF', width=frame_weight, height=frame_height)
        animation_frame.place(x=start_point_x, y=start_point_y)
        return animation_frame, frame_height

    def add_animation(self):
        """
        Add an animated GIF to the GUI.
        :return: None
        """
        gif = Image.open(GIF)
        self.frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(gif)]

        self.label = Label(self.animation_frame)
        self.label.place(x=-10, y=-50)
        self.root.after(0, self.update, 0)

    def update(self, ind):
        """
        Update the animation frames.
        :param ind: Index of the current animation frame.
        :return: None
        """
        frame = self.frames[ind]
        ind += 1
        if ind == len(self.frames):
            ind = 0
        self.label.configure(image=frame)
        self.root.after(120, self.update, ind)

    def create_control_frame(self, animation_frame_size):
        """
        Create the frame for control buttons.
        :param animation_frame_size: Height of the animation frame (int).
        :return: Tuple[Frame, int]: Tuple containing the control frame and its height
        """

        start_point_x = 0
        start_point_y = animation_frame_size

        frame_height = int(self.player_height / 5 * 2)
        frame_weight = self.player_width

        control_frame = Frame(self.root, bg="#F3F4F4", width=frame_weight, height=frame_height)
        control_frame.place(x=start_point_x, y=start_point_y)
        return control_frame, frame_height

    def create_frame_songlist(self, control_frame_size):
        """
        Create the frame for displaying the songlist.
        :param control_frame_size: Height of the control frame (int).
        :return: Tuple[Frame, int]: Tuple containing the songlist frame and its height.
        """

        start_point_x = 0
        start_point_y = control_frame_size + self.animation_frame_size

        frame_height = int(self.player_height / 5 * 2)
        frame_weight = self.player_width

        songlist_frame = Frame(self.root, bg="#333333", width=frame_weight, height=frame_height)
        songlist_frame.place(x=start_point_x, y=start_point_y)
        return songlist_frame, frame_height

    def create_songlist(self):
        """
        Create and configure the Listbox for displaying songs.
        :return: Listbox frame for a song list (tkinter.Listbox)
        """
        self.songlist = Listbox(self.music_frame, width=PLAYER_WIDTH, height=100, selectbackground="grey",
                                background='#333333', fg='#F0F0F0')
        self.songlist.place(x=0, y=10)
        self.songlist.pack(side=RIGHT, fill=BOTH)
        return self.songlist

    @staticmethod
    def load_image(path):
        """
        Load an image from the given path and return a PhotoImage object.
        :param path: Path to the image file ((str)).
        :return: Image loaded from the specified path.
        """
        return ImageTk.PhotoImage(Image.open(path))

    def create_control_buttons(self):
        """
        Create and configure control buttons for the music player.
        :return: None
        """
        browse_music_bt = Button(self.control_frame, text="Browse Music", width=40, height=2, borderwidth=4,
                                 font=("calibri", 12, "bold"), fg="#333333", bg="#F0F0F0",
                                 command=self.add_music, cursor="hand2")

        play_button = Button(self.control_frame, image=self.play_button_image, borderwidth=0, highlightthickness=0,
                             command=self.play_music, padx=0, pady=0, cursor="hand2", relief='flat', height=60,
                             width=40)
        pause_button = Button(self.control_frame, image=self.pause_button_image, borderwidth=0, highlightthickness=0,
                              command=self.pause_music, padx=0, pady=0, cursor="hand2", height=60, width=40)
        stop_button = Button(self.control_frame, image=self.stop_button_image, borderwidth=0, highlightthickness=0,
                             command=self.stop_music, padx=0, pady=0, cursor="hand2", height=60, width=40)
        next_button = Button(self.control_frame, image=self.next_button_image, borderwidth=0, highlightthickness=0,
                             command=self.next_song, padx=0, pady=0, cursor="hand2", height=60, width=40)
        previous_button = Button(self.control_frame, image=self.previous_button_image, borderwidth=0,
                                 highlightthickness=0,
                                 command=self.previous_song, padx=0, pady=0, cursor="hand2", height=60, width=40)

        previous_button.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=20)
        play_button.grid(row=0, column=1, sticky="nsew", padx=(5, 0), pady=20)
        pause_button.grid(row=0, column=2, sticky="nsew", padx=(5, 0), pady=20)
        stop_button.grid(row=0, column=3, sticky="nsew", padx=(5, 5), pady=20)
        next_button.grid(row=0, column=4, sticky="nsew", padx=(0, 10), pady=20)

        browse_music_bt.grid(row=3, column=0, sticky="nsew", columnspan=5, pady=10)

    def add_music(self):
        """
        Open a file dialog to add music to the songlist.
        :return: None
        """
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
        """
        Play the selected or paused music.
        :return: None
        """
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
        """
        Pause the currently playing music.
        :return: None
        """
        try:
            self.paused = True
            self.paused_position = mixer.music.get_pos() // 1000  # Get position in seconds
            mixer.music.pause()

        except Exception as e:
            print(f"Error pausing music: {e}")

    def stop_music(self):
        """
        Stop the currently playing music.
        :return: None
        """
        try:
            self.paused = False
            mixer.music.stop()

        except Exception as e:
            print(f"Error stopping music: {e}")

    def next_song(self):
        """
        Play the next song in the songlist.
        :return: None
        """
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
        """
        Play the previous song in the songlist.
        :return: None
        """
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
        """
        Run the main loop of the Tkinter application.
        :return: None
        """
        self.root.mainloop()
