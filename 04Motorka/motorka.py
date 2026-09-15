class Motorka:
    def __init__(self, znacka: str, kategorie: str, stav_nadrze: int, stav_stojanku: str = "vyklopený"):
        self.znacka = znacka
        self.kategorie = kategorie
        self.stav_nadrze = stav_nadrze
        self.stav_stojanku = stav_stojanku

    def zvuk_plynu(self):
        return "vrum"

    def popis_motorky(self):
        return f"toto je {self.znacka} a její kategorie je {self.kategorie}"

    def aktualni_stojanek(self):
        return f"Aktualní stav stojánku je {self.stav_stojanku}"

    def zmena_stojanek(self, nStojanek: str):
        self.stav_stojanku = nStojanek
        return f"stojánek je teď {self.stav_stojanku}"

    def popojed(self, spotreba: int):
        self.stav_nadrze -= spotreba
        return f"Popojel jsem a spotřebovalo se {spotreba}%, nádrž je na {self.stav_nadrze}%"

    def natankuj(self, mnozstvi: int):
        self.stav_nadrze += mnozstvi
        if self.stav_nadrze > 100:
            self.stav_nadrze = 100
        return f"Natankoval jsem {mnozstvi}%, nádrž je teď na {self.stav_nadrze}%"


motorka = Motorka("Honda", "cestovní", 85)
print(motorka.znacka)
print(motorka.kategorie)
print(motorka.stav_nadrze)
print(motorka.stav_stojanku)
print(motorka.zvuk_plynu())
print(motorka.popis_motorky())
print(motorka.aktualni_stojanek())
print(motorka.zmena_stojanek("sklopený"))
print(motorka.popojed(7))
print(motorka.natankuj(20))