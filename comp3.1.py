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
    """
this function creates and returns two entry boxes (in a list),
two parameters are needed:
    root, the parent that the entry boxes should be placed on
    dimentions, which should be a tuple/list with width at position 0, and height at position 1
    """
    entries = []
    entries.append(GUI(root, "Entry", 150, 40, int(dimentions[0])/8, int(dimentions[1])/3*2 - 50, text = "enter amount to buy:"))
    entries.append(GUI(root, "Entry", 150, 40, int(dimentions[0])/8*7, int(dimentions[1])/3*2 - 50, text = "enter amount to sell:"))
    return entries

#main

if(__name__ == "__main__"):
    #testing
    width = "1000"
    height = "600"

    root = setup_root(width, height)

    entries = create_entries(root, (width, height))
    widgets = []

    for i in range(0, len(entries)):
        widgets.append(entries[i].get_widget())

    product_names = ["keyboards", "monitors", "mouses"]
    product_descriptions = ["you use these to type", "you need this to see what you're doing", "you need this to move the curser"]
    
    setup_UI(root, width, height, widgets, product_names, product_descriptions)
