'''
OCR 20 Coding Challenges

10 Check if Palindrome
======================

Verion 1 - A very simple method of achieving this task

Mark Sansome - June 2018

Check if Palindrome
Checks if the string entered by the user is a palindrome. A palindrome is a word
that reads the same forwards as it does backwards like “racecar”.
'''


strg=input("Please enter a string to see if it is a palindrome: ")
strg1 = strg.lower()
strg2 = strg1[::-1]

##if strg1 == strg2:
##    print("Yes! \"%s\" is a palindrome." % strg)
##else:
##    print("No, Sorry, \"%s\" is not a palindrome." % strg)

# Using new f string fomatting:
if strg1 == strg2:
    print(f'Yes! "{strg}" is a palindrome.')
else:
    print(f'No, Sorry, "{strg}" is not a palindrome.')
