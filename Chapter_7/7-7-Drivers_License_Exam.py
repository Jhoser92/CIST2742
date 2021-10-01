# 7-7 Driver's License Exam

# The local driver's office has asked you to create an application that grades
# the written portion of the driver's license exam.
# The exam has 20 multiple choice questions.
# Here are the correct answers:
# 1.A    6.B    11.A    16.C
# 2.C    7.C    12.D    17.B
# 3.A    8.A    13.C    18.B
# 4.A    9.C    14.A    19.D
# 5.D   10.B    15.D    20.A
# Your program should store these correct answers in a list.
# The program should read the student's answers for each of the 20
# questions from a text file and store the answers in another list.
# (Create your own text file to test the application.)
# After the student's answers have been read from the file, the program
# should display a message indicating whether the student passed or failed the exam.
# (A student must correctly answer 15 of the 20 questions to pass to pass the exam.)
# It should then display the total number of correctly answered questions, the total
# number of incorrectly answered questions, and a list showing the question numbers
# of the incorrectly answered questions.

def main():
    # Call the functions.
    correct = correct_answers()
    students = student_answers()
    check_answers(correct, students)

# Use the correct_answers function to get the answers from the file.
def correct_answers():
    # Open the file.
    infile = open('answers.txt', 'r')
    # Read the file contents.
    answers = infile.readlines()
    # Close the file.
    infile.close()
    index = 0
    # Use a while loop.
    while index < len(answers):
        answers[index] = answers[index].rstrip('\n')
        index += 1
    # Return the value.
    return answers

# Use the student_answers function to get the student answers from the file.
def student_answers():
    # Open the file.
    infile = open('students.txt', 'r')
    # Read the contents of the file.
    stud_ans = infile.readlines()
    # Close the file.
    infile.close()
    index = 0
    # Use a while loop.
    while index < len(stud_ans):
        stud_ans[index] = stud_ans[index].rstrip('\n')
        index += 1
    # Return the value.
    return stud_ans

# Use the check_answers function to determine if pass/fail.
def check_answers(correct, student):
    count = 0
    wrong = []
    # Use a for loop.
    for index in range(20):
        if correct[index] == student[index]:
            count += 1
        else:
            wrong.append(index)
            count += 0
    # Make a counter using if/else and display the results.
    if count < 15:
        print()
        print('You failed.')
    else:
        print()
        print('You passed.')

    # Display the results.
    print()
    print('Number of correct answers:', count)
    print('Number of incorrect answers:', 20 - count)
    print('Question numbers answered incorrectly', wrong)

# Call the main function.
main()
