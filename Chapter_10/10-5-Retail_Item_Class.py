# 10-5 Retail Item Class

# Write a class named RetailItem that holds data about an item in a retail store.
# The class should store the following data in attributes: item description, units in inventory, and price.
# Once you have written the class, write a program that creates three RetailItem objects
# and stores the following data in them:

#              -Description        Units in Inventory     Price-
#   Item #1     Jacket             12                     59.95
#   Item #2     Designer Jeans     40                     34.95
#   Item #3     Shirt              20                     24.95

# Import the RetailItem class.
import retail

# Main function.
def main():
	# Create three employee objects
    item1 = retail.RetailItem('Jacket', '12', '59.95')
    item2 = retail.RetailItem('Designer Jeans', '40', '34.95')
    item3 = retail.RetailItem('Shirt', '20', '24.95')

    # Display the employee information.
    print()
    print('Here is the item information.')
    print()

    print('-Item 1-')
    print('-----------')
    print('Item Description:', item1.get_desc())
    print('Units in Inventory:', item1.get_units())
    print('Price:', item1.get_price())

    print()
    print('-Item 2-')
    print('-----------')
    print('Item Description:', item2.get_desc())
    print('Units in Inventory:', item2.get_units())
    print('Price:', item2.get_price())

    print()
    print('-Item 3-')
    print('-----------')
    print('Item Description:', item3.get_desc())
    print('Units in Inventory:', item3.get_units())
    print('Price:', item3.get_price())

# Call the main function.
main()