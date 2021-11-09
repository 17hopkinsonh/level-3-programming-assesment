"""
    Author: Hayden Hopkinson
    Date started: 6/11/2021
    description: this component will make a image gallery that should be displayed near the top of the canvas
    Version: 2
    Improvements since last version: made the links into buttons that take the user to the webpage
    also merged the class that was in this component with the class in comp1 stored simular information
"""

#libraries

from comp1 import *
import os, webbrowser

#classes

#functions

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


def create_gallery(root, images, links, resolution):
    """
creates the image, credit button, and buttons to scroll throught the images
takes four parameters:
    root, the parent window to assign the GUI objects to
    images, a list of images to display
    links, a list of links to the website where the related image is from
    resolution, a tuple/list with the width of the root at index 0, and the height of the root at index 1
    """
    image_widget = create_image(root, images[0], links[0], resolution)
    buttons = create_buttons(root, images, resolution, links, image_widget)
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
    image = GUI(root, "PhotoImage", 300, 200, int(res[0])/2, int(res[1])/6, image = default_img)
    credit_button = GUI(root, "Button", 300, 50, int(res[0])/2, int(res[1])/6+200, text = "image source", function = lambda: open_page(default_link))
    return [image, credit_button]


def create_buttons(root, images, res, links, img_widget):
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
    buttons.append(GUI(root, "Button", 100, 80, int(res[0])/2-50, int(res[1])/6 + 250, text = "<---", function = lambda: choose_img(images, links, img_widget, False)))
    buttons.append(GUI(root, "Button", 100, 80, int(res[0])/2+50, int(res[1])/6 + 250, text = "--->", function = lambda: choose_img(images, links, img_widget, True)))


def choose_img(images, links, img_widget, foward):
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
        print(0)
        GUI.set_img_value(0)
        change_img(img_widget, images[0], links[0])
    else:
        print(new_num)
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
    img_widget[0].get_img().config(file = image)
    img_widget[1].get_widget().config(command = lambda: open_page(link))


def open_page(page_to_open):
    """
this component should take the user to a specified webpage
it takes one parameter:
    page_to_open, the link to the webpage that should be opened
    """
    webbrowser.open(page_to_open)


#main

if(__name__ == "__main__"):

    #testing
    width = "1000"
    height = "600"

    root = Tk()
    root.title("Title Here")
    root.geometry(width + "x" + height)

    links = [
    "https://publicdomainvectors.org/en/free-clipart/Vector-graphics-of-AZERTY-computer-keyboard/13672.html",
    "https://publicdomainvectors.org/en/free-clipart/LCD-screen-with-shadow-vector-graphics/13214.html",
    "https://publicdomainvectors.org/en/free-clipart/Photorealistic-vector-image-of-computer-mouse/12989.html"
    ]


    test = create_gallery(root, get_images(), links, (width, height))

    #GUI(root, "PhotoImage", 400, 400, 400, 400, image = "testing.png")

    root.mainloop()
