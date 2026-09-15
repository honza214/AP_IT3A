class Hero:
    def __init__(self, jmeno: str, level: int, lokace: str = "Valorant"):
        self.jmeno = jmeno
        self.level = level
        self.lokace = lokace

    def pokrik(self):
        return "Pojd B"

    def predstavSe(self):
        return f"Jmenuji se {self.jmeno}, a mám {self.level} level."


hero = Hero("Láďa", 27)
print(hero.jmeno)
print(hero.level)
print(hero.lokace)
print(hero.predstavSe())