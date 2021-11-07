"""
    Author: Hayden Hopkinson
    Date started: 4/11/2021
    description: this component should use the previus two components to create buttons that buy and sell different products
    Version: 1.1
    Improvements since last version: some additional things were aded to support comp4
"""

#libraries

from tkinter import *
from comp1 import *
from comp2 import *
from comp4 import *
#classes

#functions

def create_products(names, descriptions):
    """
creates and returns a list of products,
takes two parameters:
    names, which should be a list of each products name
    descriptions, which should be a list of each products description
these should be parallel lists of the same length
    """

    #if the lengths of the lists were different raise an exception
    if(len(names) != len(descriptions)):
        raise Exception("Lists of different lengths were given")

    products = []
    for i in range(0, len(names)):
        products.append(product(names[i], descriptions[i]))
    return products 


def create_buttons(root, dimentions, products, string_vars):
    """
creates the buy and sell buttons for each product using the following parameters:
    root, the canvas to apply the buttons to
    dimentions, tuple/list containing the width and height of the canvas
    products, a list of each of the different products that can be brought/sold
    string_vars, a list of all the different StringVars, should be created with comp4's "create_display_info function"
    """
    buttons = []
    #create and append a buy and sell button for each product to the list of buttons
    for i in range(0, len(products)):
        buttons.append(GUI(root, "Button", 150, 40, int(dimentions[0])/8, int(dimentions[1])/3*2 + (i * 50), "buy product " + products[i].get_name(), color = "white", color2 = "black", function = lambda i = i: buy_button_pressed(i, products, string_vars)))
        buttons.append(GUI(root, "Button", 150, 40, int(dimentions[0])/8*7, int(dimentions[1])/3*2 + (i * 50), "sell product " + products[i].get_name(), color = "white", color2 = "black", function = lambda i = i: sell_button_pressed(i, products, string_vars)))


def buy_button_pressed(i, products, string_vars):
    """
this function should only be called by the buy button
it takes three parameters:
    i, the position of the button that was pressed
    products, a list of all the products
    string_vars, a list of the StringVars that are displayed on screen 
    """
    products[i].buy_stock()
    refresh_display_info(products, string_vars)

def sell_button_pressed(i, products, string_vars):
    """
this function should only be called by the sell button
it takes three parameters:
    i, the position of the button that was pressed
    products, a list of all the products
    string_vars, a list of the StringVars that are displayed on screen 
    """
    products[i].sell_stock()
    refresh_display_info(products, string_vars)
    
#main

if(__name__ == "__main__"):
    print("")
