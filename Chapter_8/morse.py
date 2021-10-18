# 8-4 Morse Code Converter

# Morse code for the characters.
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

# Convert the string to Morse code.
def convert_morse(user_string):
    # Convert the string to uppercase.
    user_string = user_string.upper()
    # Create a new string for replacement string.
    new_string = ''
    # Convert using for loop.
    for ch in user_string:
        if ch == ' ':
            new_string += ' '
        elif ch == ',':
            new_string += '--..--'
        elif ch == '.':
            new_string += '.-.-.-'
        elif ch == '?':
            new_string += '..--..'
        elif ch == '0':
            new_string += '-----'
        elif ch == '1':
            new_string += '.----'
        elif ch == '2':
            new_string += '..---'
        elif ch == '3':
            new_string += '...--'
        elif ch == '4':
            new_string += '....-'
        elif ch == '5':
            new_string += '.....'
        elif ch == '6':
            new_string += '-....'
        elif ch == '7':
            new_string += '--...'
        elif ch == '8':
            new_string += '---..'
        elif ch == '9':
            new_string += '----.'
        elif ch == 'A':
            new_string += '.-'
        elif ch == 'B':
            new_string += '-...'
        elif ch == 'C':
            new_string += '-.-.'
        elif ch == 'D':
            new_string += '-..'
        elif ch == 'E':
            new_string += '.'
        elif ch == 'F':
            new_string += '..-.'
        elif ch == 'G':
            new_string += '--.'
        elif ch == 'H':
            new_string += '....'
        elif ch == 'I':
            new_string += '..'
        elif ch == 'J':
            new_string += '.---'
        elif ch == 'K':
            new_string += '-.-'
        elif ch == 'L':
            new_string += '.-..'
        elif ch == 'M':
            new_string += '--'
        elif ch == 'N':
            new_string += '-.'
        elif ch == 'O':
            new_string += '---'
        elif ch == 'P':
            new_string += '.--.'
        elif ch == 'Q':
            new_string += '--.-'
        elif ch == 'R':
            new_string += '.-.'
        elif ch == 'S':
            new_string += '...'
        elif ch == 'T':
            new_string += '-'
        elif ch == 'U':
            new_string += '..-'
        elif ch == 'V':
            new_string += '...-'
        elif ch == 'W':
            new_string += '.--'
        elif ch == 'X':
            new_string += '-..-'
        elif ch == 'Y':
            new_string += '-.-'
        elif ch == 'Z':
            new_string += '--..'

    # Return the variable.
    return new_string