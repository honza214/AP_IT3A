class Sitovezarizeni:
    def __init__(self, nazev: str, ip_adresa: str, online: bool = False):
        self.nazev = nazev
        self.ip_adresa = ip_adresa
        self.online = online
        pass

    def zmen_stav(self):
        self.online = not self.online
        if self.online:
            return f"Zařízení {self.nazev} je nyní ZAPNUTO"
        else:
            return f"Zařízení {self.nazev} je nyní VYPNUTO"

    def diagnostika(self):
        return f"Spouštím obecnou diagnostiku zařízení..."

class Router(Sitovezarizeni):
    def __init__(self, nazev, ip_adresa, pocet_portu: int, online = False):
        super().__init__(nazev, ip_adresa, online)
        self.pocet_portu = pocet_portu

    def diagnostika(self):
        return super().diagnostika() + " Kontroluji LAN porty"

    def restartuj_wifi(self):
        return "Restartuju Wifi"



router = Router("Router", "192.168.1.1", 4)
#print(router.diagnostika())
#print("-" * 30)


class Server(Sitovezarizeni):
    def __init__(self, nazev, ip_adresa, OS: str , online = False):
        super().__init__(nazev, ip_adresa, online)
        self.OS = OS 


    def diagnostika(self):
        return super().diagnostika() + " Kontroluji vytížení CPU a stav disků."

server = Server("Server", "192.168.1.2", "Ubuntu")
#print(server.diagnostika())


Sit = [router, server]
for zarizeni in Sit:
    print("-" * 30)
    print(zarizeni.zmen_stav())
    print(zarizeni.diagnostika())
