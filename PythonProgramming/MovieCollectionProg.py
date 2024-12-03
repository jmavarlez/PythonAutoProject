"""
Demonstrates:
Functions
Loops and Conditionals
"""


import os
listofmovies = []
ans = ''

def printmovie(movies):
    print(f"{movies["Name"]}, directed by {movies["Director"]}, released on {movies["ReleaseDate"]}")

def addmovie():
    print ("Add a Movie")
    moviename = input("Movie Name: ")
    moviedir = input("Movie Director: ")
    movierel = input("Movie Release Date (mm/yy): ")
    listofmovies.append({"Name": moviename, "Director": moviedir, "ReleaseDate": movierel,})
    input("Movie was added in your collection. Press enter to continue.")


def showmovie():
    for movies in listofmovies:
        printmovie(movies)
    input("Press enter to continue.")


def searchmovie():
    movietitle = input("Enter the movie title to be searched: ").lower()
    for movies in listofmovies:
        if movietitle == movies["Name"].lower():
            print("This movie exists in your collection")
            printmovie(movies)
            break
    else:
        print(f"{movietitle} does not exist in your collection")
    input("Press enter to continue.")


def deletemovie():
    movietitle = input("Enter the movie title you want to delete: ").lower()
    for counter, movies in enumerate(listofmovies):
        if movietitle == movies["Name"].lower():
            del listofmovies[counter]
            print(f"{movies["Name"]} is now deleted in your collection.")
            break
    else:
        print(f"{movietitle} does not exist in your collection")
    input("Press enter to continue.")


optionsdict = {
    "add": addmovie,
    "show": showmovie,
    "search": searchmovie,
    "delete": deletemovie
}

while ans != 'quit':
    os.system('cls')
    ans = input("How can I help you? "
                "\nType 'Add' to add a movie in your collection"
                "\nType 'Show' to list all movies in your collection"
                "\nType 'Search' to search for a specific movie in your collection"
                "\nType 'Delete' to delete a movie in your collection"
                "\nType 'Quit' to exit the collection"
                "\nWhat do you want to do: ").lower()
    os.system('cls')
    if ans in optionsdict:
        optionsdict[ans]()
    elif ans == "quit":
        break
        input("Thank you. Press enter to exit.")
    else:
        input("Invalid option. Press enter to input again.")


