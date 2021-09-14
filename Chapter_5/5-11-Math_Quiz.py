# 5-11 Math Quiz

# Write a program that gives simple math quizzes.
# The program should display two random numbers that are to be added, such as:
#       247
#      +129
# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect, a message showing the correct answer should be displayed.

import random

# Main Function
def main():
      num1 = random.randint(1, 1000)            # Random number 1.
      num2 = random.randint(1, 1000)            # Random number 2.
      print('\t ', format(num1, ','))
      print('\t+', format(num2, ','))
      total = sum(num1, num2)                   # Call the sum function.
      num3 = int(input('Enter the sum: '))      # Number from user.
      if num3 == total:
            print('Congratulations! That is correct!')
      else: print('Sorry the correct answer is: ' ,
                  format(total, ','), sep='')

# Sum function.
def sum(number1, number2):
      value = number1 + number2
      return value

# Call the main function.
main()