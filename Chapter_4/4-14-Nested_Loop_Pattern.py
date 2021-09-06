# 4-14 Nested Loop Pattern

# Write a program that uses nested loops to draw this pattern:
# *******
# ******
# *****
# ****
# ***
# **
# *

# Set the values.
BASE_SIZE = 8
FINAL_COL = 0
INC = -1

# Write the nested loops.
for c in range(BASE_SIZE, FINAL_COL, INC):
    for r in range(c):
        print("*", end='')
    print()
