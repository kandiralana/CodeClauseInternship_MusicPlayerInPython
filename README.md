# Simple Music Player

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
    - [main.py](#mainpy)
    - [constants.py](#constantspy)
    - [simple_music_player.py](#simple_music_playerpy)
- [Dependencies](#dependencies)

## Overview

This project features a Simple Music Player application with a graphical user interface. It uses Tkinter for GUI
components, PIL for image processing, and pygame for handling music playback. The application allows users to browse and
play music, control playback, and visualize an animated GIF.

## Installation

To run the Simple Music Player, follow these steps:

1. Ensure you have the required dependencies installed by running:

    ```bash
    pip install tkinter
    pip install PIL
    pip install pygame
    pip install os
    pip install screeninfo
    ```

2. Clone the repository to your local machine:

```bash
git clone https://github.com/kandiralana/CodeClauseInternship_MusicPlayerInPython.git
cd CodeClauseInternship_MusicPlayerInPython
```

3. Run the application:

```bash
python main.py
```

## Usage

Launch the application using the command specified in the installation section.
Click on the "Browse Music" button to add songs to the playlist.
Control playback using the play, pause, stop, next, and previous buttons.
Enjoy the animated visual experience while listening to your favorite music!

## File Descriptions

## File Descriptions

### main.py

The main script to instantiate the SimpleMusicPlayer class and run the application.

- `main()`: The main function to run the Simple Music Player application.
    - Creates a `SimpleMusicPlayer` object.
    - Launch the program.

### constants.py

- defines constants used in a simple music player application for graphical assets and dimensions
    - PLAYER_WIDTH (int): Width of the music player window.
    - PLAYER_HEIGHT (int): Height of the music player window.
    - APP_LOGO (str): Path to the application logo image file.
    - PLAY_BUTTON (str): Path to the play button image file.
    - PAUSE_BUTTON (str): Path to the pause button image file.
    - STOP_BUTTON (str): Path to the stop button image file.
    - PREVIOUS_SONG_BUTTON (str): Path to the previous song button image file.
    - NEXT_SONG_BUTTON (str): Path to the next song button image file.
    - GIF (str): Path to an animated GIF used for visual elements.

### simple_music_player.py

This module defines the SimpleMusicPlayer class responsible for creating the graphical interface, controlling music
playback, and managing the songlist.

- `get_center(p_width=500, p_height=400)`:  Function that calculates the center coordinates for a window based on the
  primary monitor's dimensions.

- `SimpleMusicPlayer`:  Class is implementing the main functionality of the music player application. Initializes the
  GUI,
  controls music playback, and manages the songlist.
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

## Dependencies

- `tkinter`: GUI toolkit for Python.
- `PIL`: Python Imaging Library for image processing.
- `pygame`: Library for multimedia applications (audio playback in this case).
- `screeninfo`: Library for retrieving monitor information.
- `os`: Operating system interfaces for file operations.

## Contributions

Contributions are welcome! If you have any feature requests, bug reports, or suggestions, please open an issue or submit
a pull request.