class NPC:
    def __init__(self, jmeno:str, energie:int):
        self.jmeno = jmeno
        self.energie = energie
        pass

    def predstav_se(self):
        return f"Zde NPC {self.jmeno}"
    
    def vyraz_na(self, cil):
        if self.energie >= 10:
            self.energie -= 10
            return f"přesouvám se na {cil} a mám tolik energie: {self.energie}"
        else:
            return f"{self.jmeno} má nedostatek energie pro přesun"
    


class Chodec(NPC):
    def __init__(self, jmeno, energie, domovska_ctvrt:str,):
        super().__init__(jmeno, energie)
        self.domovska_ctvrt = domovska_ctvrt

    def predstav_se(self):
        return f"Zde chodec {self.jmeno}, rajón: {self.domovska_ctvrt}"
    
    def vyraz_na(self, cil:str):
        if self.energie >= 30:
            self.energie -= 30
            return f"přesouvám se na {cil} a mám tolik energie: {self.energie}"
        else:
            return f"{self.jmeno} má nedostatek energie pro přesun"



class Fizl(NPC):
    def __init__(self, jmeno, energie, zbran_tasena:bool = False):
        super().__init__(jmeno, energie)
        self.zbran_tasena = zbran_tasena

    def predstav_se(self):
        return f"Zde policista LSPD {self.jmeno}"

    def tas_nebo_skryj_zbran(self):
        self.zbran_tasena = not self.zbran_tasena
        if self.zbran_tasena == True:
            return f"{self.jmeno} ZBRAŇ TASENÁ"
        else:
            return f"{self.jmeno} ZBRAŇ skryta V POUZDŘE"



class RidicAutobusu(NPC):
    def __init__(self, jmeno, energie):
        super().__init__(jmeno, energie)
        self.cestujici = []

    def naber_cestujici(self, jmeno_cestujiciho:str):
        self.cestujici.append(jmeno_cestujiciho)
        return f"Do autobusu řidiče {self.jmeno} nastoupil cestující: {jmeno_cestujiciho}"


npc = NPC("Hynek Židlík", 30)
print(npc.predstav_se())
print(npc.vyraz_na("Praha"))
print(npc.vyraz_na("Hořovice"))
print("-" * 40)

chodec = Chodec("Big Smoke", 30, "Grove Street")
print(chodec.predstav_se())
print(chodec.vyraz_na("Čtvrt Balas"))
print("-" * 40)

fizl = Fizl("Frank Tenpenny", 100)
print(fizl.predstav_se())
print(fizl.tas_nebo_skryj_zbran())
print(fizl.tas_nebo_skryj_zbran())
print("-" * 40)

ridic = RidicAutobusu("Fandis", 80)
print(ridic.predstav_se())
print(ridic.naber_cestujici("Honza Kouty"))
print(ridic.naber_cestujici("Lenny Karel"))
print(ridic.naber_cestujici("Carl Johnson (CJ)"))
print("-" * 40)

skupina = [npc, chodec, fizl, ridic]
spolecny_cil = "Domů"
for postavy in skupina:
    print(postavy.predstav_se())
    print(postavy.vyraz_na(spolecny_cil))
    print("-" * 40)