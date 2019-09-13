'''
Possible answer to Q5 on the OCR 20 Coding Challenges
'''

names = []
name = input("Please enter a name ('xxx' to finish): ")
while name.lower() != "xxx":
    names.append(name)
    name = input("Please enter a name ('xxx' to finish): ")

order = input("Do you want to print the list in reverse order? (y/n): ").lower()
while not order.startswith("y") or order.startswith("n"):   
    print("Please say 'y' or 'n'")
    order = input("Do you want to print the list in reverse order? (y/n): ").lower()
if order == "y":
    backwards = names[::-1]
    for i in range(len(backwards)):
        print("%s. %s" %(i+1,backwards[i]))
else:
    for i in range(len(names)):
        print("%s. %s" %(i+1,names[i]))
    
    
    
    

