class Addition:

    @classmethod
    def add(cls,num1,num2):
        return (num1+num2)

    @classmethod
    def cleanupinput(cls, val):
        while val < 0:
            try:
                val = int(input('Enter a number: '))
                if val < 0:
                    raise NegativeError
            except (ValueError, TypeError, NegativeError):
                print("Enter a non-negative integer number!")
            else:
                return val

class NegativeError(Exception):
    pass

