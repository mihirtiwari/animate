import Tkinter as tk
from Tkinter import Label
from PIL import Image, ImageTk

root = tk.Tk()

def display_obj(root, obj):
    label = Label(root, image=obj)
    label.image = obj
    label.pack()

    root.mainloop()

"""
Displays the object on the screen
"""
def display(object):
    image = Image.open(object.get_image())
    photo = ImageTk.PhotoImage(image)

    display_obj(root, photo)

# """
# Animates the selected object with the given action
# """
# def show_action(object, action):
