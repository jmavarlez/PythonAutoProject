import csv

class DataFunc:
    datafile = 'Util/data.csv'

    @classmethod
    def addbook(cls):
        bookcol = cls.convertdatatodict()
        bookname = input("Book Name: ")
        bookauth = input("Book Author: ")
        readbool = True
        while readbool:
            try:
                bookread = input("Have you read this book? (yes/no): ").lower()
                if bookread == 'yes':
                    bookread = 'True'
                    readbool = False
                elif bookread =='no':
                    bookread = 'False'
                    readbool = False
                else:
                    raise InputNotValidError
            except InputNotValidError:
                input(f'{bookread} is not a valid input!')

        bookcol.append({'Name': bookname, 'Author': bookauth, 'Read': bookread})
        cls.writedicttofile(bookcol)
        cls.displaycollection(cls.convertdatatodict())
        input('Press any key to continue...')

    @classmethod
    def readbook(cls):
        bookcol = cls.convertdatatodict()
        try:
            bookname = input("Enter the name of the book you want to read: ")
            for movie in bookcol:
                if movie['Name'].lower() == bookname.lower():
                    if movie["Read"] == 'True':
                        raise BookAlreadyReadError
                    elif movie["Read"] == 'False':
                        movie["Read"] = 'True'
                        cls.writedicttofile(bookcol)
                        cls.displaycollection(cls.convertdatatodict())
                        input('Press any key to continue...')
                        break
            else:
                raise BookNotExistingError
        except BookNotExistingError:
            input(f'{bookname} does not exist in your collection. Press any key to continue.')
        except BookAlreadyReadError:
            input(f'{bookname} is already read. Press any key to continue.')


    @classmethod
    def deletebook(cls):
        bookcol = cls.convertdatatodict()
        try:
            bookname = input("Enter the name of the book you want to delete: ")
            for counter, movie in enumerate(bookcol):
                if movie['Name'].lower() == bookname.lower():
                    del bookcol[counter]
                    input(f'{bookname} is now deleted in your collection.')
                    cls.writedicttofile(bookcol)
                    cls.displaycollection(cls.convertdatatodict())
                    input('Press any key to continue...')
                    break
            else:
                raise BookNotExistingError
        except BookNotExistingError:
            input(f'{bookname} does not exist in your collection. Press any key to continue.')

    @classmethod
    def listallbooks(cls):
        cls.displaycollection(cls.convertdatatodict())
        input('Press any key to continue...')

    @classmethod
    def listallreadbooks(cls):
        bookcol = cls.convertdatatodict()
        for movie in bookcol:
            if movie['Read'] == 'True':
                print(f'{movie['Name']} written by {movie['Author']}')
        input('Press any key to continue...')

    @classmethod
    def convertdatatodict(cls):
        with open(DataFunc.datafile, 'r') as file:
            #bookdict = list(csv.DictReader(file))
            bookdict = list(csv.DictReader(file, fieldnames=('Name', 'Author', 'Read'), lineterminator='\n'))
        return bookdict

    @classmethod
    def writedicttofile(cls, collection):
        with open(DataFunc.datafile, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=('Name', 'Author', 'Read'), lineterminator='\n')
            writer.writerows(collection)

    @classmethod
    def displaycollection(cls,collection):
        print('Here is your movie collection:')
        for movie in collection:
            print(f'{movie['Name']} written by {movie['Author']} : Read Status: {movie['Read']}')

class InputNotValidError(Exception):
        pass

class BookNotExistingError(Exception):
    pass

class BookAlreadyReadError(Exception):
    pass