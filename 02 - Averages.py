'''
OCR 20 Coding Challenges

02 Averages
===========
Basic Version

© Mark Sansome June 2018

Make a program that asks the user for a series of numbers until they either want
to output the average or quit the program.
Extensions:
1. Expand the program to print the median and mode averages also
2. Include options so that if the user wants to, they can save their list of numbers to a text file and read them back out later on.
'''


numb = input("Please enter a number - XXX to finish: ")
total = 0
count = 0
# Repeatedly ask for user to input numbers

while numb.upper() != "XXX":
    numb = int(numb)
    total += numb # Keep a running total
    count += 1 # Increment the count
    numb = input("Please enter a number - XXX to finish: ")
ave = total / count # Calculate the average

print("The average of your",count,"numbers is",ave)
    
