"""
FILENAME: plotter.py
"""

import time
from data_utilities import *
from canvas_utilities import *

CHANGE_OF_X = 5
CHANGE_OF_Y = 0


def plot_trend(canvas, arrow, data_list, date_list, case_text, death_text):
    """
    Plots both graphs based on the progress of the day and data from the lists
    until th arrow is within the meter frame (i.e. maximum date is 24 May 2020)
    """
    total_cases = 0
    total_deaths = 0

    while get_left_x(canvas, arrow) < 904:
        arrow_left_x = get_left_x(canvas, arrow)
        canvas.move(arrow, CHANGE_OF_X, CHANGE_OF_Y)
        canvas.update()
        current_day = (arrow_left_x - 404) // 5
        new_cases = int(data_list[int((current_day * 2))])
        new_deaths = int(data_list[int((current_day * 2) + 1)])
        total_cases += new_cases
        total_deaths += new_deaths
        updated_x_cases = current_day*6 + 35
        updated_y_cases = 700 - total_cases + new_cases
        updated_x_deaths = current_day*6 + 715
        updated_y_deaths = 700 - (total_deaths - new_deaths) * 180
        canvas.create_oval((current_day + 1) * 6 + 33, 698 - total_cases, (current_day + 1) * 6 + 37,
                           702 - total_cases, fill='blue')
        if current_day != 0:
            canvas.create_line(updated_x_cases, updated_y_cases, (current_day + 1) * 6 + 35, 700 - total_cases,
                               fill='blue', width=1)
            canvas.itemconfig(date_text, fill='orange')
            date_text = canvas.create_text(775, 90, anchor='nw', font='Times',
                                           text=date_list[int(current_day)] + ', 2020')
        else:
            canvas.create_line(current_day * 6 + 35, 700, (current_day + 1) * 6 + 35, 700 - total_cases,
                               fill='blue', width=1)
            date_text = canvas.create_text(775, 90, anchor='nw', font='Times',
                                           text=date_list[int(current_day)] + ', 2020')
        canvas.create_oval((current_day + 1) * 6 + 713, 698 - total_deaths * 180, (current_day + 1) * 6 + 717,
                           702 - total_deaths * 180, fill='red')
        if current_day != 0:
            canvas.create_line(updated_x_deaths, updated_y_deaths, (current_day + 1) * 6 + 715,
                               700 - total_deaths * 180, fill='red', width=1)
        else:
            canvas.create_line(current_day * 6 + 715, 700, (current_day + 1) * 6 + 715,
                               700 - total_deaths * 180, fill='red', width=1)
        canvas.itemconfig(case_text, fill='white')
        canvas.itemconfig(death_text, fill='white')
        case_text, death_text = update_data_graph(canvas, total_cases, total_deaths)
        time.sleep(1/4)
    canvas.mainloop()