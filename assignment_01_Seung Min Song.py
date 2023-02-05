#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95

# Get the test scores.

# Get the test scores as integers and add code for test3 insert.
'''
test1 = input('Enter the score for test 1: ')
test2 = input('Enter the score for test 2: ')
'''
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: '))


# Calculate the average test score. Add test1, test2, and test3 before the division.
'''
average = test1 + test2 + test3 / 3
'''
average = (test1 + test2 + test3) / 3

# Print the average.
print('The average score is', average)

# If the average is a high score,
# congratulate the user.

# Use the correct constant name and indent the code print('That is a great average!')
'''
if average >= high_score:
    print('Congratulations!')
print('That is a great average!')
'''
if average >= HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!')


#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 

def rectangle_area(length, width):
  return length * width

length1 = float(input("Enter the length of rectangle 1: "))
width1 = float(input("Enter the width of rectangle 1: "))

length2 = float(input("Enter the length of rectangle 2: "))
width2 = float(input("Enter the width of rectangle 2: "))

area1 = rectangle_area(length1, width1)
area2 = rectangle_area(length2, width2)

print("The area of rectangle 1 is:", area1)
print("The area of rectangle 2 is:", area2)

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

#Using the variables name and age, print a message to the user stating something along the lines of:
#"Happy birthday, name!  You are age years old today!"

name = input("Please enter your first name: ")
age = int(input("Please enter your age: "))
print("Happy birthday, " + name + "! You are " + str(age) + " years old today!")

