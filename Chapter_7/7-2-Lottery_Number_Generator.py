# 7-2 Lottery Number Generator

# Design a program that generates a seven-digit lottery number.
# The program should generate seven random numbers, each in the
# range of 0 through 9, and assign each number to a list element.
# (Random numbers were discussed in Chapter 5.)
# Then write another loop that displays the contents of the list.
import random

# Set the max.
MAX = 7

def main():
    # Create a list.
    numbers = [0] * 7

    # Make the loop.
    for index in range(MAX):
        numbers[index] = random.randint(0, 9)

    # Display the results.
    print('Here are your lottery numbers:')
    print()
    print(numbers)

# Call the main function.
main()
