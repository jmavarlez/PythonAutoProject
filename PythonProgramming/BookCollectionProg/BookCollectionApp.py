import os
from Util import DataMethods

class BookCollection:
    choicedict = {
        "add": DataMethods.DataFunc.addbook,
        "show": DataMethods.DataFunc.listallbooks,
        "read": DataMethods.DataFunc.readbook,
        "show read": DataMethods.DataFunc.listallreadbooks,
        "delete": DataMethods.DataFunc.deletebook
    }

    @classmethod
    def menu(cls):
        ans=''
        while ans != 'quit':
            os.system('cls')
            try:
                ans = input("How can I help you? "
                    "\nType 'Add' to add a book in your collection"
                    "\nType 'Show' to list all books in your collection"
                    "\nType 'Read' to read books in your collection"
                    "\nType 'Show Read' to list all read books in your collection"
                    "\nType 'Delete' to delete a book in your collection"
                    "\nType 'Quit' to exit the collection"
                    "\nWhat do you want to do: ").lower()
                os.system('cls')
                if ans in BookCollection.choicedict:
                    BookCollection.choicedict[ans]()
                elif ans == "quit":
                    break
                    input("Thank you. Press enter to exit.")
                else:
                    raise DataMethods.InputNotValidError
            except DataMethods.InputNotValidError:
                input(f'{ans} is not a valid input!')

BookCollection.menu()

