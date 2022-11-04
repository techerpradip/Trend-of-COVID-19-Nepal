"""
FILENAME: canvas.py
"""

import tkinter
from PIL import ImageTk
from PIL import Image


def make_canvas(width, height, title=None):
    """
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width+2, height=height+2)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas


def decorate_canvas(canvas, width, height):
    """
    Adds required elements to the canvas as required including heading and
    progress meter as we move along in the data.
    """

    # Creates a border to the canvas.
    border_width = 4
    canvas.create_rectangle(0, 0, width, height, fill="chartreuse")
    canvas.create_rectangle(border_width, border_width, width - border_width, height - border_width, fill="white")

    # Designs the top view of the canvas for plots/canvas heading.
    canvas.create_rectangle(485, 10, 860, 28, outline='red', fill='yellow')
    # Heading of the canvas.
    canvas.create_text(490, 10, anchor='nw', font='Times', text='TREND OF C0VID - 19 IN NEPAL TILL 24 MAY, 2020')

    # creates a meter frame to show progress of time.
    canvas.create_rectangle(400, 38, 944, 76, outline='orange', fill='white', width=2)
    canvas.create_text(395, 57, anchor='e', font='times', text='FEB 15, 2020')
    canvas.create_text(949, 57, anchor='w', font='times', text='MAY 24, 2020')

    # rectangle to display the current day.
    canvas.create_rectangle(730, 85, 930, 115, fill='orange')

