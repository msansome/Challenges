'''
OCR 20 Coding Challenges

15 Change Return Program
========================

Basic Version:

Mark Sansome September 2018

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
# Note: We have to work in pence to avoid rounding errors.



money = [2000,1000,500,200,100,50,20,10,5,2,1]
currency = ["£20","£10","£5","£2","£1","50p","20p","10p","5p","2p","1p"]


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

cost = float(input("Please enter the cost of the product. £"))
cost = cost * 100 # Work in pence to avoid rounding errors
cash = float(input("Please enter the cash paid. £"))
cash = cash * 100
while cash < cost:
    print("That's not enough to pay for your goods!")
    cash = float(input("Please enter the cash paid. £"))
    cash = cash * 100

amount = round((cash - cost),2)
print(f"You will get £{amount/100:.2f} change") # :.2f means display 2DP
change = make_change(amount)
print(f"To make £{amount/100:.2f} change you need:")
for i in range(len(money)):
    print(currency[i],"x",change[i])
    

