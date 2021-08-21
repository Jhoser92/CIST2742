# 2-3 Land Calculation

# One acre of land is equivalent to 43,560 square feet.
# Write a program that asks the user to enter the total square feet in a tract
# of land and calculates the number of acres in the tract.
# Hint: Divide the amount entered by 43,560 to get the number of acres.

# Total acres in square feet.
acres = 43560

# Get the total square feet.
sqr_ft = int(input('Enter the total square feet: '))

# Calculate the total acres.
total_acres = sqr_ft/acres
print('The total amount of land is:' , format(total_acres, '.2f'),'acres')
