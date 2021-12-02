# 10-8 Cash Register

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

import retail
import cash

END = 0

print('Enter item Information: ')
choice = 1
object_list = []
while choice != END:
    desc = input('Description: ')
    units = input('Amount: ')
    price = float(input('Price: '))
    print()

    items = retail.RetailItem(desc, units, price)
    object_list.append(items)
    items_list = cash.CashRegister(object_list)

    choice = int(input('If you wish to add more enter 1, else if you wish to end enter 0: '))

print('Total of all purchases: ' + str(round(items_list.get_total(), 2)))
print('List of all purchases: \n' + items_list.show_item())
items_list.list_clear()