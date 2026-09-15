class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        pass
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



zvire2 = Zvire("Crocs", 8, "Sklep")
print(zvire2.jmeno)
print(zvire2.vek)
print(zvire2.misto)
print(zvire2.zvuk())
print(zvire2.predstavSe())
print(zvire2.Kdejsi())
print(zvire2.JdiNa("Škola"))