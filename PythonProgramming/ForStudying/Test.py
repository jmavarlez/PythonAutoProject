val=-1
while val < 0:
    try:
        val=int(input('Enter first number: '))
    except ValueError:
        print("Enter an integer number!")
    except TypeError:
        print("Enter an integer number!")
import sys
print(sys.path)