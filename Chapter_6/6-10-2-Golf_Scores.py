# 6-10 Golf Scores 2

# The Springfork Amateur Golf Club has a tournament every weekend.
# The club president has asked you to write two programs:
#   1. A program that will read each player's name and golf score
#      keyboard input, then save these as records in a file named golf.txt.
#      (Each record will have a field for the player's name and a field
#      for the player's score.)
#   2. A program that reads the records from the golf.txt file and displays them.

def main():
    # Open the file.
    name_file = open('golf.txt', 'r')

    # Read the player names.
    name = name_file.readline()

    # Read the file.
    while name != '':
        # Read the score.
        score = float(name_file.readline())

        # Strip the \n.
        name = name.rstrip('\n')

        # Display the player records.
        print()
        print('Player Name: ', name)
        print('Player Score: ', score)

        # Read the next name.
        name = name_file.readline()

    # Close the file.
    name_file.close()

# Call the main function.
main()