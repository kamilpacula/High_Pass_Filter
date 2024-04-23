import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
def convertToGrayscale(image):
    image = image.convert("L")
    return image

def displayGrayscale(container):
    global loaded_image

    loaded_image_widget = container.winfo_children()[0]

    if loaded_image_widget:
        loaded_image = ImageTk.getimage(loaded_image_widget)
        grayscale_image = convert_to_grayscale(loaded_image)
        grayscale_label = ttk.Label(container, image=grayscale_image)
        grayscale_label.pack()
        loaded_image_widget.destroy()
        loaded_image = grayscale_image