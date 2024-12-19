from CalcMethods import Addition

class Calculator:

    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)

    @classmethod
    def subtract(cls, num1, num2):
        num1 = -num1
        return Addition.add(num1, num2)

    @classmethod
    def multiply(cls, num1, num2):
        ans = num1
        for x in range(1,num2):
            ans = Addition.add(ans, num1)
        else:
            return ans

    @classmethod
    def divide(cls, num1, num2):
        num2 = -num2
        ans=0
        while num1 > 0:
            num1 = Addition.add(num1, num2)
            if num1 >= 0:
                ans=Addition.add(ans, 1)
        return ans

val1 = -1
val2 = -1
val1 = Addition.cleanupinput(val1)
val2 = Addition.cleanupinput(val2)

print(f'Sum: {Calculator.add(val1,val2)}')
print(f'Difference: {Calculator.subtract(val1,val2)}')
print(f'Product: {Calculator.multiply(val1,val2)}')
print(f'Quotient: {Calculator.divide(val1,val2)}')