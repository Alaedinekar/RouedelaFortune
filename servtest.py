#LANCER LE SERVEUR AVEC UNE IP ET SON PORT
#serv.py ip port
#sinon le serv sera local

import socket
import sys
import threading
from random import randint
from string import ascii_letters
from time import sleep

tlock = threading.Lock()

class Jeu():
    def __init__(self):
        self.listeJoueur = []
        self.roue = ['100', '200', '2000', 'Banqueroute']
        self.phraseCourante = ''
        self.phraseCachee = ''
        self.theme = ["Animaux","Profit","Gourmet","Bof Bof","difficulté"]
        self.expression = ["Donner sa langue au chat","Pierre qui roule n'amasse pas mousse","Avoir les yeux plus gros que le ventre","Les doigts dans le nez","Ca ne casse pas trois pattes a un canard"]

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
        a = randint(0,len(self.theme)-1)
        laPhrase  = self.expression[a]
        self.phraseCourante = laPhrase
        theme = self.theme[a]
        self.expression.remove(laPhrase)
        self.theme.remove(theme)
        return (theme,laPhrase)

    # def rapidite(self,str):
    #     pass
    #     """Le premier qui trouve gagne !\nC'est simple !"""
    #     print("Christophe : Je vous propose une épreuve de rapidité, quel est le thème Victoria ?")
    #     source = str.split(',')
    #     theme,expression = source[1][:-1],source[0][:-1]
    #     sleep(1)
    #     print("Victoria : {} !".format(theme))
    #     expressionCachee = self.cacherString(expression)
    #     sleep(1)
    #     print(expressionCachee)
    #     print("Christophe : Top !")


    def cacherString(self,str):
        newstr = ''
        for c in str:
            if c in ascii_letters:
                newstr += '-'
            else:
                newstr += c
        self.phraseCachee = newstr
        return newstr
    def premierLettre(self):
        i = randint(0,len(self.phraseCourante)-1)
        if (self.phraseCourante[i]  in ascii_letters):
            return self.phraseCourante[i]
        else :
            self.premierLettre()

    def updateCachee(self, laLettre):
        nbr = 0
        for i in range(len(self.phraseCourante)-1):
            if self.phraseCourante[i] == laLettre:
                nbr += 1
                self.phraseCachee[i] = laLettre
            else:
                return 'Non pas de {} dans le mot !'.format(laLettre)
        return nbr


def startManche():
    msg = "Nous vous donnons une lettre\t"
    c = game.premierLettre()
    game.updateCachee(c)
    for i in list_client:

        i.send(bytes(msg ,'utf-8'))
        i.send(bytes(c, 'utf-8'))
        i.send(bytes(game.phraseCachee, 'utf-8'))



def debutmanche(cptManche):
    cptManche += 1
    sleep(6)
    for i in list_client:
        i.send(bytes(str(cptManche)+ " manche \nVoici le theme et la phrase a decouvrir :\n", "utf-8"))
        (theme,phrase) = game.choisirUneExpression()
        game.cacherString(phrase)
        i.send(bytes("Le theme est : " + theme,"utf-8"))
        i.send(bytes("\nLa phrase est : " + game.phraseCachee + "\n","utf-8"))
        startManche()



def choix(cl) :
    roulette = game.tournerLaRoue()
    cl.send(bytes(roulette,"utf-8"))
    if (roulette != "banqueroute"):
        cl.send(bytes("choisissez votre lettre"))
        cl.send(bytes("choix","utf-8"))
        sleep(3)
        cl.recvfrom(1024,)



#####################################################
# --------------- DEBUT DE LA PARTIE ---------------#
#####################################################

game =Jeu()
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Parametres de connexion serveur
try:
    if sys.argv[1] != '/0' and sys.argv[2] != '/0':
        ip = sys.argv[1]
        port = sys.argv[2]
    else:
        name = socket.gethostname()
        ip = socket.gethostbyname(name)
        port = 1234
except:
    print("serveur par defaut local")

name = socket.gethostname()
ip = socket.gethostbyname(name)
port = 1234
try:
    tcpsock.bind((ip, port))
    tcpsock.listen(3)
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()



clients = []

print("[*] En écoute...")

clientsocket, address = tcpsock.accept()

print(f"[+] Le joueur {address} vient d'apparaitre")
clients.append((clientsocket,address))


list_client = [k for k,_ in clients]

for i in list_client:
    i.send(bytes("Salut a toi l'ami\n","utf-8"))
    # print(i)

cptManche = 0
debutmanche(cptManche)


while True:
    debutmanche(cptManche)









