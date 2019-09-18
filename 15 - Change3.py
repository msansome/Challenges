'''
OCR 20 Coding Challenges

15 Change Return Program
========================

Extended Version 3: (With automated checker and US Currency)

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
# Note: We have to work in pence / cents to avoid rounding errors.

from random import randint


GBmoney = [2000,1000,500,200,100,50,20,10,5,2,1]
USmoney = [10000,5000,2000,1000,500,200,100,50,25,10,5,1]

GBcurrency = ["£20","£10","£5","£2","£1","50p","20p","10p","5p","2p","1p"]
UScurrency = ["$100","$50","$20","$10","$5","$2","$1","50c","25c","10c","5c","1c"]

sign ="£"



def make_change(amount):
    change = [] # A list to hold the numbers of notes / coins required.
    for i in money:
        change.append(int(amount // i)) # Go through and integer divide by each demonination
        amount = round((amount % i),2) # Do modulo division and round the result
        #print(amount)
    return change


############################
# Main Program Starts Here #
############################

usUK = input("Do you want to work in $USD or £GBP? : (U/G) ")
while usUK.lower() != "u" and usUK.lower() != "g":
    usUK = input("Please enter U or G: ")
if usUK.lower() == "u":     # It the user choses to work in $US Dollars
    money = USmoney[:]      # we will use the $US demoninations
    currency = UScurrency[:]
    sign = "$"
else:
    money = GBmoney[:]      # Otherwise we will stick to £GBP
    currency = GBcurrency[:]

cost = float(input(f"Please enter the cost of the product. {sign}"))
cost = cost * 100 # Work in pence / cents to avoid rounding errors
cash = float(input(f"Please enter the cash paid. {sign}"))
cash = cash * 100
while cash < cost:
    print("That's not enough to pay for your goods!")
    cash = float(input(f"Please enter the cash paid. {sign}"))
    cash = cash * 100

amount = round((cash - cost),2)
print(f"You will get {sign}{amount/100} change")
change = make_change(amount)
print(f"To make {sign}{amount/100} change you need:")
for i in range(len(money)):
    print(currency[i],"x",change[i])

# Automatic testing:
n = 1000
for i in range(n):  # We will run this n times to check for errors
                    # Uncomment the print statements only if n is small!
    #print()
    randCost = randint(1,10000)
    #print(f"The random cost is {sign}{randCost/100}")
    randCash = randint(randCost,10000)
    #print(f"The random cash you gave is {sign}{randCash/100}")
    randAmount = randCash - randCost
    #print(f"You will get {sign}{randAmount/100} change")
    #print(f"To make {sign}{randAmount/100} change you need:")
    change = make_change(randAmount)
##    for i in range(len(money)):
##        print(currency[i],"x",change[i])

    # Now check it adds up!
    total = 0
    for i in range(len(money)):
        total += money[i] * change[i]
    #print(f"That adds up to {sign}{total}")

    if total != randAmount:
        print("Oh dear. We have a problem! Please contact the programmer...")


    

