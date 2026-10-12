class ChytreZarizeni:
    def __init__(self, nazev:str, mistnost:str, zapnuto:bool = False):
        self.nazev = nazev
        self.mistnost = mistnost
        self.zapnuto = zapnuto
        pass

    def prepni_stav(self):
        self.zapnuto = not self.zapnuto  #přepne z false na true
        if self.zapnuto: #self.zapnuto je nyní True
            return f"Zařízení {self.nazev} v místnosti {self.mistnost} je nyní ZAPNUTO."
        else:
            return f"Zařízení {self.nazev} v místnosti {self.mistnost} je nyní VYPNUTO."

    def proved_akci(self):
        return "Zařízení čeká na příkaz."

class ChytraZarovka(ChytreZarizeni):
    def __init__(self, nazev, mistnost, zapnuto = False, barva:str = "bílá"):
        super().__init__(nazev, mistnost, zapnuto)
        self.barva = barva

    def proved_akci(self):
        if self.zapnuto == True:
            return f"{self.nazev} svítí touto barvou: {self.barva}"
        else:
            return "Je zhasnuto"

    def zmen_barvu(self, nova_barva):
        self.barva = nova_barva
        return f"{self.nazev} teď svítí barvou: {self.barva}"

class ChytraZasuvka(ChytreZarizeni):
    def __init__(self, nazev, mistnost, aktualni_odber_w: int, zapnuto=False):
        super().__init__(nazev, mistnost, zapnuto)
        self.aktualni_odber_w = aktualni_odber_w

    def proved_akci(self):
        if self.zapnuto == True:
            return f"{self.nazev} propouští proud a aktuální odběr ve wattech je {self.aktualni_odber_w}"
        else:
            return f"{self.nazev} je vypnutá, proud nepropouští."


zasuvka = ChytraZasuvka("Zásuvka u TV", "Obývák", 150, True)
zarovka = ChytraZarovka("Lustr", "Obývák", "bílá")


domacnost = [zasuvka, zarovka]
for zarizeni in domacnost:
    print(zarizeni.prepni_stav())
    print(zarizeni.proved_akci())
    print("-" * 40)