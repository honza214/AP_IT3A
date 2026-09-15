class Hero:
    def __init__(self, jmeno: str, level: int, lokace: str = "site B"):
        self.jmeno = jmeno
        self.level = level
        self.lokace = lokace

    def pokrik(self):
        return "Pojd B"

    def predstavSe(self):
        return f"Jmenuji se {self.jmeno}, a mám {self.level} level."

    def KdeJsi(self):
        return f"jsem v Lokaci zvaném {self.lokace}."

    def PresunSe(self, nLokace: str = "site A"):
        staraLokace = self.lokace
        self.lokace = nLokace
        return f"přesouvám se z lokace {staraLokace} na {self.lokace}"


hero = Hero("Láďa", 27)
print(hero.jmeno)
print(hero.level)
print(hero.lokace)
print(hero.pokrik())
print(hero.predstavSe())
print(hero.KdeJsi())
print(hero.PresunSe())