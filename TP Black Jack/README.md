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


Vous recevez une carte : 4 de Coeur

Le croupier reçoit une carte.

Vous recevez une carte : 9 de Trèfle

Vous commencez avec : 13 points

------------------------------------------------------------------------------------

Entrer une action (pioche / stop) : █
```
---
### Déroulement du jeu
---
Au début du jeu, le programme s'occuper de vider le terminal pour plus de propreté en terme d'affichage.

Au début de la partie le joueur possède 2 cartes et le croupier 1 carte.

Dans la boucle ``while``, si le joueur est en jeu, on lui demande si il veut piocher, ou arrêter. Si la commande n'est pas comprise, on redemande au joueur une nouvelle fois.

Si le joueur décide de piocher, il tire alors une des cartes restantes dans le deck et on lui ajoute sa valeur au compteur du joueur. Si jamais il excède 21, le joueur perd instantanément.

Si le joueur décide de stop, alors il ne peut plus jouer et doit attendre le tour du croupier.

Le croupier piochera jusqu'à ce que la valeur de sa main excède 16, si jamais sa main excède 21, le croupier perd instantanément.

Si le joueur et le croupier son en dessous de 21 et qu'ils décident d'arrêter de tirer les cartes, les résultats tombent. Celui qui est le plus proche de 21 gagne, si les valeurs des deux joueurs sont égales, alors il y a égalité.