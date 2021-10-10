# 9-3-2 File Encryption and Decryption

# Write a program that uses a dictionary to assign "codes" to each letter of the alphabet.
# For example:
#   codes = { 'A' : '%', 'a' : '9', 'B' : '@', 'b' : '#', etc...}
# Using this example, the letter A would be assigned the symbol %, the letter a would be
# assigned the number 9, the letter B would be assigned the symbol @, and so forth.
# The program should open a specified text file, read its contents, then use the
# dictionary to write an encrypted version of the file's contents to a second file.
# Each character in the second file should contain the code for the corresponding
# character in the first file.
# Write a second program that opens an encrypted file and displays its decrypted
# contents on the screen.

# Make a dictionary for codes.
codes = {'A': '~', 'B': '!', 'C': '@', 'D': '#', 'E': '$', 'F': '%', 'G': '^', 'H': '&',
         'I': '*', 'J': '(', 'K': ')', 'L': '_', 'M': '+', 'N': '{', 'O': '}', 'P': ':',
         'Q': '"', 'R': '<', 'S': '>', 'T': '?', 'U': '`', 'V': '1', 'W': '2', 'X': '3',
         'Y': '4', 'Z': '5',

         'a': '6', 'b': '7', 'c': '8', 'd': '9', 'e': '0', 'f': '-', 'g': '=', 'h': '[',
         'i': ']', 'j': ';', 'k': "'", 'l': ',', 'm': '.', 'n': '/', 'o': 'A', 'p': 'B',
         'q': 'C', 'r': 'D', 's': 'E', 't': 'F', 'u': 'G', 'v': 'H', 'w': 'I', 'x': 'J',
         'y': 'K', 'z': 'L',

         '1': 'M', '2': 'N', '3': 'O', '4': 'P', '5': 'Q', '6': 'R', '7': 'S', '8': 'T',
         '9': 'U', '0': 'V', '.': 'W',  ' ': '  '}

# Main function
def main():
    # Open text file.
    infile = open('test1.txt', 'r')

    # Read file contents and strip \n.
    file_text = infile.readline()
    file_text = file_text.rstrip('\n')

    # Print the file text.
    while file_text != '':
        print()
        print(file_text)
        print()

        # Decrypt the file contents and print results.
        for ch in file_text:
            for key, value in codes.items():
                if ch == value:
                    print(key, end='')
            if ch == ' ':
                print(' ')

        # Read the next line in the file.
        print()
        file_text = infile.readline()
        print()

    # Close the file.
    infile.close()

# Call the main function.
main()
