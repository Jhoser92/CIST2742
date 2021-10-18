# 3-15 Time Calculator

# Write a program that asks the user to enter a number of seconds and works as follows:

# -There are 60 seconds in a minute.
# If the number of seconds entered by the user is greater than or equal to 60,
# the program should display the number of minutes in that many seconds.

# -There are 3,600 seconds in an hour.
# If the number of seconds entered by the user is greater than or equal to 3,600,
# the program should display the number of hours in that many seconds.

# -There are 86,400 seconds in a day.
# If the number seconds entered byt the user is greater than or equal to 86,400,
# the program should display the number of days in that many seconds.

# Set the minute, hour, and day in seconds.
minute = 60
hour = 3600
day = 86400

# Get the number of seconds from the user.
seconds = int(input('Enter the number of seconds: '))

# Calculate the time.
if seconds >= minute and seconds < hour:
    totalm = seconds / minute
    print('There is', format(totalm, '.3f'), 'minutes in', seconds, 'seconds.')
else:
    if seconds >= hour and seconds < day:
        totalm = seconds / minute
        totalh = seconds / hour
        print('There is', format(totalh, '.3f'), 'hours in', seconds, 'seconds.')
        print('There is', format(totalm, '.3f'), 'minutes in', seconds, 'seconds.')
    else:
        totalm = seconds / minute
        totalh = seconds / hour
        totald = seconds / day
        print('There is', format(totald, '.3f'), 'days in', seconds, 'seconds.')
        print('There is', format(totalh, '.3f'), 'hours in', seconds, 'seconds.')
        print('There is', format(totalm, '.3f'), 'minutes in', seconds, 'seconds.')