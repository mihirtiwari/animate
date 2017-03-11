import Tkinter as tk
from Tkinter import Label
# from PIL import Image, ImageTk

root = tk.Tk()

def display_obj(root, obj):
    w = Label(root, text=str(obj))
    w.pack()

    root.mainloop()

"""
Displays the object on the screen
"""
def display(object):
    display_obj(root, object)

# """
# Animates the selected object with the given action
# """
# def show_action(object, action):
