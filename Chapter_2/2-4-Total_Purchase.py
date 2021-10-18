# 2-4 Total Purchase

# A customer in a store is purchasing five items.
# Write a program that asks for the price of each item, and then displays
# the subtotal of the sale, the amount of sales tax, and the total.
# Assume the sales tax is 7 percent.

# Current sales tax.
sales_tax = 0.07

# Get the price of the five items.
item1 = float(input('Enter the price of the first item: '))
item2 = float(input('Enter the price of the second item: '))
item3 = float(input('Enter the price of the third item: '))
item4 = float(input('Enter the price of the fourth item: '))
item5 = float(input('Enter the price of the fifth item: '))

# Calculate the subtotal.
stotal = item1 + item2 + item3 + item4 +item5

# Calculate the total tax.
total_tax = stotal * sales_tax

# Calculate the total with tax.
total = stotal + total_tax

# Display the subtotal, sales tax, and total.
print('Subtotal =:', format(stotal, ',.2f'))
print('Sales Tax=:', format(total_tax, ',.2f'))
print('Total=:', format(total, ',.2f'))

