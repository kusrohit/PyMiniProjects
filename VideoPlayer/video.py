"""
Requirement of video player

python-vlc
tkinter
datetime
"""

import tkinter as tk
import vlc


from tkinter import filedialog
from datetime import timedelta


class MediaPlayerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.progress_bar = None
        # self.rewind_button = None
        # self.fast_forward_button = None
        # self.pause_button = None
        # self.stop_button = None
        # self.play_button = None
        # self.control_buttons_frame = None
        # self.time_label = None
        # self.select_file_button = None
        # self.current_file = None
        # self.media_player = None
        # self.instance = None
        self.palying_video = None
        self.video_paused = False
        self.playing_video = False

        self.media_canvas = tk.Canvas(self, bg="black", width=800, height=400)
        self.title("Media Player")
        self.geometry("400x300")
        self.configure(bg="#f0f0f0")

        self.initialize_player()

    def initialize_player(self):
        self.instance = vlc.Instance()
        self.media_player = self.instance.media_player_new()
        self.create_widgets()

    def create_widgets(self):
        # Media Canvas
        self.media_canvas.pack(pady=10, fill=tk.BOTH, expand=True)

        # File Button
        self.select_file_button = tk.Button(
            self,
            text="Select File",
            font=("Arial", 14, "bold"),
            command=self.select_file,
        )
        self.select_file_button.pack(pady=5)

        # Time label
        self.time_label = tk.Label(
            self,
            text="00:00:00/00:00:00",
            font=("Arial", 14, "bold"),
            fg="#555555",
            bg="#f0f0f0",
        )
        self.time_label.pack(pady=5)

        # Button Control Frame
        self.control_buttons_frame = tk.Frame(self, bg="#f0f0f0")
        self.control_buttons_frame.pack(pady=5)

        # Play button
        self.play_button = tk.Button(
            self.control_buttons_frame,
            text="Play",
            font=("Arial", 14, "bold"),
            bg="#4caf50",
            fg="white",
            command=self.play_video,
        )
        self.play_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Pause Button
        self.pause_button = tk.Button(
            self.control_buttons_frame,
            text="Pause",
            font=("Arial", 14, "bold"),
            bg="#ff9800",
            fg="white",
            command=self.pause_video,
        )
        self.pause_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Stop Button
        self.stop_button = tk.Button(
            self.control_buttons_frame,
            text="Stop",
            font=("Arial", 14, "bold"),
            bg="#f44336",
            fg="white",
            command=self.stop,
        )
        self.stop_button.pack(side=tk.LEFT, pady=5)

        # Forward Button
        self.fast_forward_button = tk.Button(
            self.control_buttons_frame,
            text="Fast forward",
            font=("Arial", 14, "bold"),
            bg="#2196f3",
            fg="white",
            command=self.fast_forward,
        )
        self.fast_forward_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Rewind Button
        self.rewind_button = tk.Button(
            self.control_buttons_frame,
            text="Rewind",
            font=("Arial", 14, "bold"),
            bg="#2196f3",
            fg="white",
            command=self.rewind_video,
        )
        self.rewind_button.pack(side=tk.LEFT, pady=5)

        # Progress Bar
        # self.progress_bar = VideoProgressBar(
        #     self,
        #     self.set_video_position,
        #     bg="#e0e0e0",
        #     highlightthickness=0,
        # )

    # Functionality
    def select_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Media Files", "*.mp4 *.avi")]
        )
        if file_path:
            self.current_file = file_path
            self.time_label.config(text="00:00:00/" + self.get_duration_str())
            self.play_video()

    def get_duration_str(self):
        if self.palying_video:
            total_duration = self.media_player.get_length()
            total_duration_str = str(timedelta(milliseconds=total_duration))[:-3]
            return total_duration_str
        return "00:00:00"

    def play_video(self):
        if not self.playing_video:
            media = self.instance.media_new(self.current_file)
            self.media_player.set_media(media)
            self.media_player.set_hwnd(self.media_canvas.winfo_id())
            self.media_player.play()
            self.playing_video = True

    def pause_video(self):
        if self.playing_video:
            if self.video_paused:
                self.media_player.play()
                self.video_paused = False
                self.pause_button.config(text="Pause")
            else:
                self.media_player.pause()
                self.video_paused = True
                self.pause_button.config(text="Resume")
                

    def stop(self):
        if self.playing_video:
            self.media_player.stop()
            self.playing_video = False
        self.time_label.config(text="00:00:00/" + self.get_duration_str())

    def fast_forward(self):  # 10 sec forward
        if self.playing_video:
            current_time = self.media_player.get.time() + 10000
            self.media_player.set_time(current_time)

    def rewind_video(self):  # 10 sec backward
        if self.playing_video:
            current_time = self.media_player.get_time() - 10000
            self.media_player.set_time(current_time)

    def set_video_position(self, value):
        if self.playing_video:
            total_duration = self.media_player.get_length()
            position = int((float(value)/100)*total_duration)
            self.media_player.set_time(position)
            
    # def update_video_progress(self):
    #     if self.playing_video:
    #         total_duration = self.media_player.get_length()
    #         current_time = self.media_player.get_time()
    #         progress_percentage = (current_time/total_duration)*100
    #         self.progress_bar.set(progress_percentage)
    #         current_time_str = str(timedelta(milliseconds=current_time))[:-3]
    #         total_duration_str = str(timedelta(milliseconds=total_duration))[:-3]
    #         self.time_label.config(text=f"{current_time_str}/{total_duration_str}")
    #     self.after(1000,self.update_video_progress)

# class VideoProgressBar(tk.Scale):
#     def __init__(self, master, command, **kwargs):
# 
#         kwargs["showvalue"] = False
#         super().__init__(
#             master,
#             from=0,
#             top=100,
#             orient=tk.HORIZONTAL,
#             length=800,
#             command=command,
#             **kwargs,
#         )
#         self.bind("<Button-1", self.on_click)
#         
#     def on_click(self,event):
#         if self.cget("state") == tk.NORMAL:
#             value = (event.x/self.winfo_width()) * 100
#             self.set(value)
# 
#     def command(self, value):
#         print("value: ", value)
            


def main():
    # root = tk.Tk()
    app = MediaPlayerApp()
    # app.update_video_progress()
    app.mainloop()


if __name__ == '__main__':
    main()

#  Not Working
