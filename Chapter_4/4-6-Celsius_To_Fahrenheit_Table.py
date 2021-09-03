# 4-6 Celsius to Fahrenheit Table

# Write a program that displays a table of the Celsius temperatures
# 0 - 20 and their Fahrenheit equivalents.
# The formula for converting a temperature from Celsius to Fahrenheit is
#       F=9/5*C+32
# where F is the Fahrenheit temperature, and C is the Celsius temperature.
# Your program must use a loop to display the table.

# Set the start and end values.
start_celsius = 0
end_celsius = 21

# Print the table.
print('Celsius\t Fahrenheit')
print('--------------------')

# Print the temperatures.
for celsius in range(start_celsius,end_celsius):
    fahrenheit =  9/5 * celsius +32
    print(celsius, '\t\t', format(fahrenheit, '.2f'))