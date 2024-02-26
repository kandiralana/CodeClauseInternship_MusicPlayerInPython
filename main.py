"""
Simple Music Player Application

This script initializes and runs a SimpleMusicPlayer instance, providing a graphical user interface for playing music.
The SimpleMusicPlayer class is responsible for managing the music player window, controlling playback, and handling user
interactions.

Usage:
- Ensure the 'simple_music_player' module contains the SimpleMusicPlayer class.
- Run this script to launch the Simple Music Player application.

Example:
    $ python main.py

Note: Ensure the necessary dependencies, such as tkinter, Pillow (PIL), pygame, and screeninfo, are installed.
"""

from simple_music_player import SimpleMusicPlayer

if __name__ == '__main__':
    # Create an instance of the SimpleMusicPlayer class
    simple_player = SimpleMusicPlayer()

    # Run the main loop of the Tkinter application
    simple_player.run()
