# 7-4 Number Analysis Program

# Design a program that asks the user to enter a series of 20 numbers.
# The program should store the numbers in a list then display the following data:
#   -The lowest number in the list
#   -The highest number in the list
#   -The total of the numbers in the list
#   -The average of the numbers in the list

# Make a constant for the size of the list.
TOTAL_NUMS = 20

def main():
    # Create a list.
    numbers = [0] * TOTAL_NUMS

    # Use try/except to handle error.
    try:
        # Get the numbers from the user.
        for index in range(TOTAL_NUMS):
            print('Enter number ',
                  index + 1, ': ', sep='', end='')
            numbers[index] = float(input())
    except Exception as err:
        print('An error has occurred: ', err)
    else:
        print()
        print("The numbers in the list are:")
        print(numbers)
        print()
        # Call the functions.
        min_max(numbers)
        total = total_nums(numbers)
        average(total)

# Use min_max function to determine the lowest and highest numbers.
def min_max(nums):
    lowest = min(nums)
    highest = max(nums)
    # Display the lowest and highest numbers.
    print('Lowest Number: ', lowest)
    print('Highest Number: ', highest)

# Use total_nums to determine the total of the numbers.
def total_nums(total_nums):
    # Set an accumulator.
    total = 0

    # Calculate the total.
    for num in total_nums:
        total += num

    # Display the total.
    print('Total: ',
          format(total, ',.2f'), sep='')

    # Return the total.
    return total

# Use the average_nums function to determine the average fo the numbers.
def average(average_nums):
    # Calculate the average.
    avg = average_nums / TOTAL_NUMS
    # Display the average.
    print('Average: ',
          format(avg, ',.2f'), sep='')

# Call the main function.
main()
