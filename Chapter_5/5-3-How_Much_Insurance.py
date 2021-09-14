# 5-3 How Much Insurance?

# Many financial experts advise that property owners should insure
# their homes or buildings for at least 80 percent of the amount
# it would cost to replace the structure.
# Write a program that asks the user to enter the replacement
# cost of a building, then display the minimum amount of insurance
# he or she should buy for the property.

# Set the recommended insurance amount.
MIN_INSURANCE = 0.8

# Get the replacement cost.
replace = float(input('Enter the replacement cost of the building: '))

# Calculate the total and display the total.
total = replace * MIN_INSURANCE
print('The minimum amount of insurance you should buy is: $',
      format(total, ',.2f'),
      sep='')