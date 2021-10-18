# 3-6 Magic Dates

# The date June 10, 1960, is special because when it is written
# in the following format, the months times the day equals the year:
# 6/10/60
# Design a program that asks the user to enter a month (in numeric form),
# a day, and a two-digit year.
# The program should then determine whether the month times the day equals the year.
# If so, it should display a message saying the date is magic.
# Other wise, it should display a message saying the date is not magic.

# Get the date from the user.
month = int(input('Enter the month in numeric form: '))
day = int(input('Enter the day: '))
year = int(input('Enter the year in two-digit form: '))

# Determine if the date is magic
# and display the results.
if month * day == year:
    print('The date is magic!')
else:
    print('The date is not magic.')