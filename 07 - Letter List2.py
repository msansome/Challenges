'''
OCR 20 Coding Challenges

07 Letter list
==============

Version 2 - With Extension task 1

Mark Sansome - September 2019

Letter list
Write a program that lets a user choose a letter. The program will then find
all the words beginning with that letter in a list and print them out. It should
also say how many words it found.

Extensions:

1. Let the user load up a list of words from a file and have the program process
them all
2. Change the program so that the user can choose whether they want all words
with only the start of the letter, or ANY place in the word.
'''

wordlist = ["television","examination","boyfriend","criticism","possibility","psychology","temperature","data","marriage","exam","hospital","unit","village","quality","relation","mixture","measurement","department","climate","refrigerator","basis","honey","king","satisfaction","depression","priority","tea","entertainment","people","volume","bread","pie","friendship","chocolate","height","church","medicine","context","energy","inflation","finding","guidance","mom","understanding","growth","event","combination","diamond","technology","bath","salad","transportation","camera","law","election","resource","food","chest","emotion","decision","road","device","instance","republic","stranger","chemistry","analysis","garbage","poet","topic","arrival","impression","fact","alcohol","coffee","weakness","revolution","employment","mall","university","suggestion","attitude","winner","studio","difference","argument","theory","poem","language","charity","uncle","world","conclusion","cabinet","perspective","investment","wedding","shirt","drawing","error"]

def get_letter():
    letter = input("What letter would you like to search for? ")
    while not letter.isalpha() or len(letter) != 1:
        print("Please enter a single LETTER.")
        letter = input("What letter would you like to search for? ")
    letter = letter.lower()
    return letter



def search_list(letter):
    count = 0
    for i in range(len(wordlist)):
        if wordlist[i].startswith(letter):
            count += 1
            print (wordlist[i])
    print("There are %s words starting with '%s'." %(count, letter.upper()))

def readfile(filename):
    wordlist = [] # Blank the word list
    ''' This function will attempt to open the file as defined by "filename".
        if it doesn't exist it will simply ask again'''
    
    try: # Only open if the file exists
        with open(filename, 'r') as filehandle:
            contents = filehandle.readlines()
            for word in contents:
                word = word[:-1] # Strip off the CR and convert the string to an int
                wordlist.append(word)
    except FileNotFoundError: # The file does not exist so tell the user and start a new list.
        print("Sorry, That file does not exist.")
        if answerYes("Do you want to try again? (Y/N): "):
            getFileName()

def getFileName():
    print("Please enter the name of the file. Note: it must be typed exactly (including")
    print("the file extension).")
    print('The default file is "wordlist.txt". Type "ENTER" to select this file')
    fname = input('or type the filename: ')
    if fname == "":
        fname = "wordlist.txt"
    return fname
          

def writefile(filename):
    ''' This funcion will write the list to the file as defined by "filename".
        It will write each word plus a newline character.'''
    with open(filename, 'w+') as file:  # w+ will create the file if it doesn't exist
        for word in wordlist:
            file.write(f"{word}\n")         # Save number with a New Line

def answerYes(message):
    ''' Reusable Yes/No function.'''
    yes = False
    ans = input(message)
    ans = ans[0].lower()
    while ans != "y" and ans != "n":
        ans = input(message)
    if ans == "y":
        yes = True
    return yes


############################
# Main program starts here #
############################
fname = "wordlist.txt"
if answerYes("Do you want to load a list of words from a file? (Y/N): "):
          fname = getFileName()
          readfile(fname)

letter = get_letter()
search_list(letter)
if answerYes("Do you want to save the list to a file? (Y/N): "):
    writefile(fname)
            

              
        
        
