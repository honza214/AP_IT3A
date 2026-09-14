class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        pass

zvire = Zvire("Tonda", 67)
print(zvire.jmeno)
print(zvire.vek)
print(zvire.misto)