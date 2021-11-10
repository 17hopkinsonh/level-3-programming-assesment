"""
    Author: Hayden Hopkinson
    Date started: 8/11/2021
    description: combined all the components into one file
    Trial: 2 
    Trial changes: this should only display the buttons/information for the image being currently 
"""

#libraries

from tkinter import *
import random, os, webbrowser, threading


#classes

class GUI:
    #create a static variable, meaning that all instances of this class use the same variable    
    current_img = 0

    def __init__(self, parent, graphic_type, width, height, x_placement, y_placement, text = "", color = None, color2 = None, function = "", textvar = "", image = ""):
        
        self._type = graphic_type
        self._parent = parent
        self._text = text
        self._dimentions = (width, height)
        self._location = (x_placement, y_placement)
        self._function = function
        self._textvar = textvar
        self._colors = (color, color2)

        #if the type provided was a Photoimage, create a Photoimage with the provided file, and then make a label that displays the photoimage
        if(self._type == "PhotoImage"):
            self._image = PhotoImage(file = image)
            self._widget = Label(self._parent, image = self._image)
        else:
            #if a TextVar was not provided set the text to be the provided text, else a TextVar must've been provided, set the textvariable to be the provided TextVar
            #the difference between using a textvar or a text is that the textvar can be more easily updated later on,
            #as if the text stored in the TextVar is updated, the displayed text will also change
            if self._textvar == "":
                #eval is used here to change the provided graphic_type from a string to code,
                #for example if "Label" was passed as the graphic type the code runs Label(self._parent, text = self._text)
                self._widget = eval(check_type(self._type))(self._parent, text = self._text)
            else:
                self._widget = eval(check_type(self._type))(self._parent, textvariable = self._textvar)
        #place the widget at the provided location, with the provided width and height, anchored at the centre northmost point of the widget 
        self._widget.place(anchor = N, width = self._dimentions[0], height = self._dimentions[1], x = self._location[0], y = self._location[1])

        #if the provided type was a button it needs to be configured to be able to run a command when it is pressed
        if(self._type == "Button"):
            self._widget.config(command = self._function, bg = self._colors[0], activebackground = self._colors[1])
        #if the provided type was an entry box then setting the text needs to be done differently
        elif (self._type == "Entry"):
            self._widget.insert(END, self._text)

    def __repr__(self):
        return "this is a {} type of widget with the dimentions {} by {}, placed at {}, {},".format(self._type, self._dimentions[0], self._dimentions[1], self._location[0], self._location[1]) + (" its defaut text is {}".format(self._text) if self._text != "" else "it has no default text") + (". it has a main color of {} and a secondary color of {}".format(self._colors[0], self._colors[1]) if self._colors[0] != None else ". it isn't colored")

    def get_img(self):
        return self._image

    def get_widget(self):
        return self._widget

    def get_img_value():
        return GUI.current_img

    def set_img_value(new_img):
        GUI.current_img = new_img


class Product:
    #create a static variable, meaning that all instances of this class use the same variable
    money = 10000
    
    def __init__(self, name, description, starting_price = 0, starting_stock = 0):
        self._name = name
        self._desc = description
        self._total_sold = 0
        self._total_brought = 0
        self._amount_owned = 0
        #if no starting price was given, randomize it, else set the price to be the price that was provided.
        #Then do the same thing for the starting stock
        if(starting_price != 0):
            self._price = starting_price
        else:
            self._price = random.randint(10,30)
        if(starting_stock != 0):
            self._stock = starting_stock
        else:
            self._stock = random.randint(3,7)

    def __repr__(self):
        return "This product has the name {}, is described as {}, has a current price of {} and has been brought {} times and sold {} times".format(self._name, self._desc, self._price, self._total_brought, self._total_sold)

    def get_name(self):
        return self._name

    def set_owned(self, now_owned):
        self._amount_owned = now_owned
        
    def get_owned(self):
        return self._amount_owned

    def set_brought(self, total):
        self._total_brought = total

    def get_brought(self):
        return self._total_brought

    def set_sold(self, total):
        self._total_sold = total

    def get_sold(self):
        return self._total_sold
    
    def set_stock(self, stock):
        self._stock = stock

    def get_stock(self):
        return self._stock

    def set_price(self, price):
        self._price = round(price)

    def get_price(self):
        return self._price

    def randomize_price(self, new_min, new_max):
        new_price = self.get_price() * (random.randint(new_min, new_max)/100)
        if(new_price > 1000):
            new_price = 1000
        elif(new_price == 0):
            new_price = 1
        return new_price

    def buy_stock(self):
        #check to see if the user should be able to buy the product
        if((self.get_stock() >= 1) and (Product.money - self.get_price() >= 0)):
            the_price = self.get_price()
            print("product {} has been purchased for {} tokens".format(self.get_name(), the_price))
            self.set_stock(self.get_stock()-1)
            #self.set_price(self.randomize_price(100, 170))
            self.set_brought(self.get_brought() + 1)
            self.set_owned(self.get_owned() + 1)
            Product.money -= the_price
        else:
            print("the product {} is either out of stock, or you dont have enough tokens to buy it".format(self.get_name()))        
    def sell_stock(self):
        #check to see if the user has any stock to sell
        if(self.get_owned() > 0):
            print("product {} has been sold for {} tokens".format(self.get_name(), self._price))
            self.set_stock(self.get_stock()+1)
            #self.set_price(self.randomize_price(66, 100))
            self.set_sold(self.get_sold()+1)
            self.set_owned(self.get_owned() - 1)
            Product.money += self.get_price()
        else:
            print("you can't sell product {} since you dont own it".format(self.get_name()))


#functions

def check_type(provided_type):
    """
    This function check the type of widget trying to be created, and compares it to a list of widgets that my program accepts.
    This is unnecessary once the project is completed, but may help when developing as it returns a list of accepted types in an error message to the shell 
    """
    accepted_types = ["Button", "Label", "Entry", "PhotoImage"]
    if(provided_type in accepted_types):
        return provided_type
    else:
        #an invalid type was provided, raise an exception that shows the accepted types that are currently accepted
        accepteds = ""
        for i in range(0, len(accepted_types)):
            accepteds = accepteds + " " + accepted_types[i] if i == (len(accepted_types) - 1) else accepteds + " " + accepted_types[i] + ","
        raise Exception("The type provided was not an accepted type, accepted types are:" + accepteds)

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
        products.append(Product(names[i], descriptions[i]))
    return products 


def create_buttons(root, dimentions, products, string_vars, label_widgets, info_labels):
    """
creates the buy and sell buttons for each product using the following parameters:
    root, the canvas to apply the buttons to
    dimentions, tuple/list containing the width and height of the canvas
    products, a list of each of the different products that can be brought/sold
    string_vars, a list of all the different StringVars, should be created with comp4's "create_display_info function"
    """
    buttons = []
    #create and append a buy and sell button for each product to the list of buttons
    #for i in range(0, len(products)):

    buy_string_var = StringVar()
    buy_string_var.set("buy product " + products[0].get_name())
    sell_string_var = StringVar()
    sell_string_var.set("sell product " + products[0].get_name())
    
    buttons.append(GUI(root, "Button", 150, 40, int(dimentions[0])/8, int(dimentions[1])/3*2, textvar = buy_string_var, color = "white", color2 = "black", function = lambda i = i: buy_button_pressed(products, string_vars, label_widgets[0].get(), info_labels)))
    buttons.append(GUI(root, "Button", 150, 40, int(dimentions[0])/8*7, int(dimentions[1])/3*2, textvar = sell_string_var, color = "white", color2 = "black", function = lambda i = i: sell_button_pressed(products, string_vars, label_widgets[1].get(), info_labels)))

    return buttons, [buy_string_var, sell_string_var]

def buy_button_pressed(products, string_vars, amount, info_labels):
    """
this function should only be called by the buy button
it takes three parameters:
    i, the position of the button that was pressed
    products, a list of all the products
    string_vars, a list of the StringVars that are displayed on screen 
    """
    for i in range(0, check_input(amount)):
        products[GUI.get_img_value()].buy_stock()
        if(products[GUI.get_img_value()].get_stock() == 0):
            break
    refresh_display_info(products, string_vars, info_labels)

def sell_button_pressed(products, string_vars, amount, info_labels):
    """
this function should only be called by the sell button
it takes three parameters:
    i, the position of the button that was pressed
    products, a list of all the products
    string_vars, a list of the StringVars that are displayed on screen 
    """
    for i in range(0, check_input(amount)):
        products[GUI.get_img_value()].sell_stock()
        if(products[GUI.get_img_value()].get_owned() == 0):
            break
    refresh_display_info(products, string_vars, info_labels)

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
also returns a list of the products that were created using the product_names and product_descriptions parameters
    """
    products = create_products(product_names, product_descriptions)
    
    string_vars, info_labels = create_display_info(root, (width, height), products)


    buttons, button_strings = create_buttons(root, (width, height), products, string_vars, label_widgets, info_labels)

    refresh_buttons(products, button_strings, buttons, string_vars, label_widgets, info_labels)
    
    return [products, string_vars, button_strings, buttons, info_labels]
    

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
    GUI(root, "Label", 120, 40, int(dimentions[0])/2, 0, textvar = string_vars[0])
    info_labels = []
    for i2 in range(len(string_vars)-1):
        for i in range(0, len(products)):
            #for each StringVar excluding the first (the first one displays the amount of credits the user has)
            #append a StringVar to the list inside the string_vars list at position i2+1
            string_vars[i2+1].append(StringVar())
        info_labels.append(GUI(root, "Label", 120, 40, int(dimentions[0])/8*(2+i2), int(dimentions[1])/3*2, textvar = string_vars[i2+1][0]))

    #since all the string_vars currently have no text, update them
    string_vars = refresh_display_info(products, string_vars, info_labels)
    return string_vars, info_labels

def refresh_display_info(products, string_vars, info_labels):
    """
this function should update each of the label's StringVars containing information, setting their text to be up-to-date
takes two parameters:
    products, a list of products that has been made, this should've been made with the create_products() function
    string_vars, a list of all the StringVars that needs to be updated, this should've been made with the create_display_info() function
    """   
    display_texts = string_vars
    #at position 0 of the string_vars list there should be a StringVar, update this StringVar to display the amount of tokens the user currently has
    display_texts[0].set("You have {} tokens".format(Product.money))
    #at positions 1-5 of the string_vars list there should be a list of StringVars,
    #each of these lists should have a length of however many products there are.
    #update each of these StringVars to have the relevent information
    for i in range(len(products)):
        display_texts[1][i].set("total brought: " + str(products[i].get_brought()))
        display_texts[2][i].set("stock remaining: " + str(products[i].get_stock()))
        display_texts[3][i].set("price: " + str(products[i].get_price())+ " tokens")
        display_texts[4][i].set("amount owned: " + str(products[i].get_owned()))
        display_texts[5][i].set("total sold: " + str(products[i].get_sold()))

    update_info_labels(info_labels, products, display_texts)
    return display_texts

def update_info_labels(info_labels, products, string_vars):
    """

    """
    info_labels[0].get_widget().config(textvariable = string_vars[1][GUI.get_img_value()])
    info_labels[1].get_widget().config(textvariable = string_vars[2][GUI.get_img_value()])
    info_labels[2].get_widget().config(textvariable = string_vars[3][GUI.get_img_value()])
    info_labels[3].get_widget().config(textvariable = string_vars[4][GUI.get_img_value()])
    info_labels[4].get_widget().config(textvariable = string_vars[5][GUI.get_img_value()])




def refresh_buttons(products, button_strings, buttons, string_vars, label_widgets, info_labels):
    """

    """
    #product_to_buy, products, string_vars, amount
    buttons[0].get_widget().config(command = lambda: buy_button_pressed(products, string_vars, label_widgets[0].get(), info_labels))
    button_strings[0].set("buy product " + products[GUI.get_img_value()].get_name())
    buttons[1].get_widget().config(command = lambda: sell_button_pressed(products, string_vars, label_widgets[1].get(), info_labels))
    button_strings[1].set("sell product " + products[GUI.get_img_value()].get_name())
    

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


def get_images():
    """
gets and returns a list of images that are stored in the same filepath as this file 
    """
    images = []

    #get a list of every file stored in the same filepath as this
    for file in os.listdir():
        #check that the file ends in .png and is not the image i had used for testing
        if(file.endswith(".png") and file != "testing.png"):
            images.append(file)

    return images


def create_gallery(root, images, links, resolution, products, string_vars, button_strings, label_widgets, info_labels):
    """
creates the image, credit button, and buttons to scroll throught the images
takes four parameters:
    root, the parent window to assign the GUI objects to
    images, a list of images to display
    links, a list of links to the website where the related image is from
    resolution, a tuple/list with the width of the root at index 0, and the height of the root at index 1
    """
    image_widget = create_image(root, images[0], links[0], resolution)
    buttons = create_gallery_buttons(root, images, resolution, links, image_widget, products, string_vars, button_strings, label_widgets, info_labels)
    return (image_widget, buttons)


def create_image(root, default_img, default_link, res):
    """
this function creates the image, and the button that links to the source of the image, returning them in a list.
this takes four parameters:
    root, the parent window to assign the GUI objects to
    default_img, the first image in alphabetical order, will be the first image displayed when the program is run
    default_link, the first link parallel to the images, will be the first assigned link when the program is run
    res, a tuple/list with the width of the root at index 0, and the height of the root at index 1
    """
    image = GUI(root, "PhotoImage", 300, 200, int(res[0])/2, int(res[1])/18, image = default_img)
    credit_button = GUI(root, "Button", 300, 50, int(res[0])/2, int(res[1])/18+200, text = "image source", function = lambda: open_page(default_link))
    return [image, credit_button]


def create_gallery_buttons(root, images, res, links, img_widget, products, string_vars, button_strings, label_widgets, info_labels):
    """
this function should create the left and right buttons used to scroll through the images
it takes five parameters:
    root, the parent window to assign the GUI objects to
    images, a list of all the images for each product
    res, a tuple/list with the width of the root at index 0, and the height of the root at index 1
    links, a list of links to the website where the related image is from
    img_widget, a list containing the label widget that displays the image, and the button widget that links to the source of the image
    """
    buttons = []
    buttons.append(GUI(root, "Button", 100, 80, int(res[0])/2-50, int(res[1])/18 + 250, text = "<---", function = lambda: choose_img(images, links, img_widget, False, products, string_vars, button_strings, label_widgets, info_labels)))
    buttons.append(GUI(root, "Button", 100, 80, int(res[0])/2+50, int(res[1])/18 + 250, text = "--->", function = lambda: choose_img(images, links, img_widget, True, products, string_vars, button_strings, label_widgets, info_labels)))


def choose_img(images, links, img_widget, foward, products, string_vars, button_strings, label_widgets, info_labels):
    """
this function should decide what image should be displayed, and then call the function change_img to change the image to the new one
this takes four functions:
    images, a list of all the images for each product
    links, a list of links to the website where the related image is from
    img_widget, a list containing the label widget that displays the image, and the button widget that links to the source of the image
    foward, (bool), should be True if going foward through the images, False if backwards
    """
    new_num = GUI.get_img_value() + (1 if foward else -1)
    #if the absolute (positive) length of the old value is equal to the length of the images list then the end of the list was reached and the value should reset to zero
    if(abs(new_num) == len(images)):
        GUI.set_img_value(0)
        change_img(img_widget, images[0], links[0])
    else:
        GUI.set_img_value(new_num)
        change_img(img_widget, images[new_num], links[new_num])
    refresh_display_info(products, string_vars, info_labels)
    refresh_buttons(products, button_strings, buttons, string_vars, label_widgets, info_labels)

def change_img(img_widget, image, link):
    """
this function should change the label widget with the image to display the new image and update the link to take the user to the new reference when clicked 
takes three parameters:
    img_widget, a list containing the label widget that displays the image, and the button widget that links to the source of the image
    image, the name of the new image to display
    link, the new link of the website that the button should take the user to 
    """
    img_widget[0].get_img().config(file = image)
    img_widget[1].get_widget().config(command = lambda: open_page(link))


def open_page(page_to_open):
    """
this component should take the user to a specified webpage
it takes one parameter:
    page_to_open, the link to the webpage that should be opened
    """
    webbrowser.open(page_to_open)

def repeat(products, string_vars, seconds, info_labels):
    """
this function repeats certain code on a timer, it takes three parameters:
products, a list of all the products
string_vars, a list of all the StringVars, needed for refreashing the display
seconds, the time, in seconds, that the function should wait before repeating
    """
    for i in products:
        i.set_price(i.randomize_price(66, 150))
    refresh_display_info(products, string_vars, info_labels)
    threading.Timer(seconds, lambda:repeat(products, string_vars, seconds, info_labels)).start()


#main

if(__name__ == "__main__"):
    width = "1000"
    height = "600"

    widgets = []

    links = [
    "https://publicdomainvectors.org/en/free-clipart/Vector-graphics-of-AZERTY-computer-keyboard/13672.html",
    "https://publicdomainvectors.org/en/free-clipart/LCD-screen-with-shadow-vector-graphics/13214.html",
    "https://publicdomainvectors.org/en/free-clipart/Photorealistic-vector-image-of-computer-mouse/12989.html"
    ]

    #these need to be in alphabetical order as that's the order the image files will be pulled
    product_names = ["keyboards", "monitors", "mouses"]
    #these were never used, it should be parallel with the product_names list, but as long as its a list of string and has the same length as the products name list it shouldn't result in errors
    product_descriptions = ["you use these to type", "you need this to see what you're doing", "you need this to move the curser"]
    
    root = setup_root(width, height)
    entries = create_entries(root, (width, height))
    for i in range(0, len(entries)):
        widgets.append(entries[i].get_widget())

    products, string_vars, button_strings, buttons, info_labels = setup_UI(root, width, height, widgets, product_names, product_descriptions)
    
    gallery = create_gallery(root, get_images(), links, (width, height), products, string_vars, button_strings, widgets, info_labels)

    repeat(products, string_vars, 2, info_labels)

    root.mainloop()
