# 9-3 File Encryption and Decryption

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
codes = { 'A':'~', 'a':'`', 'B':'!', 'b':'1', 'C':'@', 'c':'2', 'D':'#', 'd':'3', 'E':'$',
          'e':'4', 'F':'%', 'f':'5', 'G':'^', 'g':'6', 'H':'&', 'h':'7', 'I':'*', 'i':'8',
          'J':'(', 'j':'9', 'K':')', 'k':'0', 'L':'_', 'l':'-', 'M':'+', 'm':'=', 'N':'{',
          'n':'[', 'O':'}', 'o':']', 'P':'|', 'p':':', 'Q':';', 'q':"'", 'R':'"', 'r':'<',
          'S':',', 's':'>', 'T':'.', 't':'/', 'U':'?', 'u':'?!', 'V':'>@', 'v':'<#', 'W':"'$",
          'w':':%', 'X':'}^', 'x':'{&', 'Y':'+*', 'y':'_(', 'Z':'_(', 'z':'()', ' ':' ',
          '1':'#!', '2':'#@', '3':'##', '4':'#$', '5':'#%', '6':'#^', '7':'#&', '8':'#*',
          '9':'#(', '0':'#)', '.':'.. '}

def main():
    infile = open('test.txt', 'r')
    writefile = open('test1.txt', 'w')

    file_text = infile.readline()
    file_text = file_text.rstrip('\n')
    while file_text != '':
        print(file_text)
        for ch in file_text:
            if ch in codes:
                value = codes.get(ch)
                print(value, end='')
                writefile.write(value + '')
        print()
        file_text = infile.readline()
        writefile.write('\n')
    writefile.close()
    infile.close()

main()
