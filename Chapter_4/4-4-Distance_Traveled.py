# 4-4 Distance Traveled

# The distance a vehicle travels can be calculated as follows:
#       distance = speed * time
# For example, if a train travels 40 miles per hour for three hours,
# the distance traveled is 120 miles.
# Write a program that asks the user for the speed of the vehicle
# (in miles per hour) and the number of hours it has traveled.
# It should then use a loop to display the distance the
# vehicle has traveled for each hour of that time period.
# Here is an example of the desired output:
# What is the speed of the vehicle in mph? 40 [Enter]
# How many hours has it traveled? 3 [Enter]
# Hour                      Distance Traveled
# 1                            40
# 2                            80
# 3                            120

# Get the miles per hour and the time traveled.
start_time = 1
speed = int(input('What is the speed of the vehicle in mph? '))
end_time = int(input('How many hours has it traveled? '))

# Print the table headings.
print('Hour\tDistance Traveled')
print('--------------')

# Calculate the distance.
for time in range(start_time, end_time + 1, 1):
    distance = speed * time
    print(time, '  \t', distance)