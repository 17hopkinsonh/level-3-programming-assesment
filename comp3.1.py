"""
    Author: Hayden Hopkinson
    Date started: 7/11/2021
    description: this component should create entry boxes that change the amount of product being brought at once
    Version: 1
    Improvements since last version: N/A

"""

#libraries



from comp4v2 import *


#classes

#functions

def create_entries(root, dimentions):
    entries = []
    entries.append(GUI(root, "Entry", 150, 40, int(dimentions[0])/8, int(dimentions[1])/3*2 - 50, text = "enter amount to buy:"))
    entries.append(GUI(root, "Entry", 150, 40, int(dimentions[0])/8*7, int(dimentions[1])/3*2 - 50, text = "enter amount to sell:"))
    return entries

#main

if(__name__ == "__main__"):

    width = "1000"
    height = "600"

    root = setup_root(width, height)

    entries = create_entries(root, (width, height))
    widgets = []

    for i in range(0, len(entries)):
        widgets.append(entries[i].get_widget())

    setup_UI(root, width, height, widgets)
