#LANCER LE SERVEUR AVEC UNE IP ET SON PORT
#serv.py ip port
#sinon le serv sera local

import socket
import sys
import threading
from queue import Queue
from random import randint
from string import ascii_letters
from time import sleep
voyelle = ['a','e','i','o','u','y']
consonne = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
nbthread = 4  #nombre de thread
job = [1,2]
queue = Queue()
all_connections = []
all_address = []


tlock = threading.Lock()

class Jeu():
    def __init__(self):
        self.listeJoueur = []
        self.roue = ['100', '200', '2000', 'Banqueroute']
        self.ValeurRoue = ''
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
        self.ValeurRoue =  self.roue[lacase]
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
                newstr += '_'
            else:
                newstr += c
        self.phraseCachee = newstr
        return newstr

    def premierLettre(self):
        i = randint(0,len(self.phraseCourante)-1)
        if (self.phraseCourante[i]  in voyelle or self.phraseCourante[i]  in consonne):
            return self.phraseCourante[i]
        else :
            self.premierLettre()

    def updateCachee(self, laLettre):
        emplacement = []
        nbr = 1
        mot_list = list(game.phraseCachee)
        for i in range(len(self.phraseCourante)-1):
            if self.phraseCourante[i] == laLettre:
                emplacement.append(nbr)
                mot_list[i] = laLettre
                game.phraseCachee = ''.join(mot_list)
                # game.phraseCachee[nbr-1] = laLettre
            else:
                nbr = nbr + 1

        if len(emplacement) > 0:
            print("\033[92m[*]\033[0m Le client à trouvé "+ str(len(emplacement))+" lettre(s)" )
            print(game.phraseCachee)

            return len(emplacement)
        else:
            return 0
        # return nbr
    def checkPhrase(self,str):
        if self.phraseCourante==str:
            print("Bonne reponse")
            return True
        else:
            print("Mauvaise reponse")
            return False



def creat_job():
    for x in job:
        queue.put(x)
    queue.join()

def create_threadclient():
    for _ in range(nbthread):
        t = threading.Thread(target = work)
        t.daemon = True
        t.start()

def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))

def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(3)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()

def accepting_connections():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1)  # prevents timeout

            all_connections.append(conn)
            all_address.append(address)

            print("Connection has been established :" + address[0])

        except:
            print("Error accepting connections")

def list_connections():
    results = ''

    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(2048)
        except:
            del all_connections[i]
            del all_address[i]
            continue

        results = str(i) + "   " + str(all_address[i][0]) + "   " + str(all_address[i][1]) + "\n"

    print("----Clients----" + "\n" + results)



def startManche(i):

    c = game.premierLettre()
    game.updateCachee(c)
    msg = "Nous vous donnons une lettre " + str(c)
    sleep(3)
    i.send(bytes(msg  ,'utf-8'))
    sleep(1)
    i.send(bytes(game.phraseCachee, 'utf-8'))
    sleep(1)
        



def debutmanche(cptManche):
    cptManche += 1
    sleep(6)

    for i in all_connections:
        #with tlock:

                i.send(bytes("======================== \n \t"+str(cptManche)+ " MANCHE\n======================== \n Voici le theme et la phrase a decouvrir :\n", "utf-8"))
                (theme,phrase) = game.choisirUneExpression()
                game.cacherString(phrase)
                i.send(bytes("Le theme est : \033[95m " + theme + "\033[0m","utf-8"))
                sleep(1)
                i.send(bytes("\nLa phrase est : \033[95m " + game.phraseCachee + "\033[0m\n","utf-8"))
                startManche(i)
                sleep(1)

def envoyerCache(cl):
    cl.send(bytes(game.phraseCachee,"utf-8"))
    sleep(0.3)



def choix(cl) :

    bon = 1
   # with tlock:
    while (bon):
            roulette = game.tournerLaRoue()
            msg = "> La roue tourne... : " + roulette
            cl.send(bytes(msg,"utf-8"))
            sleep(1)
            cl.send(bytes(roulette,"utf-8"))
            sleep(1)
            if (roulette != "banqueroute"):
                cl.send(bytes("\n > Choisissez votre lettre \n","utf-8"))
                sleep(1)
                print("\033[94m[*]\033[0m Attente choix du client....")
                res = cl.recv(1024)
                res = res.decode('utf-8')
                print("\033[94m[*]\033[0m Choix du client : "+res[0])
                nbappartionlettre = game.updateCachee(res[0])
                cl.send(bytes(str(nbappartionlettre),"utf-8"))  ##on envoie le nb d'apparition , le client gagnera de l'argent
                if (nbappartionlettre == 0):
                    bon = 0
                                                            #faut join les threads
                envoyerCache(cl)                               #envoie la phrase maj
                res = cl.recv(1024).decode("utf-8")
                if (res == "oui"):
                    res = cl.recv(1024).decode("utf-8")
                    if(game.checkPhrase(res)):
                        cl.send(bytes("gagné","utf-8"))
                    else:
                        cl.send(bytes("perdu", "utf-8"))
                        bon = 0
            else:
                cl.send(bytes("banqueroute","utf-8"))   #on envoie banqueroute, cest le client qui gerera la perte d'argent
                bon = 0

    cl.send(bytes("joueur suivant"))




def presentation():
    
    for i in all_connections:
        #with tlock:    #zone critique on lock 1 par 1
            res = i.recvfrom(1024)
            print("TEST")
            i.send(bytes("Salut a toi l'ami " + str(res[0]),"utf-8"))
    # print(i)



#####################################################
# --------------- DEBUT DE LA PARTIE ---------------#
#####################################################

game =Jeu()
#tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Parametres de connexion serveur
# try:
#     if sys.argv[1] != '/0' and sys.argv[2] != '/0':
#         ip = sys.argv[1]
#         port = sys.argv[2]
#     else:
#         name = socket.gethostname()
#         ip = socket.gethostbyname(name)
#         port = 1234
# except:
#     print("serveur par defaut local")
#
# # name = socket.gethostname()
# name = 'localhost'
# ip = socket.gethostbyname(name)
# port = 1234
# try:
#     tcpsock.bind((ip, port))
#     tcpsock.listen(3)
# except socket.error:
#     print("La liaison du socket à l'adresse choisie a échoué.")
#     sys.exit()

#
#
# clients = []
#
# print("\033[93m[*] En écoute... \033[0m")
#
# clientsocket, address = tcpsock.accept()
#
# print(f"\033[93m[+] Le joueur {address} vient d'apparaitre \033[0m")
# clients.append((clientsocket,address))
#
#
# list_client = [k for k,_ in clients]
#
# # Attente de la réponse des clients et affiche leurs nom


cptManche = 0


# res = list_client[0].recv(1024).decode("utf-8")


##########################################################
#### BOUCLE PRINCIPALE ################
#########################################################
presentation()
def foo():
    while True:
        res = input("")
        if(res == "list"):
            list_connections()
            continue

def work():
    while True:
        x = queue.get()
        if x == 1:            ## thread qui gere les connections
            create_socket()
            bind_socket()
            accepting_connections()


        if x == 2:
            foo()
            #choix(all_connections[0])
        #if x == 3:
            #foo()
            #choix(all_connections[1])

        #if x == 4:
            #choix(all_connections[2])
            #foo()


        queue.task_done()

create_threadclient()
creat_job()