# 7-9 Population Data

# If you have downloaded the source code you will find a file
# named USPopulation.txt in the Chapter 7 folder.
# The file contains the midyear population of the United States,
# in thousands, during the years 1950 through 1990.
# The first line in the file contains the population for 1950,
# the second line contains the population for 1951, and so forth.

# Write a program that reads the file's contents into a list.
# The program should display the following data:
#   -The average annual change in population during the time period.
#   -The year with the greatest increase in population during the time period.
#   -The year with the smallest increase in population during the time period.

# Set a constant.
START = 1950


def main():
    # Call the functions.
    population = get_pop()
    change = pop_change(population)
    average = average_change(change)
    great_inc, pop_inc = big_increase(change, START)
    small_inc, pop_small = small_increase(change, START)
    display_data(average, great_inc, pop_inc, small_inc, pop_small)

# Use the get_pop function to make a list from the file.
def get_pop():
    infile = open('USPopulation.txt', 'r')
    population_list = []
    us_pop = infile.readline()

    # Make a while loop.
    while us_pop != '':
        us_pop = int(us_pop)
        population_list.append(us_pop)
        us_pop = infile.readline()

    # Close the file.
    infile.close()

    # Return the value.
    return population_list

# Use the pop_change function to determine the change.
def pop_change(population):
    change_list = []

    # Make a for loop.
    for index in range(len(population)):
        if index == 0:
            change_list.append(0)
        else:
            change_list.append(population[index] - population[index - 1])

    # Return the value.
    return change_list

# Use the average_change to get the average.
def average_change(change):
    total_change = 0

    # Use a for loop.
    for index in range(len(change)):
        total_change += change[index]

    # Calculate the average.
    annual_average = total_change / len(change)

    # Return the value.
    return annual_average

# Use the big_increase function to determine the
# greatest increase.
def big_increase(change_list, start):
    pop_inc = max(change_list)
    index = change_list.index(pop_inc)
    great_inc = index + start

    # Return the value.
    return great_inc, pop_inc

# Use the small_increase function to determine the
# smallest increase.
def small_increase(change_list, start):
    pop_small = min(change_list[1:])
    index = change_list.index(pop_small)
    small_inc = index + start

    # Return the value.
    return small_inc, pop_small

# Use the display_data function to display the results.
def display_data(average, great_inc, pop_inc, small_inc, pop_small):
    print('Average annual change in population is: ', format(average, ',.2f'))
    print('The year: ', (great_inc),
          ' had the greatest increase in population during the time period'
          ' with a population increase of: ', format(pop_inc, ','))
    print('The year: ', (small_inc),
          ' had the smallest increase in population during the time period'
          ' with a population increase of: ', format(pop_small, ','))

# Call the main function.
main()