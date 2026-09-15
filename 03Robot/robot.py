class Robot:
    def __init__(self, oznaceni: str, baterie: int, ukol: str):
        self.oznaceni = oznaceni
        self.baterie = baterie
        self.ukol = ukol

    def zvuk(self):
        return "BípPup"

    def diagnositka(self):
        return f"{self.baterie}, {self.oznaceni}"

    def aktualniUkol(self):
        return self.ukol

    def zadejUkol(self, nUkol: str):
        self.ukol = nUkol
        return f"Tvuj nový úkol je {self.ukol} "


robot = Robot("BíPuBíp", 80, "umýt nádobí")
print(robot.oznaceni)
print(robot.baterie)
print(robot.ukol)
print(robot.zvuk())
print(robot.diagnositka())
print(robot.aktualniUkol())
print(robot.zadejUkol("uklidit nádobí"))