# 2-7 Miles-per-Gallon

# A car's miles-per-gallon (MPG) can be calculated with the following formula:

# MPG = Miles driven / Gallons of gas used

# Write a program that asks the user for the number of miles driven
# and the gallons of gas used.
# It should calculate the car's MPG and display the result.

# Get the number of miles driven and the gas used.
miles = float(input('How many miles were driven: '))
gas = float(input('How many gallons of gas were used: '))

# Calculate the MPG
mpg = miles / gas

# Display the results.
print('Miles driven: ', miles)
print('Gallons of gas: ', gas)
print('Total MPG: ', format(mpg, '.2f'))