class Robot:
    def __init__(self, oznaceni:str, baterie:int):
        self.oznaceni = oznaceni
        self.baterie = baterie
        pass

    def hlaseni_stavu(self):
        return f"Moje baterie je {self.baterie} %"
    
robot = Robot("Bobot", 80)
print(robot.hlaseni_stavu())