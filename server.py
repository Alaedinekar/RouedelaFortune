import socket
import time
import random

import self as self


class Jeu():

    def __init__(self):
        self.joueur = []
        self.roulette = list("BANQUEROUTE",100,200, 300,500,"CADEAU")
        self.kdo = "une chaussette"

    def passer(self):
        mesg = "pass"
        return mesg

    def Actionroulette(self,joueur):
        r = random.randint(0,len(self.roulette))
        tirage = self.roulette[r]
       if(type(tirage) == int):
           joueur.argent += tirage
        if (tirage == "BANQUEROUTE"):
             self.passer()
        if(tirage == "CADEAU"):
            joueur.stock += self.kdo







HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    msg = "Welcome to the server!"
    msg = f"{len(msg):<{HEADERSIZE}}"+msg

    clientsocket.send(bytes(msg,"utf-8"))

    while True:
        time.sleep(3)
        msg = f"The time is {time.time()}"
        msg = f"{len(msg):<{HEADERSIZE}}"+msg

        print(msg)

        clientsocket.send(bytes(msg,"utf-8"))






