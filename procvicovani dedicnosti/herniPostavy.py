import random

class Postava:
    def __init__(self, jmeno:str, zdravi:int):
        self.jmeno = jmeno
        self.zdravi = zdravi 
        pass

    def predstav_se(self):
        return f"Jmenuji se {self.jmeno} a moje aktuální zdraví je {self.zdravi}."

    def utok(self):
        return 0

#postava = Postava("Tonda", 100)
#print(postava.predstav_se())
#print(postava.utok())

class Rytir(Postava):
    def __init__(self, jmeno, zdravi, brneni:int):
        super().__init__(jmeno, zdravi)
        self.brneni = brneni

    def utok(self):
        poskozeni = random.randint(10, 20)
        return f"Seknul jsem mečem a způsobil {poskozeni} poškození."

    def zablokuj(self):
        return f"{self.jmeno} zvedá štít a brání se"


rytir = Rytir("Tonda", 100, 60)
#print(rytir.utok())
#print(rytir.brneni())
#print("-" * 40)



class Mag(Postava):
    def __init__(self, jmeno, zdravi, mana:int):
        super().__init__(jmeno, zdravi)
        self.mana = mana

    def utok(self):
        if self.mana >= 10:
            self.mana -= 10   #-= odečte manu a uloží její nový stav
            poskozeni = random.randint(25,40)
            return f"Seslal jsem kouzlo a způsobil {poskozeni} poškození."
        else:
            return "Nemám dost many, útočím jen slabě holí (poškození 5)."

mag = Mag("Hugo", 84, 20)
#print(mag.predstav_se())
#print(mag.utok())
#print("-" * 40)


class Lukostrelec(Postava):
    def __init__(self, jmeno, zdravi, toulec):
        super().__init__(jmeno, zdravi)
        self.toulec = toulec

    def utok(self):
        if self.toulec > 0:
            self.toulec -= 1
            poskozeni = random.randint(10, 25)
            return f"Vystřelil jsem šíp a způsobil {poskozeni} poškození."
        else:
            return "Došly mi šípy, útočím aspoň dýkou (poškození 3)."


lukostrelec = Lukostrelec("Legolas", 90, 3)
#print(lukostrelec.predstav_se())
#print(lukostrelec.utok())
#print("-" * 40)




druzina = [rytir, mag, lukostrelec]
for postavy in druzina:
    print(postavy.predstav_se())
    print(postavy.utok())
    print("-" * 40)