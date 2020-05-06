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
            lettre = input("Choisir votre lettre >>")
            lettre = lettre.lower()
            if lettre not in voyelle:
                print("Eh oh! pas à nous ;-)")
                self.proposervoyelle()
            else:
                return lettre


    def proposerconsonne(self):
        lettre = input("Choisir votre consonne >>  ")
        lettre = lettre.lower()
        if lettre not in consonne:
           print("Eh oh! pas à nous ;-)")
           self.proposerconsonne()

        return lettre

    def proposerPhrase(self):
        phrase = input("Que proposez vous  comme reponse? :")
        return phrase





def debut():
    bienvenu = s.recv(1024)
    bienvenu = bienvenu.decode('utf-8')
    print(bienvenu + "\n ") #Salut a toi l'ami (Référence à MisterRobot)

    them = s.recv(1024)
    them = them.decode('utf-8')
    print(them) #X MANCHE + THEME + PHRAS


    phrase = s.recv(1024)
    phrase = phrase.decode('utf-8')
    print(phrase + "\n") #Theme 



    phrase2 = s.recv(1024)
    phrase2 = phrase2.decode('utf-8')
    print(phrase2 + "\n") #Phrase caché sans indice

    

    phrase2 = s.recv(1024)
    phrase2 = phrase2.decode('utf-8')
    print(phrase2 +": ") #Nous vous donner une lettre

    phrase4 = s.recv(1024)
    roueTourne = phrase4.decode('utf-8')
    print("La phrase est : \033[95m" +roueTourne +"\033[0m" ) #Affichage pharseCache 

    gain = s.recv(1024)
    gain = gain.decode('utf-8')
    print("\033[93m" +gain + "€ ! \033[0m") #Gain de la roue



def reponseClient(r):
    if (r == 'choix'):  ## si cest l'evenement choix alors....
        res = input("> Souhaitez vous acheter une voyelle :(oui/non) \n")
        if (res == 'oui'):
            if (j1.canbuyVoyelle()):
                s.send(bytes(j1.proposervoyelle(), "utf-8"))
            else:
                print("pas assez d'argent")

        print("> Quelle consonne choisissez vous?")
        lettre = j1.proposerconsonne()
        print("Vous avez choisi la lettre : "+lettre)

        s.send(bytes(lettre, "utf-8"))

        res1 = s.recvfrom(1024) #Mauvaise mot jsp d'ou il vient le con
        # print(res1[0])


        res2 = s.recvfrom(1024) #Vous avez trouvé un mot ou pas du tout
        print(res2[0])

        res3 = s.recvfrom(1024) #Affichage de phraseCachee
        print(res3[0])
        
        ##verifier si la lettre est bonne , plus recevoir la phrase avec la lettre
        final = input("> Souhaitez vous proposez une reponse ? oui/non \n")
        if (final == 'oui'):
            s.send(bytes("oui","utf-8"))
            s.send(bytes(j1.proposerPhrase(), "utf-8"))
            print(s.recvfrom(1024)[0]);



#####################################################
# --------------- DEBUT DE LA PARTIE ---------------#
#####################################################


j1 = Joueur("shrek")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# name = socket.gethostname()
name = 'localhost'
s.connect((socket.gethostbyname(name), 1234))   # pour plus tard on proposera de choisir ou ce co , la pour l'instant on reste en local

nam = input("Quel est votre nom : ")
s.send(bytes(nam,'utf-8'))
debut()

reponseClient('choix')
print(s.recv(1024))
