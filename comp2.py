"""
    Author: Hayden Hopkinson
    Date started: 3/11/2021
    Description: this program should create a products class that stores information about each product (price, amount brought/sold, e.c.t)
    that also has functions to buy/sell the product, and also change the price
    Version: 1
    Improvements since last version: N/A

"""

#libraries
import random

#classes

class product:

    money = 1000
    
    def __init__(self, name, description, starting_price = 0, starting_stock = 0):
        self._name = name
        self._desc = description
        self._total_sold = 0
        self._total_brought = 0
        self._amount_owned = 0
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
        return self.get_price() * (random.randint(new_min, new_max)/100)

    def buy_stock(self):
        if((self.get_stock() >= 1) and (product.money - self.get_price() >= 0)):
            the_price = self.get_price()
            print("product {} has been purchased for {} tokens".format(self.get_name(), the_price))
            self.set_stock(self.get_stock()-1)
            self.set_price(self.randomize_price(100, 170))
            if(self.get_price() > 1000):
                self.set_price(1000)
            self.set_brought(self.get_brought() + 1)
            self.set_owned(self.get_owned() + 1)
            product.money -= the_price
        else:
            print("the product {} is either out of stock, or you dont have enough tokens to buy it".format(self.get_name()))        
    def sell_stock(self):
        if(self.get_owned() > 0):
            print("product {} has been sold for {} tokens".format(self.get_name(), self._price))
            self.set_stock(self.get_stock()+1)
            self.set_price(self.randomize_price(66, 100))
            if(self.get_price() == 0):
                self.set_price(1)
            self.set_sold(self.get_sold()+1)
            self.set_owned(self.get_owned() - 1)
            product.money += self.get_price()
        else:
            print("you can't sell product {} since you dont own it".format(self.get_name()))

        
#functions


#main
if(__name__ == "__main__"):
    products = [product("name1", "description1"), product("name2", "description2"), product("name3", "description3")]
    
    for i in range(0, 500):
        if(random.randint(0,1)):
            money = products[random.randint(0, 2)].buy_stock()
        else:
            money = products[random.randint(0, 2)].sell_stock()

    for i in products:
        print(i)
