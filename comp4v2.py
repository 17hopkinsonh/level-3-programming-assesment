"""
    Author: Hayden Hopkinson
    Date started: 5/11/2021
    description: description: this component should create the labels that have information on each of the products
    Version: 1.1
    Improvements since last version: added stuff to make the buttons work with comp3.1

"""

#libraries

from comp3v2 import *


#classes

#functions

def setup_root(width, height):
    """
this function should create and return a tkinter window, it takes two parameters:
    width, the width that the tkinter window should take
    height, the height that the tkinter window should take
    """
    root = Tk()
    #set the title of the window
    root.title("Shop Program")
    #set the size of the window to the provided width and height
    root.geometry(width + "x" + height)
    return root

def setup_UI(root, width, height, label_widgets, product_names, product_descriptions):
    """
this function calls several other components, this should create a majority of the UI
takes six functions:
    root, the parent window to assign the GUI objects to
    width, width of the parent window
    height, height of the parent window
    label_widgets, a list of the label widgets that should have text containing the amount of products to buy/sell at a time
    product_names, a list containing names of each of the products
    product_descriptions, a list of descriptions for each product, should be parallel to the product_names list
    """
    products = create_products(product_names, product_descriptions)
    
    string_vars = create_display_info(root, (width, height), products)
    create_buttons(root, (width, height), products, string_vars, label_widgets)
    

def create_display_info(root, dimentions, products):
    """
this function should create several labels for each product,
each label containing informataion relating to the product, such as total amount brought, stock available, ect
takes three functions:
    root, the parent window to assign the labels objects to
    dimentions, a tuple/list that contains the width of the root at index 0, and the height of the root at index 1
    products, a list of all the products this function should create information about, this should've been made with the create_products() function
it returns a list containing all of the StringVars
    """
    string_vars = [StringVar(), [], [], [], [], []]
    GUI(root, "Label", 120, 40, int(dimentions[0])/2, int(dimentions[1])/8, textvar = string_vars[0])
    
    for i in range(0, len(products)):
        #for each product
        for i2 in range(len(string_vars)-1):
            #for each StringVar excluding the first (the first one displays the amount of credits the user has)
            #append a StringVar to the list inside the string_vars list at position i2+1
            string_vars[i2+1].append(StringVar())
            #create a label using the StringVar that was just created as the textvar
            GUI(root, "Label", 120, 40, int(dimentions[0])/8*(2+i2), int(dimentions[1])/3*2 + (i * 50), textvar = string_vars[i2+1][i])

    #since all the string_vars currently have no text, update them
    string_vars = refresh_display_info(products, string_vars)
    return string_vars

def refresh_display_info(products, string_vars):
    """
this function should update each of the label's StringVars containing information, setting their text to be up-to-date
takes two parameters:
    products, a list of products that has been made, this should've been made with the create_products() function
    string_vars, a list of all the StringVars that needs to be updated, this should've been made with the create_display_info() function
    """
    display_texts = string_vars
    #at position 0 of the string_vars list there should be a StringVar, update this StringVar to display the amount of tokens the user currently has
    display_texts[0].set("You have {} tokens".format(product.money))
    #at positions 1-5 of the string_vars list there should be a list of StringVars,
    #each of these lists should have a length of however many products there are.
    #update each of these StringVars to have the relevent information
    for i in range(len(products)):
        display_texts[1][i].set("total brought: " + str(products[i].get_brought()))
        display_texts[2][i].set("stock remaining: " + str(products[i].get_stock()))
        display_texts[3][i].set("price: " + str(products[i].get_price())+ " tokens")
        display_texts[4][i].set("amount owned: " + str(products[i].get_owned()))
        display_texts[5][i].set("total sold: " + str(products[i].get_sold()))
        
    return display_texts


#main

if(__name__ == "__main__"):
    #if you're here to try to test this component go to the file named comp4
    print("")
