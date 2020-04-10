import socket
import random
import string
import pickle

HEADERSIZE = 10



class Player():
    numPlayer = 0

    def __init__(self):
        self.argent = 0
        self.stock = ""
        self.listlettre = list(string.ascii_lowercase)
        Player.numPlayer += 1
        self.nom = "Joueur " + str(Player.numPlayer)

    def cotoi(self):
        str = "je suis et je suis connecté"
        return str + self.nom

    def ajouterargent(self, argent):
        self.argent += argent

    def ajouterstock(self, kdo):
        self.stock = self.stock + " " + kdo

    def choisirlettre(self):
        r = random.randint(0, 28)
        x = self.listlettre[r]
        self.listlettre.remove(r)
        return x

    def resetlist(self):
        self.listlettre = list(string.ascii_lowercase)

    def choisirmot(self, x):
        return x


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1243))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_msg += msg.decode("utf-8")

        print(len(full_msg))


        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ""