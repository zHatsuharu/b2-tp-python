from classes import Cards, Joueur
import os
os.system('cls||clear')

deck = Cards()

joueur = Joueur()
croupier = Joueur()

dico = {
	"AS" : 11,
	"2" : 2,
	"3" : 3,
	"4" : 4,
	"5" : 5,
	"6" : 6,
	"7" : 7,
	"8" : 8,
	"9" : 9,
	"10" : 10,
	"Valet" : 10,
	"Dame" : 10,
	"Roi" : 10,
}

print("""

------------------------------------------------------------------------------------
    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗         ██╗ █████╗  ██████╗██╗  ██╗
    ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝         ██║██╔══██╗██╔════╝██║ ██╔╝
    ██████╔╝██║     ███████║██║     █████╔╝          ██║███████║██║     █████╔╝ 
    ██╔══██╗██║     ██╔══██║██║     ██╔═██╗     ██   ██║██╔══██║██║     ██╔═██╗ 
    ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗    ╚█████╔╝██║  ██║╚██████╗██║  ██╗
    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
------------------------------------------------------------------------------------

""")

for i in range(2):
	carte = deck.piocher()
	value = dico[carte.getValue()]
	joueur.addValue(value)
	print('Vous recevez une carte :', carte.display())
	print()
	carte = deck.piocher()
	value = dico[carte.getValue()]
	croupier.addValue(value)
	print('Le croupier reçoit une carte.')
	print()

print('Vous commencez avec :', joueur.getValue(), 'points')
print("""
------------------------------------------------------------------------------------
""")
while joueur.getPlay() or croupier.getPlay() :
	if (joueur.getPlay()) :
		get = input('Entrer une action (pioche / stop) : ')
		print()
		if (get == "pioche") :
			carte = deck.piocher()
			valeur = dico[carte.getValue()]
			if (carte.getValue() == "AS" and joueur.getValue() + valeur > 21):
				valeur = 1
			joueur.addValue(valeur)
			print('Vous avez piocher :', carte.display(), "Vous êtes à", joueur.getValue())

			if (joueur.getValue() > 21):
				joueur.stop()
				print('Vous arrêtez de jouer, la valeur de vos cartes exède 21.')

		elif (get == 'stop') :
			joueur.stop()
			print('Vous arrêtez de jouer. La valeur de vos cartes est de :', joueur.getValue())

		else :
			print("La commande n'a pas été comprise")
			continue
	else :
		print('Vous ne pouvez plus jouer. Veuillez attendre la fin.')

	print()
	if (croupier.getPlay()) :
		if (croupier.getValue() < 16) :
			carte = deck.piocher()
			valeur = dico[carte.getValue()]
			if (carte.getValue() == "AS" and croupier.getValue() + valeur > 21):
				valeur = 1
			croupier.addValue(valeur)
			print('Le croupier a pioché une carte.')
		
		else :
			croupier.stop()
			print('Le croupier arrête de jouer.')
	else :
		print('Le croupier a arrêté de jouer.')
	
	print("""
------------------------------------------------------------------------------------
	""")

if (21 - joueur.getValue() < 21 - croupier.getValue() and joueur.getValue() < 21) :
	print('Vous avez gagner la partie !')
elif (joueur.getValue() == croupier.getValue() or (joueur.getValue() > 21 and croupier.getValue() > 21)) :
	print('Égalité !')
else :
	if (croupier.getValue() > 21) :
		print('Vous avez gagner la partie !')
	else :
		print('Vous avez perdu la partie ...')

print('Vous :', joueur.getValue(), '| Croupier :', croupier.getValue())
print()