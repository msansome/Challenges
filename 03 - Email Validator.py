'''
OCR 20 Coding Challenges

03 Email validator
==================

© Mark Sansome June 2018

Email validator
Make a program to check whether an email address is valid or not.
For instance, you could make sure that there are no spaces, that there is an @ symbol and a dot somewhere after it. Also check the length of the parts at the start, and that the end parts
of the address are not blank.
Extensions:
1. When an email address is found to be invalid, tell the user exactly what they did wrong with their email address rather than just saying it is invalid
2. Allow the user to choose to give a text file with a list of email addresses and have it process them all automatically.

'''
# ToDo: Extension task 2


def email_check(email):
    good_mail = True
    at_sign = email.find('@') # Returns postion of character or -1 if not found
    dots = [pos for pos, char in enumerate(email) if char == "."]
    # This list comprehension will produce a list of all of the positions of "." in the
    # email address (there can be more than one)

    if " " in email:
        good_mail = False # email should not have a space in it.
        err_msg = "Email addresses must not contain spaces"
    if at_sign == -1:
        good_mail = False # email should have a "@" in it.
        err_msg = "There is no '@' symbol in your email address"
    if dots==[] or dots[-1] < at_sign:
        good_mail = False # last "." should come AFTER "@".
        err_msg = "Invalid domain after the '@'"
    if email[:at_sign] == "":
        good_mail = False # Checks to see if blank before "@" symbol.
        err_msg = "You must have a name before the '@' symbol"
    if dots==[] or len(email[dots[-1]+1:]) < 2:
        good_mail = False # Checks to see if final domain section is > 2 characters.
        err_msg = "You need a valid domain name after the '.'"

    if not good_mail:
        print("Sorry, that is an invalid email address.")
        print(err_msg,"Please try again.")


    return good_mail


# Main Program Starts Here:

ok = False
while not ok:
    email = input("Please enter your email address: ")
    ok = email_check(email)
