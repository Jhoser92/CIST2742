# 4-15 Nested Loop Pattern 2
# Write a program that uses nested loops to draw this patter:
#       ##
#       # #
#       #  #
#       #   #
#       #    #
#       #     #

# Set the values.
BASE_SIZE = 7

# Write the nested loops.
for r in range(BASE_SIZE):
    print('#', end='')
    for c in range(r):
        print(' ', end='')
    print('#')
