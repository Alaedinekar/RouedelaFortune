import socket


voyelle = ['a','e','i','o','u','y']
consonne = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
class Joueur:

    def __init__(self,nom):
        self.nom = nom
        self.solde = 0
        self.buzz = False

    def buzzer(self):   ##UTILISATION DUN SELECT.select 1 THREAD POUR TOUS PUIS ENSUITE UN THREAD CHACUN
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

    #phrase4 = s.recv(1024)
    #roueTourne = phrase4.decode('utf-8')
    #print("\033[95m" + str(roueTourne) +"\033[0m" ) 

    gain = s.recv(1024)
    gain = gain.decode('utf-8')
    print("\033[93m Vous obtenez " + gain + " ! \033[0m") #Gain de la roue
    if(gain!="banqueroute"):
        reponseClient('choix',gain)


def reponseClient(r,gain):
    temp=j1.solde+int(gain)
    print("Vous avez : "+str(temp))
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

        nblett = s.recv(1024).decode("utf-8")
        print("\nvous avez trouvé "+ str(nblett) + " lettres\n")

        # j1.solde = j1.solde + (int(gain) * int(nblett))
        # print("vous avez desormais " + str(j1.solde) +"€\n")

        res3 = s.recv(1024).decode("utf-8") #Affichage de phraseCachee
        print(res3[0])
        
        ##verifier si la lettre est bonne , plus recevoir la phrase avec la lettre
        if(int(nblett) > 0):    
            final = input("> Souhaitez vous proposez une reponse ? oui/non \n")
            if (final == 'oui'):
                s.send(bytes("oui","utf-8"))
                s.send(bytes(j1.proposerPhrase(), "utf-8"))
                print(s.recvfrom(1024)[0])
            else:
                s.send(bytes("non","utf-8"))



#####################################################
# --------------- DEBUT DE LA PARTIE ---------------#
#####################################################


j1 = Joueur("shrek")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# name = socket.gethostname()
name = 'localhost'
s.connect((socket.gethostbyname(name), 9999))   # pour plus tard on proposera de choisir ou ce co , la pour l'instant on reste en local

nam = input("Quel est votre nom : ")
s.send(bytes(nam,'utf-8'))


#for i in range(3):
debut()

running=True

while running:

    msg=s.recv(1024).decode('utf-8')
    print(">"+msg)
    if(str(msg)=="choix"):
        value=s.recv(1024).decode('utf-8')
        if(str(value)!="banqueroute"):
            reponseClient("choix",value)
        else:
            print("Banqueroute !")
    elif(str(msg)=="fin"):
        running=False