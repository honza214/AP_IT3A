import random

class Vozidlo: 
    def __init__(self, znacka:str, rok_vyroby:int, stav_nadrze:int = 100):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.stav_nadrze = stav_nadrze
        pass

    def zvuk_motoru(self):
        return "???"

    def infoOautu(self):
        return f"Moje značka je {self.znacka} a jsem z roku {self.rok_vyroby}"

    def startuj(self):
        if self.stav_nadrze > 0:
            return f"Úspěšně jsi nastartoval {self.zvuk_motoru()}"
        else:
            return "došla ti šťáva"



vozidlo = Vozidlo( "Škoda", "2016")
print(vozidlo.zvuk_motoru())
print(vozidlo.infoOautu())
print(vozidlo.startuj())
print("-" * 20)           #vypíše to 20x pomlčku pro přehlednost#


class Auto(Vozidlo):
    def __init__(self, znacka, rok_vyroby, typ_prevodovky: str, stav_nadrze = 100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.typ_prevodovky = typ_prevodovky

    def zvuk_motoru(self):
        return "Vrum vrum!"

    def zatrub(self):
        return "trubtrub"


auto =Auto("BMW", 2020,"automatická")
print(auto.znacka)
print(auto.rok_vyroby)
print(auto.typ_prevodovky)
print(auto.infoOautu())
print(auto.zvuk_motoru())
print(auto.zatrub())
print("-" * 20)    




class Moped(Vozidlo):
    def __init__(self, znacka, rok_vyroby, ma_slapadla:bool, stav_nadrze = 100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.ma_slapadla = ma_slapadla

    def zvuk_motoru(self):
        return "Trrrrr!"

    def slapej(self):
        if self.ma_slapadla:
            return "Šlapeme"
        else:
            return "Tento moped nemá šlapadla"

moped = Moped("Babetta", 1985, True)
print(moped.znacka)
print(moped.infoOautu())
print(moped.zvuk_motoru())
print(moped.startuj())
print(moped.slapej())

print("-" * 20)   

moped2 = Moped("Simson", 1990, False)
print(moped2.slapej())


garaz = [auto, moped]

for vozidlo in garaz:
    print(vozidlo.infoOautu())
    print(vozidlo.startuj())
    print("-" * 20)