class Robot:
    def __init__(self, oznaceni:str, baterie:int):
        self.oznaceni = oznaceni
        self.baterie = baterie
        pass

    def hlaseni_stavu(self):
        return f"Moje baterie je {self.baterie} %"
    
    def proved_misi(self):
        return "Čekám na zadání souřadnic"
    
    def nabij_baterii(self):
        if self.baterie > 100:
            self.baterie = 100
        self.baterie = 100
        return "Baterie je nyní na 100 %"
    
    def stav_baterie(self):
        return f"Moj baterie je nyní: {self.baterie} %"


    
#robot = Robot("Bobot", 80)
#print(robot.hlaseni_stavu())
#print(robot.nabij_baterii())

class Kvadrokoptera(Robot):
    def __init__(self, oznaceni, baterie, max_vyska:int):
        super().__init__(oznaceni, baterie)
        self.max_vyska = max_vyska

    def proved_misi(self):
        if self.baterie > 25:
            self.baterie -= 25
            return f"{self.oznaceni} odletěl do své max výšky: {self.max_vyska} a pořídil snímky a nyní má baterii: {self.baterie} %"
        else:
            return f"{self.oznaceni} Odmítnul vzlétnout"
        

        
class PruzkumyPasak(Robot):
    def __init__(self, oznaceni, baterie, ma_termokameru:bool):
        super().__init__(oznaceni, baterie)
        self.ma_termokameru = ma_termokameru

    def proved_misi(self):
        if self.ma_termokameru == True:
            self.baterie -= 10
            return "Skenuju teplo."
        else:
            return "Nemá termokameru."


kvadrokoptera = Kvadrokoptera("Bobot", 80, 175)
pruzkumypasak = PruzkumyPasak("Hugo", 40, True)

seznam = [kvadrokoptera, pruzkumypasak]
for zarizeni in seznam:
    print(zarizeni.proved_misi())
    print(zarizeni.stav_baterie())
    print(zarizeni.nabij_baterii())
    print("-" * 40)