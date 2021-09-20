# 6-4 Item Counter

# Assume a file containing a series of names (as strings)
# is named names.txt and exists on the computer's disk.
# Write a program that displays the number of names
# that are stored in the file.
# (Hint: Open the file and read every string stored in it.
# Use a variable to keep a count of the number of items that
# are read from the file.)

def main():
    # Set the accumulator.
    total = 0

    try:
        # Open the names.txt file.
        name_file = open('names.txt', 'r')
    except Exception as exx:
        print('An error occurred trying to read the file:', exx)
    else:
        # Read the files content.
        line = name_file.readline()

        # Set the counter.
        while line != '':
            total += 1
            line = name_file.readline()

        # Close the file.
        name_file.close()

        # Print the results.
        print('Amount of names in the file: ', total)

# Call the main function.
main()