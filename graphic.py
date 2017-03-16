import Tkinter as tk
from Tkinter import Canvas
from PIL import Image, ImageTk

root = tk.Tk()

def display_obj(root, obj):
    # label = Label(root,image=obj)
    # label.image = obj
    # label.pack()
    canvas = Canvas(root, width=800, height=500)
    canvas.create_image(100, 100, image = obj)

    canvas.pack()

    root.mainloop()

"""
Displays the object on the screen
"""
def display(object):
    # Image only works for .jpg
    image = Image.open(object)
    photo = ImageTk.PhotoImage(image)

    display_obj(root, photo)

# """
# Animates the selected object with the given action
# """
# def show_action(object, action):
