# 5-15 Test Average and Grade

# Write a program that asks the user to enter five test scores.
# The program should display a letter grade for each score
# and the average test score.
# Write the following functions in the program:
# -calc_average. This function should accept five test scores
# as argument and return the average of the scores.

# -determine_grade. This function should accept a test score
# as an argument and return a letter grade for the score based
# on the following grading scale.

#   Score       Letter Grade
#   90-100            A
#   80-89             B
#   70-79             C
#   60-69             D
#   Below 60          F

# Main function
def main():
    # Get the test scores
    test1 = int(input('Enter the first test score: '))
    test2 = int(input('Enter the second test score: '))
    test3 = int(input('Enter the third test score: '))
    test4 = int(input('Enter the fourth test score: '))
    test5 = int(input('Enter the fifth test score: '))
    print()
    determine_grade(test1, test2, test3, test4, test5)
    print()
    calc_average(test1, test2, test3, test4, test5)

# Define the determine_grade function
def determine_grade(test1, test2, test3, test4, test5):
    for test in test1, test2, test3, test4, test5:
        if test >= 90 and test <= 100:
            print('Your test score of', test, 'is an A')
        elif test >= 80 and test < 90:
            print('Your test score of', test, 'is a B')
        elif test >= 70 and test < 80:
            print('Your test score of', test, 'is a C')
        elif test >= 60 and test < 70:
            print('Your test score of', test, 'is a D')
        else:
            print('Your test score of', test, 'is an F')

# Define the calc_average function.
def calc_average(score1, score2, score3, score4, score5):
    total_avg = (score1 + score2 + score3 + score4 + score5) / 5
    if total_avg >= 90 and total_avg <= 100:
        print('Your average letter grade is an A')
    elif total_avg >=80 and total_avg < 90:
        print('Your average letter grade is a B')
    elif total_avg >=70 and total_avg < 80:
        print('Your average letter grade is a C')
    elif total_avg >=60 and total_avg < 70:
        print('Your average letter grade is a D')
    else:
        print('Your average letter grade is F')

# Call the main function.
main()