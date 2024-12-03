"""
Demonstrates:
Class as Parameter
Error Handling
"""

class Collection:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __repr__(self):
        return f'{self.brand}: {self.model}'

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return (len(self.cars))

    def __str__(self):
        return self.cars

    def addcar (self, car):
        if not isinstance(car, Collection):
            raise TypeError(f"{car.__class__.__name__} is not a Collection car!")
        self.cars.append(car)

car = Garage()
carcol1 = Collection("Toyota", "Fortuner")
car.addcar(carcol1)
carcol2 = Collection("Mitsubishi", "Montero")
car.addcar(carcol2)
print(car.cars)