# coding: utf-8

import socket
from string import *
voyelle = ['a','e','i','o','u','y']
consonne = ['b','c','d','f','g','h''j','k','l','m','n','p','q','r','s','t','v','w','x','z']
class Joueur:

    def __init__(self,nom):
        self.nom = nom
        self.solde = 0
        self.buzz = False

    def buzzer(self):   ##UTILISATION DUN SELECT 1 THREAD POUR TOUS PUIS ENSUITE UN THREAD CHACUN
        self.buzz = True

    def proposervoyelle(self): ##1000 le prix du voyelle
        if(self.solde>1000):
            lettre = input("choisir votre lettre >>")
            lettre = lettre.lower()
            if lettre not in voyelle:
                print("Eh oh! pas à nous ;-)")
                self.proposervoyelle()

            return lettre
        return "desolé pas assez d'argent pour acheter une voyelle"

    def proposerconsonne(self):
        lettre = input("choisir votre consonne >>")
        lettre = lettre.lower()
        if lettre not in consonne:
           print("Eh oh! pas à nous ;-)")
           self.proposerconsonne()

        return lettre

    def proposerPhrase(self):
        phrase = input("Que proposez vous  comme reponse? :")
        return phrase






s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 1111))   ## pour plus tard on proposera de choisir ou ce co , la pour l'instant on reste en local
name = input("quel est votre nom:")
j1 = Joueur(name)


r = s.recv(99999) ## on recoit du serveur l'evenement


if(r == 'choix'):  ## si cest l'evenement choix alors....

    res = input("souhaitez vous acheter une voyelle :(oui/non")
    if (res== 'oui'):
        s.send(j1.proposervoyelle().encode('ascii'))
    print("quelle consonne choisissez vous?")
    s.send((j1.proposerLettre()).encode('ascii'))
    final = input("souhaitez vous proposez une reponse ? oui/non")
    if(final == 'yes'):
        s.send((j1.proposerPhrase()).encode('ascii'))


if(r == 'buzz'):
    j1.buzz()
    attente = s.recv(1024)
    if (attente == "ok"):
        j1.proposerPhrase()


if(r == "defaite"):
    print("vous avez perdu dommage")
    s.close()


if (r == "recap"):
    recap = s.recv(2048)
    print(recap)

