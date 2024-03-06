# Requirements
# pygame

import tkinter as tk
from tkinter import filedialog
import pygame

class AudioPlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Audio Player")
        
        self.audio_file = None
        self.playing = False
        
        self.create_widgets()
    
    def create_widgets(self):
        # Open file button
        self.open_button = tk.Button(self.master, text="Open Audio", command=self.open_audio)
        self.open_button.pack()
        
        # Play/Pause button
        self.play_button = tk.Button(self.master, text="Play", command=self.play_pause)
        self.play_button.pack()
        
    def open_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if file_path:
            self.audio_file = file_path
    
    def play_pause(self):
        if self.audio_file:
            if not self.playing:
                pygame.mixer.init()
                pygame.mixer.music.load(self.audio_file)
                pygame.mixer.music.play()
                self.playing = True
            else:
                pygame.mixer.music.stop()
                self.playing = False

def main():
    root = tk.Tk()
    root.geometry('400x300')
    AudioPlayerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
