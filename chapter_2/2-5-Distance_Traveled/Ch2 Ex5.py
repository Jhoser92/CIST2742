# 2-5 Distance Traveled

# Assuming there are no accidents or delays, the distance that a car
# travels down the interstate can be calculated with the following formula:

# Distance = Speed x Time

# A car is traveling at 70 miles per hour.
# Write a program that displays the following:

# -The distance the car will travel in 6 hours
# -The distance the car will travel in 10 hours
# -The distance the car will travel in 15 hours

# Set the speed.
speed = 70

# Set the times.
time1 = 6
time2 = 10
time3 = 15

# Calculate the distance.
dist1 = speed * time1
dist2 = speed * time2
dist3 = speed * time3

# Display the results.
print('The car is going down the interstate at', speed,'mph.')
print('In 6 hours the car would have traveled', dist1,'miles.')
print('In 10 hours the car would have traveled', dist2,'miles.')
print('In 15 hours the car would have traveled', dist3,'miles.')
