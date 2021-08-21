# This program calculates the total acres
# in a tract of land.

# Total acres in square feet.
acres = 43560

# Get the total square feet.
sqr_ft = int(input('Enter the total square feet: '))

# Calculate the total acres.
total_acres = sqr_ft/acres
print('The total amount of land is:' , format(total_acres, '.2f'),'acres')
