'''
OCR 20 Coding Challenges

06 Max and min list
===================

Basic Version - No Extensions

Mark Sansome June 2018

Max and min list
Write a program that lets the user input a list of numbers. Every time they
input a new number, the program should give a message about what the maximum and minimum numbers
in the list are.

Extensions

1. The program should let the user choose the allowable minimum and maximum
values, and should not let the user input something to the list that is
outside of these bounds
2. The user should be able to write these values to a file and then also read
them back out again.
3. If a file has any numbers outside of the boundaries, it should strip them
out of the list once it has read them in.
'''


# Get a list of integers from the user
numb = input("Please enter a number - XXX to finish: ")
maxi = int(numb)
mini = int(numb) # start by initialising both max and min to the first
                 # number entered 

while numb.upper() != "XXX":
    num = int(numb)
    if num > maxi:
        maxi = num
    if num < mini:
        mini = num
    print("Max =", maxi, "Min =", mini)
    numb = input("Please enter a number - XXX to finish: ")
