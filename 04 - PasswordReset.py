'''
OCR 20 Coding Challenges

04 Password Reset Program
=========================

Version 1 - Non Python Specific Code
(See Version 2 for version usin Python tools)

© Mark Sansome June 2018

Password reset program
Only accept a new password if it is:
1. At least eight characters long
2. Has lower case and upper case letters.
The password reset program should also make the user input their new password
twice so that the computer knows that the user has not made any mistakes when
typing their new password.
Extensions:
1. Make some sort of algorithm to suggest how strong the password is
(Weak, Medium, Strong) depending on length, whether or not the password has
special characters in etc.
2. Let the user input their username. The program should go to a text file
with a list of usernames and old passwords, and the program should only let
you change your password if you input your old password.
'''
# ToDo: Extension Task 2
# ToDo: make goodPwd into a function

def pwdAnalyse(pwd):
    special="!#$£%&()*+,-/.:;<=>?{|}~@"
    upr = 0
    lwr = 0
    num = 0
    spc = 0

    for i in pwd:
        asc = ord(i)
        if i in special:
            spc += 1
        if asc >= 48 and asc <= 57:
            num += 1
        if asc >= 65 and asc <= 90:
            upr += 1
        if asc >= 97 and asc <= 122:
            lwr += 1
    return upr, lwr, num, spc


# Main Program starts here

goodPwd = False
while not goodPwd:
    pwd1 = input("Please enter a suitable password: ")
    while len(pwd1) < 8:
        print("Your password must be at least 8 characters")
        pwd1 = input("Please enter a suitable password: ")
        
    pwd2 = input("Please re-enter your suitable password: ")
    while pwd2 != pwd1:
        print("The passwords do not match! Please try again")
        pwd2 = input("Please re-enter your suitable password: ")
    upr, lwr, num, spc = pwdAnalyse(pwd1)
    if upr < 1 or lwr < 1:
        print("Sorry your password must include at least one upper case and one lower case character")
        print("Please try again")
    else:
        goodPwd = True

    
print("Your password is", len(pwd1), "characters")
print("There are",upr, "upper-case characters in the password")
print("There are",lwr, "lower-case characters in the password")
print("There are",num, "numbers in the password")
print("There are",spc, "special characters in the password")
        
