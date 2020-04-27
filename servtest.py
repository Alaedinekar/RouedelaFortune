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


game =Jeu()





tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = socket.gethostname()
port = 1234
ip = socket.gethostbyname(name)

try:
    tcpsock.bind((ip, port))
    tcpsock.listen(3)
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()



clients = []
shutdown = False

def receiving(name,sock):
    while not  shutdown:
        try:
            tlock.acquire()
            while True:
                data,addr = sock.recvfrom(1024)
                print(str(data))
        except:
            pass
        finally:
            tlock.release()


def i_manage_clients(clients):    #Function to manage clients
    for client in clients:
        tcpsock.send('VOUS ETES BIEN CO'.encode('ascii'))

print("En écoute...")
# quitting = False
# while not quitting:
#
#         try:
#             data,addr = tcpsock.recvfrom(1024)
#             if "Quit" in str(data):
#                 quitting = True
#             if addr not in clients:
#                 clients.append(addr)
#         finally:
clientsocket, address = tcpsock.accept()

print(f"le joueur {address} vient d'apparaitre")
clients.append(clientsocket)
id = clientsocket.recv(1024)
id = id.decode("utf-8")
game.ajouterJoueur(id)
for i in game.listeJoueur:
    print("bienvenue a " + i)

for i in clients:
    i.send(bytes("salut a toi l'ami\n","utf-8"))

while(len(clients) < 2):
    #msg = clientsocket.recv(1024)
    #print("cest au tour de " + msg.decode("utf-8"))

    clientsocket.send(bytes("choix","utf-8"))



    msg = clientsocket.recv(1024)
    print(msg.decode("utf-8"))

    msg = clientsocket.recv(1024)
    print(msg.decode("utf-8"))

#data = tcpsock.recv(1024)
#print(data.decode("utf-8"))




##on remplit la liste des clients
#newthread = ClientThread(ip, port, clientsocket)
#i_manage_clients()
# newthread.start()


#except KeyboardInterrupt:
#  tcpsock.close()

#nom = tcpsock.recv(1024)
#print(nom)