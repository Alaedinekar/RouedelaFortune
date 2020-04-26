# coding: utf-8

import socket
import threading
lock = threading.Lock()

from random import randint
from time import sleep
from string import ascii_letters
import os
from client1 import *

class Jeu():
    def __init__(self):
        self.listeJoueur = []
        self.roue = ['100', '200', '2000', 'Banqueroute']
        self.phraseCourante = ''
        self.phraseCachee = ''

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
        self.phraseCourante = laPhrase[randint(0,len(laPhrase)-1)]
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
        self.phraseCachee = newstr
        return newstr

    def updateCachee(self,laLettre):
        nbr = 0
        for i in range(len(self.phraseCourante))
            if self.phraseCourante[i] == laLettre:
                nbr++
                self.phraseCachee[i] = laLettre
        return nbr




game =Jeu()

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port,))

    def run(self):
        print("Connexion de %s %s" % (self.ip, self.port,))

        r = self.clientsocket.recv(2048)

       ## self.clientsocket.send()




tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    tcpsock.bind((socket.gethostname(), 1234))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()


clients = []

def i_manage_clients():    #Function to manage clients
    for client in clients:
        client.send('VOUS ETES BIEN CO'.encode('ascii'))

while True:
    try:
        tcpsock.listen(3)
        print("En écoute...")
        (clientsocket, (ip, port)) = tcpsock.accept()
        clients.append(clientsocket) ##on remplit la liste des clients
        newthread = ClientThread(ip, port, clientsocket)
        i_manage_clients()
        newthread.start()
    except KeyboardInterrupt:
        tcpsock.close()




    ###etape1 buzz avec un select
    ## un thread par joueur




