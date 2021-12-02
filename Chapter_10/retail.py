# 10-5 Retail Item Class: Module

# Write a class named RetailItem that holds data about an item in a retail store.
# The class should store the following data in attributes: item description, units in inventory, and price.
# Once you have written the class, write a program that creates three RetailItem objects
# and stores the following data in them:

#              -Description        Units in Inventory     Price-
#   Item #1     Jacket             12                     59.95
#   Item #2     Designer Jeans     40                     34.95
#   Item #3     Shirt              20                     24.95

# RetailItem class.
class RetailItem:
    # The __init__ method to initialize attributes.
    def __init__(self, desc, units, price):
        self.__desc = desc
        self.__units = units
        self.__price = price

    # Set the attributes.
    def set_desc(self, desc):
        self.__desc = desc

    def set_units(self, units):
        self.__units = units

    def set_price(self, price):
        self.__price = price

    # Return the attributes.
    def get_desc(self):
        return self.__desc

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price

    # The __str__ method returns the object's state
    # as a string.
    def __str__(self):
        return 'Description: ' + self.__desc + \
               '\nUnits in Inventory: ' + self.__units + \
               '\nPrice: ' + self.__price