'''
OCR 20 Coding Challenges

05 Basic lists
==============

Make a program that lets a user input a series of names into a list. The program should then
ask the user whether they want to print out the list in the original order, or in reverse.

Version 1 - Basic task only

Mark Sansome June 2018

Extensions:
1. Enable the user to choose what number item in the list they want to print out
2. Enable the user to only print out a ‘slice’ of the list (eg item three to item nine only)
3. Enable the user to remove any items of the list that they want to
4. Enable the user to save their list to a file for later, and also enable them to load it
back up again too
5. ‘Clean’ the list by making all the items lowercase.
'''

names = [] # A list to hold the names as they are typed
name = input("Please enter a name ('xxx' to finish): ")
while name.lower() != "xxx": # Need some way to stop
    names.append(name) # Add the name to the list
    name = input("Please enter a name ('xxx' to finish): ")

# Ask if the user wants the output reversed. Get the first letter of their answer and convert it to lower case.
ans = input("Do you want to print the list in reverse order? (y/n): ")[0]
## A method of schieving this more simply using Python-specific tools is:
#while not ans.startswith("y") and not ans.startswith("n"): 
while ans.lower() != "y" and ans.lower() != "n":
    print("Please say 'y' or 'n'")
    ans = input("Do you want to print the list in reverse order? (y/n): ")[0]
if ans == "y": # If yes - print list in reverse order
    backwards = names[::-1] # Python string slicing - Make a copy in reverse order
    for i in range(len(backwards)):
        print("%s. %s" %(i+1,backwards[i]))
        ## New 'f sting' method:
        #print(f'{i+1}. {backwards[i]}')
else:
    for i in range(len(names)):
        print("%s. %s" %(i+1,names[i]))
        #print(f'{i+1}. {names[i]}')
    
    
    
    

