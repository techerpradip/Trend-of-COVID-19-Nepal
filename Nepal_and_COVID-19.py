"""
File name : Nepal_and_COVID-19.py
Now corona virus has taken it's rapid increasing way in Nepal.
This program plots the graph of total cases and total deaths of COVID - 19 in Nepal
as a function of the days.
"""

from canvas import *
from plotter import *

CANVAS_WIDTH = 1345
CANVAS_HEIGHT = 725
DATA_FILE_NAME = "files/Nepal_COVID19_Data.txt"
DATE_FILE_NAME = "files/Dates.txt"


def main():
    # Creates main working canvas.
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'NEPAL AND COVID - 19')

    # adds required element to the canvas.
    decorate_canvas(canvas, CANVAS_WIDTH, CANVAS_HEIGHT)

    # adds flag of Nepal to the canvas.c
    flag_image = ImageTk.PhotoImage(Image.open("images/flag.png"))
    canvas.create_image(1237, 10, anchor="nw", image=flag_image)
    # adds map of Nepal to the canvas.
    map_image = ImageTk.PhotoImage(Image.open("images/map.jpg"))
    canvas.create_image(8, 10, anchor="nw", image=map_image)

    # adds arrow as a meter to animate the progress of the day.
    arrow_image = ImageTk.PhotoImage(Image.open("images/arrow.png"))
    arrow = canvas.create_image(404, 42, anchor='nw', image=arrow_image)

    # gets the data list and stores it.
    data_list = get_data_list(DATA_FILE_NAME)

    # gets the date list and stores it.
    date_list = get_date_list(DATE_FILE_NAME)

    # Creates two empty graphs for total deaths and total cases.
    create_empty_graphs(canvas)

    # Creates the legend to indicate number of cases and death data.
    data_indicator_legend(canvas)

    # total cases and deaths before the start of program are 0.
    total_cases = 0
    total_deaths = 0

    case_text, death_text = update_data_graph(canvas, total_cases, total_deaths)

    # plots the data in the list to show a trend of COVID-19.
    plot_trend(canvas, arrow, data_list, date_list, case_text, death_text)


if __name__ == '__main__':
    main()
