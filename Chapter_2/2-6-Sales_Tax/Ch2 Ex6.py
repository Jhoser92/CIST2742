# 2-6 Sales Tax

# Write a program that will ask the user to enter the amount of a purchase.
# The program should then compute the state and county sales tax.
# Assume the state sales tax is 5 percent and the county sales tax is 2.5 percent.
# The program should display the amount of the purchase, the state sales tax, the county sales tax, and
# the total of the sale (which is the sum of the amount of purchase plus the total sales tax).
# Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.

# Set the state and county sales tax.
stax = 0.05
ctax = 0.025

# Get the amount of a purchase.
pamount = float(input('Enter the amount of the purchase: '))

# Calculate the tax.
total_stax = pamount * stax
total_ctax = pamount * ctax
total_tax = total_stax + total_ctax

# Calculate the overall total.
total = pamount + total_tax

# Display the results.
print('Purchase amount: $', format (pamount, ',.2f'), sep='')
print('State sales tax: $', format (total_stax, ',.2f'), sep='')
print('County sales tax: $', format (total_ctax, ',.2f'), sep='')
print('Overall total: $', format (total, ',.2f'), sep='')