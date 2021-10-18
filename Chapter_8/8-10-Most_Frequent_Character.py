# 8-10 Most Frequent Character

# Write a program that lets the user enter a string and display the character
# that appears most frequently in the string.

# Main function.
def main():
    # Get string from user.
    user_string = input('Enter a string: ')
    # Make a list for count.
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Set the alphabet.
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Make the user string uppercase.
    user_string = user_string.upper()

    # Start the count.
    for ch in user_string:
        index = alpha.find(ch)
        if index > -1:
            count[index] += 1

    # Find the letter that appears most and display it.
    print(alpha[count.index(max(count))])

# Call the main function.
main()
