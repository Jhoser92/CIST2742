# 10-4 Employee Class

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

# Import the Employee class.
import employee

# Main function.
def main():
	# Create three employee objects
	emp1 = employee.Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
	emp2 = employee.Employee('Mark Jones', '39119', 'IT', 'Programmer')
	emp3 = employee.Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')

	# Display the employee information.
	print()
	print('Here are the employee information.')
	print()

	print('-Employee 1-')
	print('-----------')
	print('Name:', emp1.get_name())
	print('ID Number:', emp1.get_idnum())
	print('Department:', emp1.get_dept())
	print('Job Title:', emp1.get_title())

	print()
	print('-Employee 2-')
	print('-----------')
	print('Name:', emp2.get_name())
	print('ID Number:', emp2.get_idnum())
	print('Department:', emp2.get_dept())
	print('Job Title:', emp2.get_title())

	print()
	print('-Employee 3-')
	print('-----------')
	print('Name:', emp3.get_name())
	print('ID Number:', emp3.get_idnum())
	print('Department:', emp3.get_dept())
	print('Job Title:', emp3.get_title())

# Call the main function.
main()