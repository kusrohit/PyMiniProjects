# Requirements
# moviepy 
# pygame

import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip


class VideoPlayerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Video Player")

        self.play_button = None
        self.open_button = None
        self.video_clip = None
        self.playing = False
        
        self.create_widgets()
    
    def create_widgets(self):
        # Open file button
        self.open_button = tk.Button(self.master, text="Open Video", command=self.open_video)
        self.open_button.pack()
        
        # Play/Pause button
        self.play_button = tk.Button(self.master, text="Play", command=self.play_pause)
        self.play_button.pack()
        
    def open_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
        if file_path:
            self.video_clip = VideoFileClip(file_path)
    
    def play_pause(self):
        if self.video_clip:
            if not self.playing:
                self.video_clip.preview()
                self.playing = True
            else:
                self.video_clip.close()
                self.playing = False


def main():
    root = tk.Tk()
    root.geometry("400x300")
    VideoPlayerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
