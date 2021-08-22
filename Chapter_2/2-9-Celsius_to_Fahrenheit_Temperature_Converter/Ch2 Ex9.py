# 2-9 Celsius to Fahrenheit Temperature Converter

# Write a program that converts Celsius temperatures to Fahrenheit temperatures.
# The formula is as follow:

# F = 9 / 5 C + 32

# The program should ask the user to enter a temperature in Celsius,
# and then display the temperature converted to Fahrenheit.

# Get the temperature in Celsius.
celsius = float(input('What is the temperature in Celsius: '))

# Convert Celsius to Fahrenheit using the formula.
fahrenheit =  9 / 5 * celsius + 32

# Display the results.
print('Temperature in Celsius: ', format(celsius, '.2f'), 'C', sep='')
print('Temperature in Fahrenheit: ', format(fahrenheit, '.2f'), 'F', sep='')