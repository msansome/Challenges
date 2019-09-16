'''
OCR 20 Coding Challenges

11 Count Words in a String
==========================

Verion 1 - A couple of very simple approaches to this task this task

Mark Sansome - June 2018

Count Words in a String
Counts the number of individual words in a string. For added complexity,
the program could read these strings in from a text file and generate a summary.
'''

testString="Counts the number    of individual words in a string. For added complexity, the program could read these strings in from a text file and generate a summary"

### Or we could ask the user for a string:
###testString = input("Please Enter your Own String : ")


# Method 1 : No special Python tools:
# Note: This simple version relies on the fact that words are split
#       by a single space, a newline, or a tab.
#       This could be improved upon

total = 1 # We start from 1 because the first space comes after the first word usually.

for i in range(len(testString)):
    if(testString[i] == ' ' or testString[i] == '\n' or testString[i] == '\t'):
        total = total + 1

print("The number of words in the string is", total)




### Method 2 : Using the Python command .split

lst = testString.split() # .split splits on whitespace and puts the words into a list.
print ("The number of words in the string is", len(lst))

