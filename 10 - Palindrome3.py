'''
OCR 20 Coding Challenges

10 Check if Palindrome
======================

Verion 3 - A Version Using Recursion 

NB - IMPORTANT:
Students are NOT expected to understand recursion at GCSE level!
(In fact not even in AS Level - Only A Level)

Mark Sansome - June 2018

Check if Palindrome
Checks if the string entered by the user is a palindrome. A palindrome is a word
that reads the same forwards as it does backwards like “racecar”.
'''

def isPalindrome(string):
	"""This is a recursive palidrome checker
	Returns True if string / list is palindromic
	(It works with lists too.)"""
	
	if len(string) <= 2:
		return string[0] == string[-1]
	else:
		if string[0] != string[-1]:
			return False
	#print(string[1:-1]) # for debugging
	# recursively call the function wrth the remainder of the string / list
	return isPalindrome(string[1:-1])

def stringPrep(string):
        # Remove spaces and punctuation from string
        newString = ""
        for i in string:
                if i.isalpha():
                        newString += i.lower()
        return newString


############################
# Main Program Starts Here #
############################


strg=input("Please enter a string to see if it is a palindrome: ")
newString = stringPrep(strg)

if isPalindrome(newString):
        print(f'Yes! "{strg}" is a palindrome.')
else:
        print(f'No, Sorry, "{strg}" is not a palindrome.')
    

### It works with lists too...
##txt_lst = ['m', 'a', 'd', 'a', 'm', 'i', 'm', 'a', 'd', 'a', 'm']
##num_lst = [4,5,6,6,5,4]
##print(isPalindrome(txt_lst))
##print(isPalindrome(num_lst))
##print(isPalindrome("Madam I'm Adam."))

