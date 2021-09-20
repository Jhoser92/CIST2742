# 6-2 File Head Display

# Write a program that asks the user for the name of a file.
# The program should display only the first five lines fo the file's content.
# If the file contains less than five lines, it should display the
# file's entire contents.

def main():
    # Get the name of the file from the user.
    filename = input('Enter a filename: ')

    try:
        # Open the file.
        name_file = open(filename, 'r')
    except Exception as exx:
        print('An error occurred trying to read the file:', exx)
    else:
        # Set counter for amount of lines read.
        for count in range(1, 5 + 1):
            contents = name_file.readline()

            # Strip the \n from the contents.
            contents = contents.rstrip('\n')

            # Print the contents.
            print(contents)

        # Close the file.
        name_file.close()

# Call the main function.
main()