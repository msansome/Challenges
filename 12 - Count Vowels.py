'''
OCR 20 Coding Challenges

11 Count Vowels
===============

Verion 1 - A very simple approaches to this task this task

Mark Sansome - September 2019

Count Vowels
Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.
'''


### Basic Version

vowels = "aeiou"
testString = "Counts the number    of individual words in a string. For added complexity, the program could read these strings in from a text file and generate a summary"
vowelCount = 0
### Or we could ask the user for a string:
#testString = input("Please Enter your Own String : ")


for i in range(len(testString)):
    if testString[i].lower() in vowels:
        vowelCount += 1

print("The number of vowels in the string is", vowelCount)


### Extended Version
print()

vowelCount = 0
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for i in range(len(testString)):
    if testString[i].lower() == "a":
        count_a += 1
    elif testString[i].lower() == "e":
        count_e += 1
    elif testString[i].lower() == "i":
        count_i += 1
    elif testString[i].lower() == "o":
        count_o += 1
    elif testString[i].lower() == "u":
        count_u += 1

vowelCount = count_a + count_e + count_i + count_o + count_u

print("There are:")
print(count_a, "As")
print(count_e, "Es")
print(count_i, "Is")
print(count_o, "Os")
print(count_u, "Us")
print("The total number of vowels in the string is", vowelCount)
