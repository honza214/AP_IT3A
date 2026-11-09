import random
from datetime import datetime

class Car:
    def __init__(self, brand:str, model:str, year:int,stkYear:int, fuel:int = 100):
        self.brand = brand
        self.model = model
        self.year = year
        self.stkYear = stkYear
        self.fuel = fuel
        pass

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - fuel: {self.fuel}"
    
    def move(self):
        usage = random.randint(5,20)
        if self.fuel >= usage:
            self.fuel -= usage
            return f"{self.brand} {self.model} spotřeboval {usage} % a palivo má {self.fuel} %"
        else:
            return f"{self.brand} {self.model} by do cile nedojel. Potřebuje {usage} % paliva a ma jen {self.fuel} %"

    def natankuj(self):
        filled = 100 - self.fuel
        self.fuel = 100
        return f"{self.brand} {self.model} natankoval {filled} % paliva"
    
    def STK(self):
        if self.stkYear < datetime.now().year:
            return f"{self.brand} {self.model} musí na technickou. Technická skončila v roce {self.stkYear}."
        else:
            return f"{self.brand} {self.model} je v pohodě a na technickou bude muset za následujících počet let: {self.stkYear - datetime.now().year}."


car1 = Car("Škoda", "Octavia 3", 2016, 2026, 85)
car2 = Car("Hyundai", "Getz", 2009, 2022, 3)
car3 = Car("Toyota", "Hilux", 2014, 2028, 34)

#testovaci vypis
print(car1)
print(car2)
print(car3)
print("-" * 40)
print(car1.move())
print(car1.natankuj())
print(car1.move())
print("-" * 40)
print(car2.move())
print(car2.natankuj())
print(car2.move())
print("-" * 40)


#testování Technické u auta s DATETIME
print(car1.STK())
print(car2.STK())
print(car3.STK())
print("-" * 40)

class Garage:
    def __init__(self, name:str):
        self.name = name
        self.cars = []
        pass

    def addCar(self, car:(Car)):
        self.cars.append(car)
        return f"Do garáže {self.name} bylo přidáno auto {car.model}"
    
garage = Garage("Baxtrix")
print(garage.addCar(car1))
print(garage.addCar(car2))
print(garage.addCar(car3))
print("-" * 40)