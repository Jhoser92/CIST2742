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
    # Get the test scores and call the functions.
    test1 = int(input('Enter the first test score: '))
    determine_grade(test1)
    test2 = int(input('Enter the second test score: '))
    determine_grade(test2)
    test3 = int(input('Enter the third test score: '))
    determine_grade(test3)
    test4 = int(input('Enter the fourth test score: '))
    determine_grade(test4)
    test5 = int(input('Enter the fifth test score: '))
    determine_grade(test5)
    print()
    calc_average(test1, test2, test3, test4, test5)

# Define the determine_grade function
def determine_grade(score):
        if score >= 90 and score <= 100:
            print('Grade: A')
        elif score >= 80 and score < 90:
            print('Grade: B')
        elif score >= 70 and score < 80:
            print('Grade: C')
        elif score >= 60 and score < 70:
            print('Grade: D')
        else:
            print('Grade: F')

# Define the calc_average function.
def calc_average(score1, score2, score3, score4, score5):
    avg = (score1 + score2 + score3 + score4 + score5) / 5
    print('Average')
    determine_grade(avg)

# Call the main function.
main()
