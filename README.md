# RouedelaFortune

Mini Projet  : Communication Inter Process
Cahier des charges : Il s'agit de la "Roue de la Fortune".
Fabriquer la version client/serveur du jeu décrit par la vidéo : https://www.youtube.com/watch?v=ZJo-Oq36ikA
Groupes : Arthur Fontaine - Aleadine Karouia - Shaun Phipps - Fabre Quentin

Introduction : Le projet est developpé en Python et a pour objectif de reproduire le célèbre jeu La roue de la fortune. L'interface de jeu sera implémentée depuis l'invité de commande et se composera de 4 Joueurs en ligne.

Lancement  : 
Afin de pouvoir lancer le serveur il faudra exécuter la ligne suivante : python3 serv.py
La connexion au serveur du client se fera après avoir exécuté la commande python3 client.py

Technique : 
Le jeu est développer entièrement en Python avec aucune librairie tiers. Pour cela nous n'utilisons pas SocketIO mais des socket avec le protocol TCP.
Le client représente le joueur. Un thread est lancé pour chaque joueur ainsi qu'un pour la gestion du jeu et pour la connexion du client.

Reste à faire : 
- Régler le problème de répartition des taches sur les différents Threads
- Déconnexion joueur
- Nouvelle interface
- Ajout sur le serveur polymnie  


######################## Consignes ########################
Spécifier votre application :
Tout est à faire par vous !
qui sont les clients ?
qui sont les serveurs ?
comment on rejoint le jeu  ? 
comment on le quitte ?
comment on affiche les lettres, les résultats ? ...
Vous pouvez aussi l'adapter . Par exemple, les joueurs sont théoriquement tous "présents",
mais pour un jeu réseau ce n'est pas le cas, comment ca se passe si un joueur disparait ?
déconnecté ? ou parti ?

 Les groupes : 4 personnes maximum
Cela devrait suffire à abattre pas mal de travail.



  Rendus : un jeu déployé plus qu'un programme.
Vous fournirez les sources, une documentation TECHNIQUE (diagramme UML, protocoles mis en place, paquets, ..) mais aussi un serveur déployé permettant à tous de jouer. Le minimum c'est polymnie ou une machine de l'UCA. Si vous avez un cluster dans un cloud ... ca peut le faire aussi !

Vos choix techniques :
Le choix "classique" c'est de le faire en C et c'est très bien comme cela. Mais,

Est ce que je peux utiliser autre choses que C pour coder ? ... YES
Est ce qu'il peut y avoir des morceaux en C, d'autres en Python .. etc ?  YES
Si vous pensez à une techno (Js par exemple) qui vous éloigne des sockets que l'on a vu ensemble, il faut que vous fassiez valider votre choix AVANT.
Est ce que le serveur pourrait gérer plusieurs parties ? .. YES MAIS il faudrait qu'il en gère au moins une bien  avant !
Est qu'il y aura une User Interface ? ... Pourquoi pas mais ce n'est pas obligatoire tout dépend de votre niveau et comment vous vous sentez . Le textuel peut aussi être une solution.
Est ce qu'il peut y avoir une déconnexion "brutale" ? YES !

Sur quoi ca doit s'exécuter ?  =>  Unix !  Linux ou Cygwin

Evaluation ?
ca va encore évoluer mais une partie pourrait être donné par un test grandeur nature et un vote
chacune aurait un certain nombre de points à donner ?

Calendrier
Sans doute livraison mi mai (grand max)
