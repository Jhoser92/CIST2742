# 6-6 Average of Numbers

# Assume a file containing a series of integers is names numbers.txt
# and exists on the computer's disk.
# Write a program that calculates the average of all the numbers
# stored in the file.

def main():
    # Set the accumulators.
    amount = 0
    total = 0

    try:
        # Open the file.
        name_file = open('numbers.txt', 'r')
    except Exception as exx:
        print('An error occurred trying to read the file:', exx)
    else:
        # Read the files content.
        line = name_file.readline()

        # Set a counter.
        while line != '':
            num = int(line)
            total += num
            amount += 1
            line = name_file.readline()

        # Close the file
        name_file.close()

        # Calculate the average.
        avg = total / amount

        # Print the results.
        print('The numbers on the file average out to: ',
              format(avg, ',.2f'), sep='')

# Call the main function.
main()