from random import randint

class Card:

	def __init__(self, value, color):
		self.value = value
		self.color = color

	def getValue(self):
		return self.value
	
	def getColor(self):
		return self.color
	
	def display(self):
		return f"{self.value} de {self.color}"

colors = ['Carreau', 'Trèfle', 'Coeur', 'Pique']
names = ["AS", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]

cardList = []
for value in names:
	for color in colors:
		cardList.append(Card(value, color))

class Cards:

	def __init__(self):
		self.deck = cardList
		self.compteur = len(cardList)

	def getDeck(self):
		return self.deck

	def getCompteur(self):
		return self.compteur

	def piocher(self):
		carte = self.deck[randint(0, self.compteur-1)]
		self.deck.remove(carte)
		self.compteur = len(self.deck)
		return carte

class Joueur:

	def __init__(self):
		self.value = 0
		self.play = True

	def getPlay(self):
		return self.play
	
	def getValue(self):
		return self.value

	def stop(self):
		self.play = False

	def addValue(self, value):
		self.value += value