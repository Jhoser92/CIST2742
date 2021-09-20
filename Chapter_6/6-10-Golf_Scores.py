# 6-10 Golf Scores

# The Springfork Amateur Golf Club has a tournament every weekend.
# The club president has asked you to write two programs:
#   1. A program that will read each player's name and golf score
#      keyboard input, then save these as records in a file named golf.txt.
#      (Each record will have a field for the player's name and a field
#      for the player's score.)
#   2. A program that reads the records from the golf.txt file and displays them.

def main():
    # Create a control variable.
    another = 'y'

    # Open the file.
    name_file = open('golf.txt', 'a')

    # Add the player records.
    while another == 'y' or another == 'Y':
        # Enter the information.
        print('Enter the players data')
        name = input('Name: ')
        score = input('Golf Score: ')

        # Append the data.
        name_file.write(name + '\n')
        name_file.write(str(score) + '\n')

        # Ask the user if they want to add more player records.
        print()
        print('Do you want to add another player record?')
        another = input('Y for yes, N for no: ')
        print()

    # Close the file.
    name_file.close()
    print('Data recorded to file golf.txt')

# Call the main function.
main()