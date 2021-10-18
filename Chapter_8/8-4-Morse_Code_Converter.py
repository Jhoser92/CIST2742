# 8-4 Morse Code Converter

# Morse code is a code where each letter of the English Alphabet,
# each digit, and various punctuation characters are represented
# by a series of dots and dashes.
# Table 8-4 shows part of the code.
# Write a program that asks you to enter a string, then converts
# that string to Morse code.
#   -Character-     -Code-      -Character-     -Code-      -Character-     -Code-
#    space           space       A               .-          O               ---
#    comma           --..--      B               -...        P               .--.
#    period          .-.-.-      C               -.-.        Q               --.-
#    question mark   ..--..      D               -..         R               .-.
#    0               -----       E               .           S               ...
#    1               .----       F               ..-.        T               -
#    2               ..---       G               --.         U               ..-
#    3               ...--       H               ....        V               ...-
#    4               ....-       I               ..          W               .--
#    5               .....       J               .---        X               -..-
#    6               -....       K               -.-         Y               -.-
#    7               --...       L               .-..        Z               --..
#    8               ---..       M               --
#    9               ----.       N               -.

# Import file.
import morse

# Main function.
def main():
    # Get a string from the user.
    user_string = input('Type something to convert to Morse code: ')
    print()
    # Display the results in upper case.
    print(user_string.upper())
    print()
    print('In Morse code is:')
    print()
    # Convert to Morse code by calling function from morse.py file and display it.
    print(morse.convert_morse(user_string))

# Call the main function.
main()
