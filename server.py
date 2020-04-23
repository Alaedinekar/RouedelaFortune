# coding: utf-8

import socket
import threading

from random import randint
from time import sleep
from string import ascii_letters
import os
from client1 import *

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
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1111))
clients = []

def i_manage_clients():    #Function to manage clients
    for client in clients:
        client.send('Message to pass')

while True:
    try:
        tcpsock.listen(3)
        print("En écoute...")
        (clientsocket, (ip, port)) = tcpsock.accept()
        clients.append(clientsocket) ##on remplit la liste des clients
        newthread = ClientThread(ip, port, clientsocket)
        newthread.start()
    except KeyboardInterrupt:
        socket.close()




    ###etape1 buzz avec un select
    ## un thread par joueur


