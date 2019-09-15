'''
OCR 20 Coding Challenges

07 Letter list
==============

Version 1 - Basic task

Mark Sansome June 2018

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

lst = ["television","examination","boyfriend","criticism","possibility","psychology","temperature","data","marriage","exam","hospital","unit","village","quality","relation","mixture","measurement","department","climate","refrigerator","basis","honey","king","satisfaction","depression","priority","tea","entertainment","people","volume","bread","pie","friendship","chocolate","height","church","medicine","context","energy","inflation","finding","guidance","mom","understanding","growth","event","combination","diamond","technology","bath","salad","transportation","camera","law","election","resource","food","chest","emotion","decision","road","device","instance","republic","stranger","chemistry","analysis","garbage","poet","topic","arrival","impression","fact","alcohol","coffee","weakness","revolution","employment","mall","university","suggestion","attitude","winner","studio","difference","argument","theory","poem","language","charity","uncle","world","conclusion","cabinet","perspective","investment","wedding","shirt","drawing","error"]

def get_letter():
    letter = input("What letter would you like to search for? ")
    while not letter.isalpha() or len(letter) != 1:
        print("Please enter a single LETTER.")
        letter = input("What letter would you like to search for? ")
    letter = letter.lower()
    return letter



def search_list(letter):
    count = 0
    for i in range(len(lst)):
        if lst[i].startswith(letter):
            count += 1
            print (lst[i])
    print("There are %s words starting with '%s'." %(count, letter.upper()))


############################
# Main program starts here #
############################
letter = get_letter()
search_list(letter)
            

              
        
        
