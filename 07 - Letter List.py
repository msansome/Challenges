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


# Main Program starts here.
letter = get_letter()
search_list(letter)
            

              
        
        
