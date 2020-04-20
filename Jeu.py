from random import randint
from time import sleep
from string import ascii_letters
import os
from Joueur import *

class Jeu():
    def __init__(self):
        self.listeJoueur = []
        self.roue = ['100', '200', '2000', 'Banqueroute']

    def afficherListe(self):
        for j in self.listeJoueur:
            print(j.nom)
    def ajouterJoueur(self,nom):
        self.listeJoueur.append(nom)
    def tournerLaRoue(self):
        """Tourne la roue à votre place, vous faites pas mal !"""
        lacase = randint(0,len(self.roue)-1)
        return self.roue[lacase]

    def choisirUneExpression(self):
        """Choisis une expression dans la liste"""
        f = open('enigmes/expressions.txt',mode='r',encoding='utf-8')
        laPhrase  = f.readlines()
        return laPhrase[randint(0,len(laPhrase)-1)]

    def rapidite(self,str):
        pass
        """Le premier qui trouve gagne !\nC'est simple !"""
        print("Christophe : Je vous propose une épreuve de rapidité, quel est le thème Victoria ?")
        source = str.split(',')
        theme,expression = source[1][:-1],source[0][:-1]
        sleep(1)
        print("Victoria : {} !".format(theme))
        expressionCachee = self.cacherString(expression)
        sleep(1)
        print(expressionCachee)
        print("Christophe : Top !")


    def cacherString(self,str):
        newstr = ''
        for c in str:
            if c in ascii_letters:
                newstr += '_'
            else:
                newstr += c
        return newstr



########### TESTS ##########

Partie = Jeu()
shaun = Joueur('Shaun')
Partie.ajouterJoueur(shaun)
Partie.afficherListe()
print(Partie.tournerLaRoue())
print(Partie.rapidite(Partie.choisirUneExpression()))

#print(Partie.cacherString("Coucou comment va ?"))