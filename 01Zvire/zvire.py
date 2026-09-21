import random

class Zvire:
    def __init__(self, jmeno: str, vek: int, misto: str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto

    def zvuk(self):
        return "???"

    def predstavSe(self):
        return f"Jmenuji se {self.jmeno}, a je mi {self.vek} let."

    def Kdejsi(self):
        return f"jsem v místě zvaném {self.misto}."

    def JdiNa(self, nMisto: str):
        self.misto = nMisto
        return f"Přesunul jsem se na {nMisto}, {self.Kdejsi()}"
    

zvire = Zvire("Tonda", 67)
print(zvire.jmeno)
print(zvire.vek)
print(zvire.zvuk())

print("-" * 20)


zvire2 = Zvire("Crocs", 8, "Sklep")
print(zvire2.jmeno)
print(zvire2.vek)
print(zvire2.misto)
print(zvire2.zvuk())
print(zvire2.predstavSe())
print(zvire2.Kdejsi())
print(zvire2.JdiNa("Škola"))

print("-" * 20)

class Pes(Zvire):
    def __init__(self, jmeno, vek, plemeno, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.plemeno = plemeno

    def zvuk(self):
        return "hafhaf"
    
    def aport(self):
        return f"{self.jmeno} přinesl míček."
    
    def vycesat(self):
        if(random.randint(0,1) > 0):
            return f"{self.jmeno} utekl před tvým kartáčem!"
        else:
            return f"{self.jmeno} nechal se vyčesat"
        
    def predstavSe(self):
        return f"{super().predstavSe()} jsem {self.plemeno}"
            
    
pes = Pes("Hugo", 6, "Australský ovčák", "na gauči")

print(pes.jmeno)
print(pes.plemeno)
print(pes.zvuk())
print(pes.predstavSe())
print(pes.aport())
print(pes.vycesat())
print(pes.Kdejsi())
print(pes.predstavSe())

print("-" * 20)           #vypíše to 20x pomlčku pro přehlednost#


class Kocka(Zvire):
    def __init__(self, jmeno, vek, barva, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.barva = barva

    def zvuk(self):
        return "mnaumnau"
    
    def utok(self):
        return f"{self.jmeno} te poškrábal"
    
    def pohladit(self):
        if(random.randint(0,1) > 0):
            return f"{self.jmeno} vrniii"
        else:
            return f"{self.jmeno} se nenechal pohladit"
    


kocka = Kocka("Arašíd", 2, "zrzek", "na gauči")

print(kocka.jmeno)
print(kocka.barva)
print(kocka.zvuk())
print(kocka.utok())
print(kocka.pohladit())


print("-" * 20)


class Papousek(Zvire):
    def __init__(self, jmeno, vek,barvaPeri, misto = "Klec"):
        super().__init__(jmeno, vek, misto)
        self.barvaPeri = barvaPeri

    def zvuk(self):
        return "krakrak"
    
    def opakuj(self, slovo:str):
        return f"{self.jmeno} opakuje: {slovo} {slovo}"
    

papousek = Papousek("Vidlák", 2, "zelená")

print(papousek.jmeno)
print(papousek.vek)
print(papousek.barvaPeri)
print(papousek.zvuk())
print(papousek.opakuj("Vidlák"))


print("-" * 20)


class Had(Zvire):
    def __init__(self, jmeno, vek, delkavCM:int,jedovaty:bool, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.delkavCM = delkavCM
        self.jedovaty = jedovaty

    def zvuk(self):
        return "SssssssS"
    
    def ustknuti(self):
        if self.jedovaty:
            return f"POZOR!!! {self.jmeno} tě uštknul a je jedovatý!"
        else:
            return f"{self.jmeno} tě kousnul, ale není jedovatý"
        
    def predstavSe(self):
        if self.ustknuti:
            typ = "jedovatý"
        else:
            typ = "škrtič"

        return f"SssssS ..... já jsem {self.jmeno}, měřím {self.delkavCM} a jsem {typ}"
    
had = Had("Láďa Maňo", 2, 137, True, "Terárium")

print(had.jmeno)
print(had.vek)
print(had.delkavCM)
print(had.zvuk())
print(had.ustknuti())
print(had.predstavSe())


print("-" * 20)


zoo = [pes, kocka, papousek, had]

for obyvatel in zoo:
    print(obyvatel.zvuk())                   #polymorfismus#
    print(obyvatel.predstavSe())
    print("-" * 20)