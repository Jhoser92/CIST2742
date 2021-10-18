# 10-4 Employee Class: Module

# Write a class named Employee that holds the following data about an employee
# in attributes: name, ID number, department, and job title.
# Once you have written the class, write a program that creates three Employee
# objects to hold the following data:
#  -Name            ID Number       Department          Job Title-
#   Susan Meyers    47899           Accounting          Vice President
#   Mark Jones      39119           IT                  Programmer
#   Joy Rogers      81774           Manufacturing       Engineer
# The program should store this data in the three objects, then display the data
# for each employee on the screen.

# Employee class.
class Employee:
    # The __init__ method to initialize attributes.
    def __init__(self, name, idnum, dept, title):
        self.__name = name
        self.__idnum = idnum
        self.__dept = dept
        self.__title = title

    # Set the attributes.
    def set_name(self, name):
        self.__name = name

    def set_idnum(self, idnum):
        self.__idnum = idnum

    def set_dept(self, dept):
        self.__dept = dept

    def set_title(self, title):
        self.__title = title

    # Return the attributes.
    def get_name(self):
        return self.__name

    def get_idnum(self):
        return self.__idnum

    def get_dept(self):
        return self.__dept

    def get_title(self):
        return self.__title

    # The __str__ method returns the object's state
    # as a string.
    def __str__(self):
        return 'Name: ' + self.__name + \
               '\nID Number: ' + self.__idnum + \
               '\nDepartment: ' + self.__dept + \
               '\nJob Title: ' + self.__title