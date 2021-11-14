"""
    Author: Hayden Hopkinson
    Date started: 8/11/2021
    description: combined all the components into one file, then made improvements based on user testing
    Version: 1.1
    Improvements since last version: Now uses constants in place of most magic numbers, also added extra comments

"""

#libraries
from tkinter import *
from tkinter import messagebox
import random, os, webbrowser, threading, re

#classes

class GUI:
    #create a static variable, whenever/wherever "GUI.current_img" is referenced this will be returned    
    current_img = 0

    def __init__(self, parent, graphic_type, width, height, x_placement, y_placement, text = "", color = None, color2 = None, function = "", text_var = "", image = ""):
        self._type = graphic_type
        self._parent = parent
        self._text = text
        self._dimensions = (width, height)
        self._location = (x_placement, y_placement)
        self._function = function
        self._text_var = text_var
        self._colors = (color, color2)

        #if the type provided was a Photoimage, create a Photoimage with the provided file, and then make a label that displays the photoimage
        if(self._type == "PhotoImage"):
            self._image = PhotoImage(file = image)
            self._widget = Label(self._parent, image = self._image)
        else:
            #if a TextVar was not provided set the text to be the provided text, else a TextVar must've been provided, set the textvariable to be the provided TextVar
            #the difference between using a textvar or a text is that the textvar can be more easily updated later on,
            #as if the text stored in the TextVar is updated, the displayed text will also change
            if self._text_var == "":
                #eval is used here to change the provided graphic_type from a string to code,
                #for example if "Label" was passed as the graphic type the code runs Label(self._parent, text = self._text)
                self._widget = eval(check_type(self._type))(self._parent, text = self._text)
            else:
                self._widget = eval(check_type(self._type))(self._parent, textvariable = self._text_var)
        #place the widget at the provided location, with the provided width and height, anchored at the centre northmost point of the widget 
        self._widget.place(anchor = N, width = self._dimensions[0], height = self._dimensions[1], x = self._location[0], y = self._location[1])

        #if the provided type was a button it needs to be configured to be able to run a command when it is pressed
        if(self._type == "Button"):
            self._widget.config(command = self._function, bg = self._colors[0], activebackground = self._colors[1])
        #if the provided type was an entry box then setting the text needs to be done differently
        elif (self._type == "Entry"):
            self._widget.insert(END, self._text)

    def __repr__(self):
        return "this is a {} type of widget with the dimensions {} by {}, placed at {}, {},".format(self._type, self._dimensions[0], self._dimensions[1], self._location[0], self._location[1]) + (" its default text is {}".format(self._text) if self._text != "" else "it has no default text") + (". it has a main color of {} and a secondary color of {}".format(self._colors[0], self._colors[1]) if self._colors[0] != None else ". it isn't colored")

    def get_img(self):
        return self._image

    def get_widget(self):
        return self._widget

    def get_img_value():
        return GUI.current_img

    def set_img_value(new_img):
        GUI.current_img = new_img


class Product:
    #create a static variable, whenever/wherever "Product.tokens" is referenced this will be returned  
    tokens = 100
    
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
            MIN_RAND = 10
            MAX_RAND = 30
            self._price = random.randint(MIN_RAND, MAX_RAND)

        if(starting_stock != 0):
            self._stock = starting_stock
        else:
            MIN_RAND = 5
            MAX_RAND = 10
            self._stock = random.randint(MIN_RAND, MAX_RAND)

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

        MIN_PRICE = 1
        MAX_PRICE = 1000
        
        if(new_price > MAX_PRICE):
            new_price = MAX_PRICE
        elif(new_price < MIN_PRICE):
            new_price = MIN_PRICE
        return new_price

    def buy_stock(self):
        #check to see if the user should be able to buy the product
        if((self.get_stock() >= 1) and (Product.tokens - self.get_price() >= 0)):
            the_price = self.get_price()
            print("product {} has been purchased for {} tokens".format(self.get_name(), the_price))
            self.set_stock(self.get_stock()-1)
            self.set_brought(self.get_brought() + 1)
            self.set_owned(self.get_owned() + 1)
            Product.tokens -= the_price
        else:
            print("the product {} is either out of stock, or you dont have enough tokens to buy it".format(self.get_name()))        
    def sell_stock(self):
        #check to see if the user has any stock to sell
        if(self.get_owned() > 0):
            print("product {} has been sold for {} tokens".format(self.get_name(), self._price))
            self.set_stock(self.get_stock()+1)
            self.set_sold(self.get_sold()+1)
            self.set_owned(self.get_owned() - 1)
            Product.tokens += self.get_price()
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
        for i in range(len(accepted_types)):
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
    for i in range(len(names)):
        products.append(Product(names[i], descriptions[i]))
    return products 


def create_buttons(root, dimensions, products, string_vars, label_widgets):
    """
creates the buy and sell buttons for each product using the following parameters:
    root, the canvas to apply the buttons to
    dimensions, tuple/list containing the width and height of the canvas
    products, a list of each of the different products that can be brought/sold
    string_vars, a list of all the different StringVars, should be created with comp4's "create_display_info" function
    label_widgets, a list containing the widget for the label tkinter object for the buy and sell side
    """
    buttons = []
    BUTTON_WIDTH = 150
    BUTTON_HEIGHT = 40
    GAP = 50
    
    #create and append a buy and sell button for each product to the list of buttons
    for i in range(len(products)):
        #create 2 buttons per product, set their width and height to the respective constants,
        #(x-axis) put the buy button 1/8th across the window, and the sell button at 7/8ths,
        #(y-axis) start putting the buttons at 2/3rds of the height, adding Gap amount of pixels per button thats already been placed
        buttons.append(GUI(root, "Button", BUTTON_WIDTH, BUTTON_HEIGHT, int(dimensions[0])/8, int(dimensions[1])*2/3 + (i * GAP), "Buy product " + products[i].get_name(), color = "white", color2 = "grey", function = lambda i = i: buy_button_pressed(products, i, string_vars, label_widgets[0].get())))
        buttons.append(GUI(root, "Button", BUTTON_WIDTH, BUTTON_HEIGHT, int(dimensions[0])/8*7, int(dimensions[1])*2/3 + (i * GAP), "Sell product " + products[i].get_name(), color = "white", color2 = "grey", function = lambda i = i: sell_button_pressed(products, i, string_vars, label_widgets[1].get())))


def buy_button_pressed(products, product_to_buy, string_vars, amount):
    """
this function should only be called by the buy button
it takes four parameters:
    products, a list of all the products
    product to buy, the position of the product being brought in the products list
    string_vars, a list of the StringVars that are displayed on screen, needed so that they can be updated afterwards
    amount, a string of the amount the user wants to buy
    """
    #remove non-numeric characters from the amount string and convert it into an int
    amount = check_input(amount)
    
    for i in range(amount):
        #if there is no stock remaining display an error message, then break out of the buy loop
        if(products[product_to_buy].get_stock() == 0):
            messagebox.showerror("Error", "There is no remaining stock of that product")
            break
        #or if the user doesnt have enough money to buy the product display a (different) error message, then break out of the buy loop
        elif(Product.tokens - products[product_to_buy].get_price() < 0):
            messagebox.showerror("Error", "You dont have enough tokens")
            break
        #if the program gets to this point then the user should be able to buy a product, do this
        products[product_to_buy].buy_stock()
    #update the stringvars the labels are displaying 
    refresh_display_info(products, string_vars)

def sell_button_pressed(products, product_to_sell, string_vars, amount):
    """
it takes four parameters:
    products, a list of all the products
    product to sell, the position of the product being sold in the products list
    string_vars, a list of the StringVars that are displayed on screen, needed so that they can be updated afterwards
    amount, a string of the amount the user wants to sell
    """
    #remove non-numeric characters from the amount string and convert it into an int
    amount = check_input(amount)
    
    for i in range(amount):
        #if the user is trying to sell a product that they dont own any of then display an error message and break out of the sell loop
        if(products[product_to_sell].get_owned() == 0):
            messagebox.showerror("Error", "You dont have any of that product to sell")
            break
        #if the program gets to this point then the user should be able to sell a product, do this
        products[product_to_sell].sell_stock()
    #update the stringvars the labels are displaying 
    refresh_display_info(products, string_vars)

def check_input(label_input):
    """
this changes the string parameter label_input into a int,
removing any non-int characters
    """
    #code from https://www.kite.com/python/answers/how-to-remove-all-non-numeric-characters-from-a-string-in-python
    numeric_string = re.sub("[^0-9]", "", label_input)

    if(numeric_string == ""):
        messagebox.showerror("error","you need to enter numbers into the text boxes")

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


def setup_UI(root, dimensions, label_widgets, product_names, product_descriptions):
    """
this function calls several other components, this should create a majority of the UI
takes five parameters:
    root, the parent window to assign the GUI objects to
    dimensions, a tuple/list that contains the width of the root at index 0, and the height of the root at index 1
    label_widgets, a list of the label widgets that should have text containing the amount of products to buy/sell at a time
    product_names, a list containing names of each of the products
    product_descriptions, a list of descriptions for each product, should be parallel to the product_names list
also returns a list of the products that were created using the product_names and product_descriptions parameters
    """
    products = create_products(product_names, product_descriptions)
    string_vars = create_display_info(root, dimensions, products)
    
    create_buttons(root, dimensions, products, string_vars, label_widgets)
    
    return [products, string_vars]


def create_display_info(root, dimensions, products):
    """
this function should create several labels for each product,
each label containing informataion relating to the product, such as total amount brought, stock available, ect
takes three functions:
    root, the parent window to assign the labels objects to
    dimensions, a tuple/list that contains the width of the root at index 0, and the height of the root at index 1
    products, a list of all the products this function should create information about, this should've been made with the create_products() function
it returns a list containing all of the StringVars
    """
    LABEL_WIDTH = 120
    LABEL_HEIGHT = 40
    GAP = 50
    
    string_vars = [StringVar(), [], [], [], [], []]
    GUI(root, "Label", LABEL_WIDTH, LABEL_HEIGHT, int(dimensions[0])/2, 0, text_var = string_vars[0])
    
    for i in range(len(products)):
        #for each product
        for i2 in range(len(string_vars)-1):
            #for each StringVar excluding the first (the first one displays the amount of credits the user has)
            #append a StringVar to the list inside the string_vars list at position i2+1
            string_vars[i2+1].append(StringVar())
            #create a label using the StringVar that was just created as the textvar
            #make the label the width and height of the constants,
            #then place them at (2 + i2)/8ths (which should be between 2/8ths and 6/8ths) across the window
            #and 2/3rds + (i * GAP) down the window
            GUI(root, "Label", LABEL_WIDTH, LABEL_HEIGHT, int(dimensions[0])*(2+i2)/8, int(dimensions[1])*2/3 + (i * GAP), text_var = string_vars[i2+1][i])

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
    display_texts[0].set("You have {} tokens".format(Product.tokens))
    #at positions 1-5 of the string_vars list there should be a list of StringVars,
    #each of these lists should have a length of however many products there are.
    #update each of these StringVars to have the relevent information
    for i in range(len(products)):
        display_texts[1][i].set("Total brought: " + str(products[i].get_brought()))
        display_texts[2][i].set("Stock remaining: " + str(products[i].get_stock()))
        display_texts[3][i].set("Price: " + str(products[i].get_price())+ " tokens")
        display_texts[4][i].set("Amount owned: " + str(products[i].get_owned()))
        display_texts[5][i].set("Total sold: " + str(products[i].get_sold()))
        
    return display_texts

def create_entries(root, dimensions):
    """
this function creates and returns two entry boxes (in a list),
two parameters are needed:
    root, the parent that the entry boxes should be placed on
    dimensions, which should be a tuple/list with width at position 0, and height at position 1
    """
    WIDTH = 150
    HEIGHT = 40
    GAP = 10
    
    entries = []

    #create an entry box for buying and selling and append them to the entries list,
    #these should use the height and width constants,
    #the buy entry should be placed 1/8th across the window, while the sell is 7/8ths along
    #they should both be the height + gap constants above 2/3rds of the way down the window
    #also create a label and place it just above the entries, also using the height and width constants for size,
    #placed at the same position on the x-axis
    entries.append(GUI(root, "Entry", WIDTH, HEIGHT, int(dimensions[0])/8, int(dimensions[1])*2/3 - (HEIGHT + GAP)))
    GUI(root, "Label", WIDTH, HEIGHT, int(dimensions[0])/8, int(dimensions[1])/3*2 - (10 + HEIGHT * 2), text = "Enter amount to buy:")
    entries.append(GUI(root, "Entry", WIDTH, HEIGHT, int(dimensions[0])*7/8, int(dimensions[1])*2/3 - (HEIGHT + GAP)))
    GUI(root, "Label", WIDTH, HEIGHT, int(dimensions[0])/8*7, int(dimensions[1])/3*2 - (10 + HEIGHT * 2), text = "Enter amount to sell:")

    return entries


def get_images():
    """
gets and returns a list of images (specifically png's) that are stored in the same filepath as this file 
    """
    images = []

    #get a list of every file stored in the same file path as this, loop over the following code for each file 
    for file in os.listdir():
        #check that the file ends in .png and is not the image I used for testing
        if(file.endswith(".png") and file != "testing.png"):
            #if it does then it must be an image intended for use with this, append it to the images file
            images.append(file)

    return images


def create_gallery(root, images, links, resolution):
    """
creates the image, credit button, and buttons to scroll throught the images
takes four parameters:
    root, the parent window to assign the GUI objects to
    images, a list of images to display
    links, a list of links to the website where the related image is from
    resolution, a tuple/list with the width of the root at index 0, and the height of the root at index 1
    """
    image_widget, gallery_height = create_image(root, images[0], links[0], resolution)
    buttons = create_gallery_buttons(root, images, resolution, links, image_widget, gallery_height)
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

    WIDTH = 300
    PHOTO_HEIGHT = 200
    BUTTON_HEIGHT = 50

    #create an image, using the width and photo_height constants
    #placing it in the middle of the window in terms of x axis, and slightly below (1/18th) the top of the window
    image = GUI(root, "PhotoImage", WIDTH, PHOTO_HEIGHT, int(res[0])/2, int(res[1])/18, image = default_img)
    #then, create a credit button just below the image, using the button_height constant,
    #along with the same width constant, and x-axis placement from making the photo
    credit_button = GUI(root, "Button", WIDTH, BUTTON_HEIGHT, int(res[0])/2, int(res[1])/18 + PHOTO_HEIGHT, text = "Image source", function = lambda: open_page(default_link))
    return [image, credit_button], PHOTO_HEIGHT + BUTTON_HEIGHT


def create_gallery_buttons(root, images, res, links, img_widget, gallery_height):
    """
this function should create the left and right buttons used to scroll through the images
it takes five parameters:
    root, the parent window to assign the GUI objects to
    images, a list of all the images for each product
    res, a tuple/list with the width of the root at index 0, and the height of the root at index 1
    links, a list of links to the website where the related image is from
    img_widget, a list containing the label widget that displays the image, and the button widget that links to the source of the image
    gallery_height, the height (in pixels) of the gellery image and credit button combined
    """
    WIDTH = 150
    HEIGHT = 75
    
    #create the left and right buttons for the gallery
    #they should use the height and width from the respective constants,
    #the left button should be placed at 1/2 the width to the left of the centre,
    #the right button should be placed at 1/2 the width to the right of the centre,
    #on the y-axis both buttons should be placed at 1/18th of the windows height, plus the height of the gallery 
    GUI(root, "Button", WIDTH, HEIGHT, int(res[0])/2 - (WIDTH/2), int(res[1])/18 + gallery_height, text = "<---", function = lambda: choose_img(images, links, img_widget, False))
    GUI(root, "Button", WIDTH, HEIGHT, int(res[0])/2 + (WIDTH/2), int(res[1])/18 + gallery_height, text = "--->", function = lambda: choose_img(images, links, img_widget, True))


def choose_img(images, links, img_widget, foward):
    """
this function should decide what image should be displayed, and then call the function change_img to change the image to the new one
this takes four parameters:
    images, a list of all the images for each product
    links, a list of links to the website where the related image is from
    img_widget, a list containing the label widget that displays the image, and the button widget that links to the source of the image
    foward, (bool), should be True if going foward through the images, False if backwards
    """
    #the new number should be the old number plus one if it was the foward button pressed
    #or the old number minus one if the back button was pressed
    new_num = GUI.get_img_value() + (1 if foward else -1)
    #if the absolute (positive) length of the old value is equal to the length of the images list then the end of the list was reached and the value should reset to zero
    if(abs(new_num) == len(images)):
        print("the index of the currently displayed image is " + str(0))
        #set the static variable of the class GUI to 0
        GUI.set_img_value(0)
        change_img(img_widget, images[0], links[0])
    else:
        print("the index of the currently displayed image is " + str(new_num))
        #set the static variable of the class GUI to the value of new_num
        GUI.set_img_value(new_num)
        change_img(img_widget, images[new_num], links[new_num])
        

def change_img(img_widget, image, link):
    """
this function should change the label widget with the image to display the new image and update the link to take the user to the new reference when clicked 
takes three parameters:
    img_widget, a list containing the label widget that displays the image, and the button widget that links to the source of the image
    image, the name of the new image to display
    link, the new link of the website that the button should take the user to 
    """
    #set the PhotoImage to the new image, updating the display to show the new image
    img_widget[0].get_img().config(file = image)
    #set the credit button to take the user to the new image's link when it's pressed 
    img_widget[1].get_widget().config(command = lambda: open_page(link))


def open_page(page_to_open):
    """
this component should take the user to a specified webpage
it takes one parameter:
    page_to_open, the link to the webpage that should be opened
    """
    webbrowser.open(page_to_open)

def repeat(products, string_vars, seconds):
    """
this function repeats certain code on a timer, it takes three parameters:
    products, a list of all the products
    string_vars, a list of all the StringVars, needed for refreashing the display
    seconds, the time, in seconds, that the function should wait before repeating
    """

    MINIMUM_PERCENTAGE = 66
    MAXIMUM_PERCENTAGE = 150

    #randomize each products price
    for i in products:
        i.set_price(i.randomize_price(MINIMUM_PERCENTAGE, MAXIMUM_PERCENTAGE))
    #update the display with the new prices
    refresh_display_info(products, string_vars)
    #repeat this function after "seconds" seconds
    threading.Timer(seconds, lambda:repeat(products, string_vars, seconds)).start()

def final_setup():
    #the width and height that will be used to make the tkinter window
    WIDTH = "1000"
    HEIGHT = "600"

    widgets = []

    #this list needs to be in alphabetical order as that's the order the image files will be pulled
    product_names = ["keyboards", "monitors", "mouses"]
    #this list was never used, it should be parallel with the product_names list, but as long as its a list of string and has the same length as the products name list it shouldn't result in errors
    product_descriptions = ["you use these to type", "you need this to see what you're doing", "you need this to move the curser"]
    #this list list needs to be parallel to the product_names list, it should have a link to the respective image 
    links = [
    "https://publicdomainvectors.org/en/free-clipart/Vector-graphics-of-AZERTY-computer-keyboard/13672.html",
    "https://publicdomainvectors.org/en/free-clipart/LCD-screen-with-shadow-vector-graphics/13214.html",
    "https://publicdomainvectors.org/en/free-clipart/Photorealistic-vector-image-of-computer-mouse/12989.html"
    ]
    #the time, in seconds between each price change
    SECONDS_BETWEEN_RESETS = 15

    #-----------------------------------------------
    #call the needed functions to create the program
    root = setup_root(WIDTH, HEIGHT)
    entries = create_entries(root, (WIDTH, HEIGHT))
    
    for i in range(0, len(entries)):
        widgets.append(entries[i].get_widget())

    loop_stuff = setup_UI(root, (WIDTH, HEIGHT), widgets, product_names, product_descriptions)
    gallery = create_gallery(root, get_images(), links, (WIDTH, HEIGHT))
    repeat(loop_stuff[0], loop_stuff[1], SECONDS_BETWEEN_RESETS)
    root.mainloop()
    #-----------------------------------------------

#main

if(__name__ == "__main__"):
    final_setup()
    
