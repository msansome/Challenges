'''
Possible answer to Q6 on the OCR 20 Coding Challenges
Max Min
'''


lst=[]

def getNums():
    maxi = 0
    mini = 999
    # Get a list of integers from the user
    numb = input("Please enter a number - XXX to finish: ")

    while numb.upper() != "XXX":
        lst.append(int(numb))
        num = int(numb)
        if num > maxi:
            maxi = num
        if num < mini:
            mini = num
        print("Max =", maxi, "Min =", mini)
        numb = input("Please enter a number - XXX to finish: ")
    return lst

getNums()
