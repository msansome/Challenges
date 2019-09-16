'''
OCR 20 Coding Challenges

10 Check if Palindrome
======================

Verion 2 - A slightly more sophistcated version (ignores spaces etc.)

Mark Sansome - June 2018

Check if Palindrome
Checks if the string entered by the user is a palindrome. A palindrome is a word
that reads the same forwards as it does backwards like “racecar”.
'''


testString = "Madam I'm Adam."

strg=input("Please enter a string to see if it is a palindrome: ")
# Remove spaces and punctuation from string
newString = ""
for i in strg:
        if i.isalpha():
                newString += i.lower()
                
newString2 = newString[::-1] # Make a copy of the string in reverse order

# Using new f string fomatting:
if newString == newString2:
    print(f'Yes! "{strg}" is a palindrome.')
else:
    print(f'No, Sorry, "{strg}" is not a palindrome.')
