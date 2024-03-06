# creating a notepad in python

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class NotepadApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Note Editor")
        self.textarea = tk.Text(self.master, wrap="word")
        self.textarea.pack(expand=True, fill="both")
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.master)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.master.config(menu=menubar)

    def new_file(self):
        self.textarea.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.textarea.delete(1.0, tk.END)
                self.textarea.insert(tk.END, content)

    def save_file(self):
        content = self.textarea.get(1.0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)
            messagebox.showinfo("Success", "File saved successfully.")

def main():
    root = tk.Tk()
    root.geometry("900x700")
    NotepadApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
