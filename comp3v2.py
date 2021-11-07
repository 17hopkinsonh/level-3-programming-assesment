"""
    Author: Hayden Hopkinson
    Date started: 4/11/2021
    ver 2 started: 7/11/2021
    description: this component should use the previus two components to create buttons that buy and sell different products
    Version: 2.1
    Improvements since last version: now breaks out of the for statement when
    more products are brought than are left in stock
"""

#libraries

from tkinter import *
from comp1 import *
from comp2 import *
import comp4v2

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


def create_buttons(root, dimentions, products, string_vars, label_widgets):
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
        buttons.append(GUI(root, "Button", 150, 40, int(dimentions[0])/8, int(dimentions[1])/3*2 + (i * 50), "buy product " + products[i].get_name(), color = "white", color2 = "black", function = lambda i = i: buy_button_pressed(i, products, string_vars, label_widgets[0].get())))
        buttons.append(GUI(root, "Button", 150, 40, int(dimentions[0])/8*7, int(dimentions[1])/3*2 + (i * 50), "sell product " + products[i].get_name(), color = "white", color2 = "black", function = lambda i = i: sell_button_pressed(i, products, string_vars, label_widgets[1].get())))


def buy_button_pressed(product_to_buy, products, string_vars, amount):
    """
this function should only be called by the buy button
it takes three parameters:
    i, the position of the button that was pressed
    products, a list of all the products
    string_vars, a list of the StringVars that are displayed on screen 
    """
    for i in range(0, check_input(amount)):
        products[product_to_buy].buy_stock()
        if(products[product_to_buy].get_stock() == 0):
            break
    comp4v2.refresh_display_info(products, string_vars)

def sell_button_pressed(product_to_sell, products, string_vars, amount):
    """
this function should only be called by the sell button
it takes three parameters:
    i, the position of the button that was pressed
    products, a list of all the products
    string_vars, a list of the StringVars that are displayed on screen 
    """
    for i in range(0, int(amount)):
        products[product_to_sell].sell_stock()
        if(products[product_to_sell].get_owned() == 0):
            break
    comp4v2.refresh_display_info(products, string_vars)

def check_input(label_input):
    """
this changes the string parameter label_input into a int,
removing any non-int characters    
    """
    #code from https://www.kite.com/python/answers/how-to-remove-all-non-numeric-characters-from-a-string-in-python
    numeric_string = re.sub("[^0-9]", "", label_input)
    try:
        return int(numeric_string)
    except:
        return 0
    
    
#main

if(__name__ == "__main__"):
    print("")
