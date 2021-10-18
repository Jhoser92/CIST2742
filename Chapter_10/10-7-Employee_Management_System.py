# 10-7 Employee Management System

# This exercise assumes you have entered the Employee class for Programming Exercise 4.
# Create a program that stores Employee objects in a dictionary.
# Use the employee ID number as the key
# The program should present a menu that lets the user perform the following actions:
# -Look up an employee in the dictionary
# -Add a new employee to the dictionary
# -Change an existing employee's name, department, and job title in the dictionary
# -Delete an employee from the dictionary
# -Quit the program
# When the program ends, it should pickle the dictionary and save it to a file.
# Each time the program starts, it should try to load the pickled dictionary form the file.
# If the file does not exist, the program should start with an empty dictionary.

# Import employee and pickle.
import employee
import pickle

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constant for the filename.
FILENAME = 'employee.dat'

# Main function.
def main():
    # Load the dictionary contents.
    empinfo = load_info()

    # Initialize a variable for the user's choice.
    choice = 0

    # Process menu selections until user
    # wants to quit the program.
    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()
        # Process the choice.
        if choice == LOOK_UP:
            look_up(empinfo)
        elif choice == ADD:
            add(empinfo)
        elif choice == CHANGE:
            change(empinfo)
        elif choice == DELETE:
            delete(empinfo)

    # Save the information.
    save_info(empinfo)

# Load info function loads the information.
def load_info():
    try:
        # Open the the file for binary reading.
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary.
        employee_dct = pickle.load(input_file)

        # Close the file.
        input_file.close()
    except IOError:
        # If it could not open the file, create
        # an empty dictionary.
        employee_dct ={}

    # Return the dictionary.
    return employee_dct

# The get menu choice function gets users choice.
def get_menu_choice():
    # Menu
    print()
    print('Menu')
    print('--------------------')
    print('1. Look up an employee')
    print('2. Add a new employee')
    print('3. Change an existing employee')
    print('4. Delete an employee')
    print('5. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # Return the user's choice.
    return choice

# The look up function looks up an ID Number in the dictionary.
def look_up(empinfo):
    # Get an ID Number to look up.
    idnum = input('Enter an ID Number: ')

    # Look it up in the dictionary.
    print(empinfo.get(idnum, 'That ID Number is not found.'))

# The add function adds a new entry to the dictionary.
def add(empinfo):
    # Get the contact info.
    name = input('Name: ')
    idnum = input('ID Number: ')
    dept = input('Department: ')
    title = input('Job Title: ')

    # Create an employee object named entry.
    entry = employee.Employee(name, idnum, dept, title)

    # If the ID Number does not exit in the dictionary,
    # add it as a key with the entry object as the
    # associated value.
    if idnum not in empinfo:
        empinfo[idnum] = entry
        print('The entry has been added.')
    else:
        print('That ID Number already exist.')

# The change function changes existing employee information from dictionary.
def change(empinfo):
    # Get a name to look up
    idnum = input('Enter an ID Number: ')

    if idnum in empinfo:

        # Get a new ID Number.
        name = input('Enter a new name:')

        # Get a new email address.
        dept = input('Enter the new department: ')

        # Get a new job title.
        title = input('Enter a new job title: ')

        # Create a employee object named entry.
        entry = employee.Employee(name, idnum, dept, title)

        # Update the entry.
        empinfo[idnum] = entry
        print('Information updated.')
    else:
        print('That ID Number not found.')

# The delete function deletes information from the dictionary.
def delete(empinfo):
    # Get an ID Number to look up.
    idnum = input('Enter an ID Number: ')

    # If the name is found, delete the entry.
    if idnum in empinfo:
        del empinfo[idnum]
        print('Info has been deleted.')
    else:
        print('That ID Number was not found.')

# The save info function pickles the specified object and saves it to the employee file.
def save_info(empinfo):
    # Open the file for writing.
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(empinfo, output_file)

    # Close the file.
    output_file.close()

# Call the main function.
main()