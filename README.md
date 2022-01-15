# Rendu TP python BLACKJACK

```
------------------------------------------------------------------------------------
    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗         ██╗ █████╗  ██████╗██╗  ██╗
    ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝         ██║██╔══██╗██╔════╝██║ ██╔╝
    ██████╔╝██║     ███████║██║     █████╔╝          ██║███████║██║     █████╔╝ 
    ██╔══██╗██║     ██╔══██║██║     ██╔═██╗     ██   ██║██╔══██║██║     ██╔═██╗ 
    ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗    ╚█████╔╝██║  ██║╚██████╗██║  ██╗
    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
------------------------------------------------------------------------------------
```
---
## Sommaire
- [I - L'architecture du TP](#i---l'architecture-du-tp)
- [II - Les classes](#ii---les-classes)
- [III - Le fonctionnement du jeu](#iii---le-fonctionnement-du-jeu)
---
## I - L'architecture du TP

Le tp est réparti en 2 fichier :
- ``blackjack.py`` : fait fonctionner le jeu.
- ``classes.py`` : contient les classes pour le fonctionnement du jeu.

Ainsi on réparti le code pour une meilleur compréhension.

## II - Les classes

Les classes sont répartis dans le fichier ``classes.py``.

Il y a dans ce fichier 3 classes :
- ``Card`` : contient les informations des cartes, leurs valeur (AS, Dame, 2, etc.) et leur couleur (Carreau, pique, etc.) 
- ``Cards`` : il s'agit du deck, toutes les cartes sont dedans. On peut tirer une carte et la carte sera alors enlever du paquet.
- ``Joueur`` : cette classe est faites pour compter les points des joueurs et savoir s'ils jouent encore.

Ainsi par ce fonctionnement, on peut séparer chaque fonctionnalité et se repérer plus facilement sur les variables.

## III - Le fonctionnement du jeu
---
### Lancement du jeu
---
Pour lancer le jeu, il faut faire dans le terminal :
```shell
$ py blackjack.py
```

Le jeu se présentera comme cela :
```shell


------------------------------------------------------------------------------------
    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗         ██╗ █████╗  ██████╗██╗  ██╗
    ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝         ██║██╔══██╗██╔════╝██║ ██╔╝
    ██████╔╝██║     ███████║██║     █████╔╝          ██║███████║██║     █████╔╝
    ██╔══██╗██║     ██╔══██║██║     ██╔═██╗     ██   ██║██╔══██║██║     ██╔═██╗
    ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗    ╚█████╔╝██║  ██║╚██████╗██║  ██╗
    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
------------------------------------------------------------------------------------


Vous recevez une carte : 7 de Carreau

Le croupier reçoit une carte.

Vous recevez une carte : 10 de Coeur

Le croupier reçoit une carte.

Vous commencez avec : 17 points

------------------------------------------------------------------------------------

Entrer une action (pioche / stop) : █
```
---
### Déroulement du jeu
---
Au début du jeu, le programme s'occuper de vider le terminal pour plus de propreté en terme d'affichage.

Au début de la partie une boucle ``for`` s'occupe d'effectuer les 2 premiers tirages de la pioche.  Une fois les cartes données, une boucle ``while`` démarre avec comme condition, si le croupier ou le joueur est encore en jeu, la boucle continue.

Dans la boucle ``while``, si le joueur est en jeu, on lui demande si il veut piocher, ou arrêter. Si la commande n'est pas comprise, on redemande au joueur une nouvelle fois.

Si le joueur décide de piocher, il tire alors une des cartes restantes dans le deck et on lui ajoute sa valeur au compteur du joueur. Si jamais il excède 21, on force le joueur à arrêter.

Si le joueur décide de stop, alors il ne peut plus jouer et doit attendre que le croupier termine.

Une fois que le joueur fait une action, le croupier joue à son tour. Il tire des cartes tant que la valeur de sa main n'excède pas 16.

Quand les 2 joueurs ont arrêté de jouer, les résultats tombent. Si les 2 joueurs excèdent 21 ou que leurs mains ont la même valeur, alors c'est une égalité. Sinon, c'est celui qui est en dessous de 21 ou celui qui se rapproche le plus de 21 qui gagne la partie.