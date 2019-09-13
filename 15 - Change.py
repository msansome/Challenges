'''
Possible answer to Q15 on the OCR 20 Coding Challenges
Calculate notes / coins to give as change
'''


amount = 22.99
money = [20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
currency = ["£20","£10","£5","£2","£1","50p","20p","10p","5p","2p","1p"]


def make_change(amount):
    change = []
    for i in money:
        change.append(int(amount // i))
        amount = round(amount % i,2)
        #print(amount)
    return change

change = make_change(amount)
print("To make £%s change you need:"%amount)
for i in range(len(money)):
    print(currency[i],"x",change[i])
    

