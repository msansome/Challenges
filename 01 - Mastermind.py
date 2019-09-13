'''
OCR 20 Coding Challenges

01 Mastermind
=============
Extension Version:

© Mark Sansome June 2018

Generate a random four digit number. The player has to keep inputting four digit numbers until they guess the randomly generated number. After each unsuccessful try it should say
how many numbers they got correct, but not which position they got right. At the end of the game should congratulate the user and say how many tries it took.
Extensions:
1. Let the user pick an easy mode which shows the user which position that they guessed correctly
2. Let the user pick a hard mode that gives five digits instead of four
3. After the game is finished, ask the user for their name and input their score into a table. Show them the high score at the start of the game so that it gives a sense of competition.
'''
# ToDo: Extensions 1,2 & 3


from random import randint

length = 4
target=[]

def get_target():
    # Function to create the hidden number
    # This is stored as a string to make processing easier.
    for i in range(length):
        target.append(str(randint(0,9)))

    target_string = "".join(target)
    return target_string

    
def get_user_number():
    # User's guess - held as a string.
    user_input = input("Please enter your 4 digits: ")
    # Note: No error checking yet!
    return user_input


def score_it(input_numbers):
    all_right = False
    count = 0
    count_correct = 0
    test_numbers = target[::]   # Make a copy of the target numbers
                                # This is so we can delete items so that
                                # we don't count them more than once

    # First see how many of the user numbera are in the target number
    for i in range(len(input_numbers)):
        if input_numbers[i] in test_numbers:
            # Remove the first instance of that number so it can't be counted again
            test_numbers.remove(input_numbers[i])
            # Score this number as being present in the target
            count += 1
    print("You got", count, "right numbers.")
          
    # Next see how many are in the right position
    for i in range(len(input_numbers)):
        if input_numbers[i] == target[i]:
            count_correct += 1
    print(count_correct, "of them are in the right place.")
    
    # Finally, check if they are all in the right place
    # Note: we could also do this by checking if count_correct == len(target)
    if list(input_numbers) == target:
        all_right = True
    return all_right
        

# Main program starts Here:

target_string = get_target()

### Uncomment the line below if you want to see the hidden number (for testing)
#print(target, target_string)

all_right = False
goes = 0
while not all_right:
    num = get_user_number()
    all_right = score_it(num)
    goes += 1
print("Well Done!, You guessed the number correctly! You took",goes,"goes.")


