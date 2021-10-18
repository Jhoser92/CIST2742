# 3-10 Money Counting Game

# Create a change counting game that gets the user to enter
# the number of coins required to make exactly one dollar.
# The program should prompt the user to enter the number of
# pennies, nickels, dimes, and quarters.
# If the total value of the coins entered is equal to one
# dollar, the program should congratulate the user for
# winning the game.
# Otherwise, the program should display a message indicating
# whether the amount entered was more than or less than one dollar.

# Set the values of the coins.
pvalue = 0.01
nvalue = 0.05
dvalue = 0.10
qvalue = 0.25
dollar = 1.00

# Get the amount of coins from the user.
penny = int(input('Enter the amount of pennies: '))
nickel = int(input('Enter the amount of nickels: '))
dime = int(input('Enter the amount of dimes: '))
quarter = int(input('Enter the amount of quarters: '))

# Calculate the value of the coins and the total.
total_pvalue = penny * pvalue
total_nvalue = nickel * nvalue
total_dvalue = dime * dvalue
total_qvalue = quarter * qvalue
total = total_pvalue + total_nvalue + total_dvalue + total_qvalue

# Display the results and determine if more than or less than a dollar.
print('Your total is: $', format(total, ',.2f'), sep='')
if total == dollar:
    print('Congratulations! Your total is equal to $', format(dollar, ',.2f'),'!', sep='')
else:
    if total > dollar:
        print('Sorry your total is more than $', format(dollar, ',.2f'), sep='')
    else:
        print('Sorry your total is less than $', format(dollar, ',.2f'), sep='')