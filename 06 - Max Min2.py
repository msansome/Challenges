'''
OCR 20 Coding Challenges

06 Max and min list
===================

Version 2 - With Extension tasks

Mark Sansome September 2019

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


def getNums():
    ''' This functio will get a list of integers from the user
       It will write them into the 'numlist' array'''
    numb = input(f"Please enter a number between {lowerB} and {upperB} - XXX to finish: ")
    while numb.upper() != "XXX":
        numb = int(numb)
        if numb >= lowerB and numb <= upperB:
            numlist.append(numb)
        else:
            print(f"Sorry. That number is not betweem {lowerB} and {upperB}.")
        numb = input("Please enter a number - XXX to finish: ")

def findMaxMin(lowerB, upperB):
    ''' This function will find the maximum and minimun entries in the 'numlist' array'''
    if len(numlist) == 0: # If the list is empty reset max & min to 0
        maxi = 0
        mini = 0
    else:
        maxi = lowerB
        mini = upperB
        for i in numlist:
            if i > maxi:
                maxi = i
            if i < mini:
                mini = i
    return maxi, mini

def readfile(filename):
    ''' This function will attempt to open the file as defined by "filename".
        if it doesn't exist it will simply call the getNums fuction to start creating
        a list of numbers. This will later be written to the file.'''
    
    try: # Only open if the file exists
        with open(filename, 'r') as filehandle:
            contents = filehandle.readlines()
            for numb in contents:
                numb = int(numb[:-1]) # Strip off the CR and convert the string to an int
                if numb >= lowerB and numb <= upperB:
                    numlist.append(numb) # If it's between the upper and lower bounds add it to the list
    except FileNotFoundError: # The file does not exist so tell the user and start a new list.
        print("The file does not exist. It will be created now...")
        getNums()

def writefile(filename):
    ''' This funcion will write the list to the file as defined by "filename".
        It will write the integer plus a newline character.'''
    with open(filename, 'w+') as file:  # w+ will create the file if it doesn't exist
        for numb in numlist:
            file.write(f"{numb}\n")         # Save number with a New Line

def answerYes(message):
    ''' Reusable Yes/No function.'''
    yes = False
    ans = input(message)
    ans = ans[0].lower()
    while ans != "y" and ans != "n":
        ans = input(message)
    if ans == "y":
        yes = True
    return yes

def upperLower():
    ''' This function will get upper and lower bounds for the list from the user.
        If not set, it will use the default values'''
    upperB = 1000 # Default Values
    lowerB = 1
    if answerYes(f"Do you wish to set upper and lower limits? (default {lowerB}-{upperB}) Y/N : "):
        lowerB = int(input("Please enter the lower limit: "))
        upperB = int(input("Please enter the upper limit: "))
    return lowerB, upperB


############################
# Main program starts here #
############################

numlist=[] # Empty list to store the integers
filename = "list_of_numbers.txt" # Filename of the file to be written / read

    
lowerB, upperB = upperLower() # Get upper and lower bounds for the list
if answerYes("Do you wish to load the last list saved to file? (Y/N): "):
    print(f"Note: The numbers loaded will be restrict to the upper and lower bounds of {lowerB}-{upperB}.")
    readfile(filename)
else:
    getNums() # Start a new list
print(numlist)
high, low = findMaxMin(lowerB, upperB)
print("Max =", high, "Min =", low)
writefile(filename) # Save the list to a file for next time


'''
###Alternative method to read / write to file

with open(filename, 'w') as filehandle:
    for listitem in numbs[:-1]:             # Write all but the last entry
        filehandle.write(f'{listitem},')    # with a comma after it.
    filehandle.write(f'{numbs[-1]}\n')      # Write the last entry with a newline
                                            # after it.

with open(filename, 'r') as filehandle:
    filecontents = filehandle.readlines()   # read in the file
    filecontents = filecontents[0]          
    print(filecontents)
    newthing = filecontents.split(",")
    for i in range (len(newthing)):
        newthing[i] = int(newthing[i])
    print(newthing)
'''
