class VesmirnaLod:
    def __init__(self, nazev:str, palivo:int):
        self.nazev = nazev
        self.palivo = palivo
        pass
        
    def predstav_se(self):
        return f"Zde loď {self.nazev}"
    
    def let_na(self, cil:str):
        if self.palivo > 100:
            self.palivo = 100
        elif self.palivo < 0:
            self.palivo = 0

        self.cil = cil
        if self.palivo >= 10:
            self.palivo -= 10
            return f"Zahajuji podsvětelný let na {self.cil}. a zbýva paliva: {self.palivo} %."
        else:
            return "Nedostatek paliva pro let!"

        
class PozemskyKriznik(VesmirnaLod):
    def __init__(self, nazev, palivo, velitel:str):
        super().__init__(nazev, palivo)
        self.velitel = velitel

    def predstav_se(self):
        return f"Zde pozemský křižník {self.nazev}, velí {self.velitel}."
    
    def let_na(self, cil):
        self.cil = cil
        if self.palivo >= 30:
            self.palivo -= 30
            return f"Otevírám hyperprostorové okno k cíli: {self.cil} a zbývá: {self.palivo} %"
        else:
            return "Nedostatek paliva"
        
pozemskykriznik = PozemskyKriznik("Daedalus",20, "Filip Frank")
print(pozemskykriznik.predstav_se())
print(pozemskykriznik.let_na("praha"))
print("-" * 40)
        
class PuddleJumper(VesmirnaLod):
    def __init__(self, nazev, palivo, maskovani_aktivni:bool):
        super().__init__(nazev, palivo)
        self.maskovani_aktivni = maskovani_aktivni

    def predstav_se(self):
        return f"Zde antický Jumper {self.nazev}"
    
    def let_na(self, cil):
        return super().let_na(cil)
    
    def zamaskuj_se(self):
        self.zamaskuj_se = not self.zamaskuj_se
        if self.maskovani_aktivni == True:
            return f"Jumper 1: Maskování AKTIVOVÁNO."
        else:
            return f"Jumper 1: Maskování NEAKTIVOVÁNO."
        
puddlejumper = PuddleJumper("Loď z Atlantis",30, True)
print(puddlejumper.predstav_se())
print(puddlejumper.let_na("plzen"))
print(puddlejumper.zamaskuj_se())
print("-" * 40)

class Teltak(VesmirnaLod):
    def __init__(self, nazev, palivo, naklad = []):
        super().__init__(nazev, palivo)
        self.naklad = naklad

    def naloz_naklad(self, polozka:str):
        self.naklad = [polozka]
        return f"{self.nazev} bylo naloženo: {polozka}"
    
teltak = Teltak("Goauldská nákladní loď",30)
print(teltak.naloz_naklad("KFC"))
print("-" * 40)

        


flotila = [pozemskykriznik, puddlejumper, teltak]
spolecny_let = "Planeta Lantea"
for lode in flotila:
    print(lode.predstav_se())
    print(lode.let_na(spolecny_let))
