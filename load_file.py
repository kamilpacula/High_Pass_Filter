import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image

def loadFile(container):
    loaded_image = None
    file_path = filedialog.askopenfilename()
    for widget in container.winfo_children():
        widget.destroy()
    if file_path:
        image = Image.open(file_path)
        resized_image = image.resize((400, 300), Image.LANCZOS)
        photo = ImageTk.PhotoImage(resized_image)
        image_label = ttk.Label(container, image=photo)
        image_label.photo = photo
        image_label.pack(fill='both', expand=True)