# Requires
# pip install Pillow

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Viewer")
        
        self.image_label = tk.Label(self.master)
        self.image_label.pack()
        
        self.create_menu()
    
    def create_menu(self):
        menubar = tk.Menu(self.master)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open Image", command=self.open_image)
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.master.config(menu=menubar)
    
    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.gif;*.bmp")])
        if file_path:
            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep a reference to avoid garbage collection

def main():
    root = tk.Tk()
    root.geometry("800x600")
    app = ImageViewerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
