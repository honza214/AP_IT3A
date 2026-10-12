class Naradi:
    def __init__(self, znacka:str, model:str):
        self.znacka = znacka
        self.model = model
        pass

    def identifikace(self):
        return f"Jsem {self.znacka} a mám tento model: {self.model}"

    def pracuj(self):
         return "Nářadí pracuje"

class AkuVrtacka(Naradi):
    def __init__(self, znacka, model, baterie:int):
        super().__init__(znacka, model)
        self.baterie = baterie
        self.baterie = max(0, min(100, baterie))

    def pracuj(self):
        if self.baterie > 0:
            self.baterie -= 10
            return "Vrtačka vrtá"
        elif self.baterie == 0:
            return "Nutno nabít!"

class MotorovaPila(Naradi):
    def __init__(self, znacka, model, nadrz_plna:bool):
        super().__init__(znacka, model)
        self.nadrz_plna = nadrz_plna

    def pracuj(self):
        if self.nadrz_plna == True:
            return f"{self.znacka} Pracuje"
        else:
            return f"{self.znacka} Nepracuje"

akuvrtacka = AkuVrtacka("Bosch", "GSR 12V", 150)
motorovapila = MotorovaPila("Stihl", "MS 170", 20)


while akuvrtacka.baterie > 0:
    print(akuvrtacka.pracuj())
    print(f"Baterie: {akuvrtacka.baterie} %")
    print("-" * 40)