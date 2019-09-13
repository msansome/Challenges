'''
OCR 20 Coding Challenges

02 Averages
===========
Extension Version (With functions)

© Mark Sansome June 2018

Make a program that asks the user for a series of numbers until they either want
to output the average or quit the program.
Extensions:
1. Expand the program to print the median and mode averages also
2. Include options so that if the user wants to, they can save their list of numbers to a text file and read them back out later on.

ToDo: Extension 2 - Saving lists
'''

lst=[]

def getNums():
    # Get a list of integers from the user
    numb = input("Please enter a number - XXX to finish: ")

    while numb.upper() != "XXX":
        lst.append(int(numb))
        numb = input("Please enter a number - XXX to finish: ")
    return lst

def calcAverage():
    total = 0
    for i in range(0,len(lst)):
        total += lst[i]
    ave = total / len(lst)
    return ave


def calcMedian():
    # Part 2a - Median
    lst.sort() # Sort the list (the median will be the mid point)
    mid = len(lst) // 2 # Integer division to find mid point of list

    if len(lst) % 2 != 0: # Check to see if there are an even number of items
        median = lst[mid] # If not, the median is just the middle item
    else:
        median = (lst[mid-1] + lst[mid])/2 # If even no. of items the median is the
                                           # average of the two in the middle
    return median



def calcMode():
    # Part 2b - Mode

    # Note: This will not work if the list is bi-modal (more work needed)
    maximum = 0
    mode = 0
    for i in lst:
        count = lst.count(i)
        if count > maximum and count > 1:
            maximum = count
            mode = i
    return mode, maximum
       
    
    
# Print out the answers:
getNums()
print(lst)
avg = calcAverage()
median = calcMedian()
mode, maximum = calcMode()

print("The average of your",len(lst),"numbers is",avg)
    
print("The median of your",len(lst),"numbers is",median)

print("The mode of your",len(lst),"numbers is",mode, "which has", maximum, "occurrences.")

