# 10-8 Cash Register: Module

# This exercise assumes you have created the RetailItem class for Programming Exercise 5.
# Create a CashRegister class that can be used with the RetailItem class. The CashRegister
# class should be able to internally keep a list of RetailItem objects.
# The class should have the following methods:

# -A method named purchase_item that accepts a RetailItem object as an argument.
#  Each time the purchase_item method is called, the RetailItem object that is passed
#  as an argument should be added to the list.
# -A method named get_total that returns the total price of all the RetailItem objects
#  stored in the CashRegister object's internal list.
# -A method named show_items that displays data about the RetailItem objects stored
#  in the CashRegister object's internal list.
# -A method names clear that should clear the CashRegister object's internal list.

# Demonstrate the CashRegister class in a program that allows the user to select several
# items for purchase.
# When the user is ready to check out, the program should display a list of all the items
# he or she selected for purchase, as well as the total price.

class CashRegister:
    def __init__(self, item_list):
        self.__item_list = item_list

    def purchase_item(self, item_list):
        self.__item_list = item_list

    def get_goods_list(self):
        return self.__item_list

    def get_total(self):
        total_price = 0
        item_list = self.__item_list
        for item in item_list:
            total_price += item.get_price()
        return total_price

    def show_item(self):
        item_list = self.__item_list
        string_items = ''
        for item in item_list:
            string_items += item.get_desc() + '\n'
        return string_items

    def list_clear(self):
        self.__item_list.clear()