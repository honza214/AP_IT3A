import random
from datetime import datetime
class Animal:
    def __init__(self, species:str, name:str, birthYear:int, checkupYear:int = 0, energy:int = 100):
        self.species = species
        self.name = name
        self.birthYear = birthYear
        self.checkupYear = checkupYear
        self.energy = energy

        if self.energy >= 100:
            self.energy = 100
        elif self.energy < 0:
            self.energy = 0
        pass

    def __str__(self):
        return f" {self.species} {self.name} {self.birthYear} energy: {self.energy}"
    
    def play(self):
        usage = random.randint(5,20)
        if self.energy >= usage:
            self.energy -= usage
            return f"{self.species} {self.name} spotřeboval při hře {usage} % energie a zbývá mu {self.energy}%"
        else:
            return f"{self.species} {self.name} je moc unavený. Potřebuje {usage} % energie, ale má jen {self.energy}"
        
    def feed(self):
        filled = 100 - self.energy
        self.energy = 100
        return f"{self.species} {self.name} byl nakrmen a doplnil {filled}% energie"

    def vetCheck(self):
        if self.checkupYear < datetime.now().year:
             return f"{self.species} {self.name} musí k veterináři - platnost prohlídky skončila v roce {self.checkupYear}"
        else:
            return f"{self.species} {self.name}má prohlídku v pořádku. Další kontrola bude za následující počet let:  {self.checkupYear - datetime.now().year}."



animal1 = Animal("Lev", "Alex", 2016, 2026, 85)
animal2 = Animal("zebra", "Marty", 2018, 2022)
animal3 = Animal("Lev", "Simba", 2020, 2024, 40)
print(animal1)
print(animal1.play())
print(animal1.feed())
print(animal1.vetCheck())
print("-" *50)

print(animal2)
print(animal2.play())
print(animal2.feed())
print(animal2.vetCheck())
print("-" *50)

print(animal3)
print(animal3.play())
print(animal3.feed())
print(animal3.vetCheck())
print("-" *50)



