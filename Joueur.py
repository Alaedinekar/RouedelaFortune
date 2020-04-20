from string import *

class Joueur:

    def __init__(self,nom):
        self.nom = nom
        self.solde = 0
        self.buzz = False

    def buzzer(self):
        self.buzz = True

    def proposerLettre(self,lettre):
        if lettre not in ascii_letters:
            return "Eh oh! pas à nous ;-)"
        lettre = lettre.lower()
        return lettre
    def proposerPhrase(self,phrase):
        return phrase

#
# shaun = Joueur('Shaun')
# print(shaun.proposerLettre('R'))
# print(shaun.proposerLettre('%'))
# print(shaun.proposerPhrase('euh alors es-ce que ça marche ?'))

