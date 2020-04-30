import socket
import threading
import time

voyelle = ['a','e','i','o','u','y']
consonne = ['b','c','d','f','g','h''j','k','l','m','n','p','q','r','s','t','v','w','x','z']
class Joueur:

    def __init__(self,nom):
        self.nom = nom
        self.solde = 0
        self.buzz = False

    def buzzer(self):   ##UTILISATION DUN SELECT 1 THREAD POUR TOUS PUIS ENSUITE UN THREAD CHACUN
        self.buzz = True

    def canbuyVoyelle(self):
        return (self.solde > 1000)

    def proposervoyelle(self): ##1000 le prix du voyelle
        if(self.canbuyVoyelle()):
            lettre = input("choisir votre lettre >>")
            lettre = lettre.lower()
            if lettre not in voyelle:
                print("Eh oh! pas à nous ;-)")
                self.proposervoyelle()
            else:
                return lettre


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




j1 = Joueur("shrek")



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = socket.gethostname()
s.connect((socket.gethostbyname(name), 1234))   # pour plus tard on proposera de choisir ou ce co , la pour l'instant on reste en local

nam = input("quel est votre nom: ")
s.send(bytes(nam,'utf-8'))
def debut():
    bienvenu = s.recv(1024)
    bienvenu = bienvenu.decode('utf-8')
    print(bienvenu + "\n")
    them = s.recv(1024)
    them = them.decode('utf-8')
    print(them )
    phrase = s.recv(1024)
    phrase = phrase.decode('utf-8')
    print(phrase + "\n")

    phrase2 = s.recv(1024)
    phrase2 = phrase2.decode('utf-8')
    print(phrase2 + "\n")

    phrase2 = s.recv(1024)
    phrase2 = phrase2.decode('utf-8')
    print(phrase2 + "\n")

debut()






def reponseClient(r):
    if (r == 'choix'):  ## si cest l'evenement choix alors....

        res = input("souhaitez vous acheter une voyelle :(oui/non)")
        if (res == 'oui'):
            if (j1.canbuyVoyelle()):
                s.send(bytes(j1.proposervoyelle(), "utf-8"))
            else:
                print("pas assez d'argent")

        print("quelle consonne choisissez vous?")
        s.send(bytes(j1.proposerconsonne(), "utf-8"))
        ##verifier si la lettre est bonne , plus recevoir la phrase avec la lettre
        final = input("souhaitez vous proposez une reponse ? oui/non")
        if (final == 'oui'):
            s.send(bytes(j1.proposerPhrase(), "utf-8"))

