'''
OCR 20 Coding Challenges

15 Change Return Program
========================

Extended Version: (With automated checker)

Mark Sansome September 2019

Change Return Program
The user enters a cost and then the amount of money given. You should write a
program that works out what denominations of change should be given in pounds,
50p, 20p, 10p etc.

Extensions:
1. The program will figure out the change for the American currency and the
number of quarters, dimes, nickels, pennies needed for the change
2. Make an automatic testing part of your program where it automatically
generates a random price and an amount that you give the cashier. It then works
out what change to give, and then tests that your program works by adding the
change back onto the price of the item to prove your program works. It should
flag an error if there are problems.

Possible answer to Q15 on the OCR 20 Coding Challenges
Calculate notes / coins to give as change
'''

from random import uniform

amount = 22.99
money = [20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
currency = ["£20","£10","£5","£2","£1","50p","20p","10p","5p","2p","1p"]


def make_change(amount):
    change = [] # A list to hold the numbers of notes / coins required.
    for i in money:
        change.append(int(amount // i)) # Go through and integer divide by each demonination
        amount = round(amount % i,2) # Do modulo division and round the result
        #print(amount)
    return change


############################
# Main Program Starts Here #
############################

cost = float(input("Please enter the cost of the product. £"))
cash = float(input("Please enter the cash paid. £"))
amount = round((cash - cost),2)
print(f"You will get £{amount} change")
change = make_change(amount)
print(f"To make £{amount} change you need:")
for i in range(len(money)):
    print(currency[i],"x",change[i])


# Automatic testing:
randCost = round(uniform(0.1,100),2)
print(f"The random cost is £{randCost}")
randCash = round(uniform(randCost,100),2)
print(f"The random cash you gave is £{randCash}")
randAmount = round((randCash - randCost),2)
print(f"You will get £{randAmount} change")
print(f"To make £{randAmount} change you need:")
change = make_change(randAmount)
for i in range(len(money)):
    print(currency[i],"x",change[i])

# Now check it adds up!
total = 0
for i in range(len(money)):
    total += round((money[i] * change[i]),2)
print(f"That adds up to £{total}")

if total != randAmount:
    print("Oh dear. We have a problem! Please contact the programmer...")


    

