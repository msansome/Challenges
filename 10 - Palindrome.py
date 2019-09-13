
'''
Possible answer to Q10 on the OCR 20 Coding Challenges
Palindrome Checker
'''


strg=input("Please enter a string to see if it is a palindrome: ")
strg1 = strg.lower()
strg2 = strg1[::-1]

if strg1 == strg2:
    print("Yes! \"%s\" is a palindrome." % strg)
else:
    print("No, Sorry, \"%s\" is not a palindrome." % strg)

