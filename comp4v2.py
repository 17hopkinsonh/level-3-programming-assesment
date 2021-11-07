"""
    Author: Hayden Hopkinson
    Date started: 5/11/2021
    description: 
    Version: 1.1
    Improvements since last version: added stuff to make the buttons work with comp3.1

"""

#libraries

from comp3v2 import *


#classes

#functions

def setup_root(width, height):
    root = Tk()
    root.title("Title Here")
    root.geometry(width + "x" + height)
    return root

def setup_UI(root, width, height, label_widgets):
    product_names = ["keyboards", "monitors", "mouses"]
    product_descriptions = ["you use these to type", "you need this to see what you're doing", "you need this to move the curser"]
    products = create_products(product_names, product_descriptions)
    
    string_vars = create_display_info(root, (width, height), products)
    create_buttons(root, (width, height), products, string_vars, label_widgets)
    

def create_display_info(root, dimentions, products):
    string_vars = [StringVar(), [], [], [], [], []]
    GUI(root, "Label", 120, 40, int(dimentions[0])/2, int(dimentions[1])/8, textvar = string_vars[0])
    for i in range(0, len(products)):
        for i2 in range(len(string_vars)-1):
            string_vars[1+i2].append(StringVar())
            GUI(root, "Label", 120, 40, int(dimentions[0])/8*(2+i2), int(dimentions[1])/3*2 + (i * 50), textvar = string_vars[i2+1][i])

    string_vars = refresh_display_info(products, string_vars)
    return string_vars

def refresh_display_info(products, string_vars):
    display_texts = string_vars
    display_texts[0].set("You have {} tokens".format(product.money))
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
