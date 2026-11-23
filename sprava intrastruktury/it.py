import random
from datetime import datetime

class Server:
    def __init__(self,hostname:str, os:str, deployYear:int, warrantyYear:int = 0, storageFree:int = 100):
        self.hostname = hostname
        self.os = os
        self.deployYear = deployYear
        self.warrantyYear = warrantyYear
        self.storageFree = storageFree
        pass

    def __str__(self):
        return f"{self.hostname}, {self.os}, {self.deployYear}, - volné místo {self.storageFree}"
    
    def saveData(self):
        usage = random.randint(5,20)
        if self.storageFree >= usage:
            self.storageFree -= usage
            return f"Na server {self.hostname} se uložila data {usage} %, ale k dispozici je jen {self.storageFree} %"
        else:
            f"Chyba: Na serveru {self.hostname} není místo! Potřeba {usage}%, ale k dispozici je jen {self.storageFree}%."

    def cleanDisk(self):
        clean = 100 - self.storageFree
        self.storageFree = 100
        return f"Disky na serveru {self.hostname} byly pročištěny. Uvolnilo se {clean}% místa."
    
    def warrantyCheck(self):
        if self.warrantyYear < datetime.now().year:
            return f"Platnost záruky skončila v roce {self.warrantyYear}"
        else:
            return f"Záruka platí {self.warrantyYear - datetime.now().year}"
        

class ServerRoom:
    def __init__(self,name:str):
        self.name = name
        self.servers = []
        pass

    def addServer(self, server):
        self.servers.append(server)
        print(f"{server.hostname} byl přidán do seznamu.")

    def showServers(self):
        if len(self.servers) == 0:
            return f"Varování: V datacentru nejsou žádné servery!"
        else:
            for server in self.servers:
                return f"--> {server}"
            
    def oldestServer(self):
        return min(self.servers, key= lambda server:server.deployYear)
    
    
    def avgStorage(self):
        return sum(server.storageFree for server in self.servers) / len(self.servers)
    
    def fullServers(self, limit = 30): 
        result = []
        for server in self.servers:
            if server.storageFree < limit:
                result.append(server)
        return result
    
    def serversForReplacement(self):
        result = []
        for server in self.servers:
            if server.warrantyYear > datetime.now().year:
                result.append(server)
        return result


server = Server("Web-Main", "Ubuntu Linux", 2018, 2028)
print(server.saveData())
print(server.cleanDisk())
print(server.warrantyCheck())
print("-" * 50)

room = ServerRoom("datacentrum praha")
room.addServer(server)
print(room.showServers())
print("-" * 50)
oldest = room.oldestServer()
print(f"Nejstarší server: {oldest}")
print("-" * 50)
avg = room.avgStorage()
print(f"Průměrné volné místo: {avg}%")
print("-" * 50)
print("Plné servery:")
for s in room.fullServers():
    print(f"-->{s}")
    print("-" * 50)
    print("servery k výměně:")
for s in room.serversForReplacement():
    print(f"-->{s}")