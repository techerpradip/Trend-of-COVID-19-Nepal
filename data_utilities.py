"""
FILENAME: data_utilities.py
"""


def get_data_list(file_name):
    """
    Returns a list consisting of data of cases and deaths due to COVID - 19
    in different dates.
    """
    with open(file_name, 'r') as file:
        data_list = []
        for line in file:
            line = line.strip()
            data_list += line.split()
    return data_list


def get_date_list(file_name):
    """
    Returns a list consisting of the dates that are recorded in the graph.
    """
    with open(file_name, 'r') as file:
        date_list = []
        for line in file:
            line = line.strip()
            date_list += line.split()
    return date_list


def data_indicator_legend(canvas):
    """
    Creates a legend for the total-cases and total-deaths graphs.
    """

    # Displays the total cases up-to the date and indicates the color used to indicate cases in the graph.
    canvas.create_oval(314, 134, 326, 146, fill='blue')
    canvas.create_text(330, 140, anchor='w', font='Times', text='Total Cases = ')

    # Displays the total deaths up-to the date and indicates the color used to indicate cases in the graph.
    canvas.create_oval(994, 134, 1006, 146, fill='red')
    canvas.create_text(1010, 140, anchor='w', font='Times', text='Total Deaths = ')


def update_data_graph(canvas, total_cases, total_deaths):
    """
    Displays data as text in canvas for total cases and total deaths on
    to of respective graphs, when we progressively move forward.
    """
    case_text = canvas.create_text(420, 140, anchor='w', font='Times', text=str(total_cases), fill='blue')
    death_text = canvas.create_text(1105, 140, anchor='w', font='Times', text=str(total_deaths), fill='red')
    return case_text, death_text
