"""
FILENAME: canvas_utilities.py
"""

GRAPH_GAP = 45


def get_left_x(canvas, canvas_object):
    """
    Returns the x coordinate of the left side of given shape in canvas.
    """
    return canvas.coords(canvas_object)[0]


def create_empty_graphs(canvas):
    """
        Creates two empty graphs for total deaths and total cases.
    """
    for i in range(2):
        canvas.create_line(35 + (635 + GRAPH_GAP) * i, 700, 635 + (635 + GRAPH_GAP) * i, 700)
        canvas.create_line(35 + (635 + GRAPH_GAP) * i, 700, 35 + (635 + GRAPH_GAP) * i, 95)
        canvas.create_line(635 + (635 + GRAPH_GAP) * i, 700, 625 + (635 + GRAPH_GAP) * i, 690)
        canvas.create_line(635 + (635 + GRAPH_GAP) * i, 700, 625 + (635 + GRAPH_GAP) * i, 710)
        canvas.create_line(35 + (635 + GRAPH_GAP) * i, 95, 25 + (635 + GRAPH_GAP) * i, 105)
        canvas.create_line(35 + (635 + GRAPH_GAP) * i, 95, 45 + (635 + GRAPH_GAP) * i, 105)
        for j in range(100):
            canvas.create_line(35 + 6 * (j + 1) + (635 + GRAPH_GAP) * i, 698, 35 + 6 * (j + 1) + (635 + GRAPH_GAP) * i,
                               702)
        for j in range(3):
            canvas.create_line(35 + (635 + GRAPH_GAP) * i, 700 - (180 * (j + 1)), 635 + (635 + GRAPH_GAP) * i,
                               700 - (180 * (j + 1)))
        canvas.create_text(32 + (635 + GRAPH_GAP) * i, 700, anchor='e', font='Times', text='0')

    # Displays the X-axis division names of the graphs in the canvas.
    for i in range(2):
        canvas.create_text(41 + 680 * i, 704, anchor='n', font='Times', text='Feb15')
        canvas.create_text(113 + 680 * i, 704, anchor='n', font='Times', text='Feb26')
        canvas.create_text(191 + 680 * i, 704, anchor='n', font='Times', text='Mar10')
        canvas.create_text(263 + 680 * i, 704, anchor='n', font='Times', text='Mar22')
        canvas.create_text(341 + 680 * i, 704, anchor='n', font='Times', text='Apr04')
        canvas.create_text(413 + 680 * i, 704, anchor='n', font='Times', text='Apr16')
        canvas.create_text(491 + 680 * i, 704, anchor='n', font='Times', text='Apr29')
        canvas.create_text(563 + 680 * i, 704, anchor='n', font='Times', text='May11')
        canvas.create_text(641 + 677 * i, 704, anchor='n', font='Times', text='May24')

    # displays the division of graph by 3 lines each at a distance of 180 pixels from each other.
    for i in range(3):
        num1 = 180 * (i + 1)
        canvas.create_text(32, 700 - (180 * (i + 1)), anchor='e', font='Times', text=str(num1))
    for i in range(3):
        num2 = (i + 1)
        canvas.create_text(712, 700 - (180 * (i + 1)), anchor='e', font='Times', text=str(num2))
