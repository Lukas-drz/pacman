import pygame
from pygame.locals import *
from random import *
import time

class Niveau:

	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0

	def generer(self):
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau


	def afficher(self, fenetre):

		mur = pygame.image.load("Structure/mur.png").convert()
		noir = pygame.image.load("Structure/noir.png").convert()
		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * 30
				y = num_ligne * 30
				if sprite == 'm':		   #m = Mur
					fenetre.blit(mur, (x,y))
					num_case += 1
				elif sprite == 'r' or sprite == 'p' or sprite == 'q':
					num_case += 1
			num_ligne += 1

class Perso:
	def __init__(self, droite, gauche, haut, bas, niveau):
		#Sprites du personnage
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		#Position du personnage en cases et en pixels
		self.case_x = 14
		self.case_y = 23
		self.x = 390
		self.y = 660
		#Direction par défaut
		self.direction = self.droite
		#Niveau dans lequel le personnage se trouve
		self.niveau = niveau


	def deplacer(self, direction):
		noir = pygame.image.load("Structure/noir.png").convert_alpha()
		#Déplacement vers la droite
		if direction == 'droite':
			if self.niveau.structure[self.case_y][self.case_x+1] == 'p':
				self.case_x = 0
			#On vérifie que la case de destination n'est pas un mur
			elif self.niveau.structure[self.case_y][self.case_x+1] != 'm':
				#Déplacement d'une case
				self.case_x += 1
				#Calcul de la position "réelle" en pixel
				self.x = self.case_x * 30
			#Image dans la bonne direction
			self.direction = self.droite

		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.niveau.structure[self.case_y][self.case_x-1] == 'q':
				self.case_x = 26
			elif self.niveau.structure[self.case_y][self.case_x-1] != 'm':
				self.case_x -= 1
				self.x = self.case_x * 30
			self.direction = self.gauche

		#Déplacement vers le haut
		if direction == 'haut':
			if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
				self.case_y -= 1
				self.y = self.case_y * 30
			self.direction = self.haut

		#Déplacement vers le bas
		if direction == 'bas':
			if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
				self.case_y += 1
				self.y = self.case_y * 30
			self.direction = self.bas

class Ghost:
	def __init__(self, droite, gauche, haut, bas, niveau):
		#Sprites du personnage
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()

	def ghost_deplacer(self, direction = 'gauche'):
		from random import randint
		a=randint(1,4)
		if a == 1:
			while self.niveau.structure[self.case_y-1][self.case_x] != 'm':
				if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * 30
				self.direction = self.haut
		if a == 2:
			while self.niveau.structure[self.case_y][self.case_x+1] != 'm':
				if self.niveau.structure[self.case_y][self.case_x+1] == 'p':
					self.case_x = 0
				elif self.niveau.structure[self.case_y][self.case_x+1] != 'm':
	                #Déplacement d'une case
					self.case_x += 1
	                #Calcul de la position "réelle" en pixel
					self.x = self.case_x * 30
	            #Image dans la bonne direction
				self.direction = self.droite
		if a == 3:
			while self.niveau.structure[self.case_y+1][self.case_x] != 'm':
				if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * 30
				self.direction = self.bas
		if a == 4:
			while self.niveau.structure[self.case_y][self.case_x-1] != 'm':
				if self.niveau.structure[self.case_y][self.case_x-1] == 'q':
					self.case_x = 26
				elif self.niveau.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * 30
				self.direction = self.gauche
		
class Ghost_red(Ghost):
	def __init__(self, droite, gauche, haut, bas, niveau):
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		self.case_x = 12
		self.case_y = 12
		self.x = 330
		self.y = 330
		self.direction = self.gauche
		self.niveau = niveau
		Ghost.ghost_deplacer(self)

class Ghost_pink(Ghost):
	def __init__(self, droite, gauche, haut, bas, niveau):
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		self.case_x = 12
		self.case_y = 14
		self.x = 330
		self.y = 390
		self.direction = self.bas
		self.niveau = niveau
		Ghost.ghost_deplacer(self)

class Ghost_cyan(Ghost):
	def __init__(self, droite, gauche, haut, bas, niveau):
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		self.case_x = 16
		self.case_y = 12
		self.x = 450
		self.y = 330
		self.direction = self.haut
		self.niveau = niveau
		Ghost.ghost_deplacer(self)

class Ghost_orange(Ghost):
	def __init__(self, droite, gauche, haut, bas, niveau):
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		self.case_x = 16
		self.case_y = 14
		self.x = 450
		self.y = 390
		self.direction = self.droite
		self.niveau = niveau
		Ghost.ghost_deplacer(self)

class pac_gomme:
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0
		image_pac_gomme = pygame.image.load("pac_gomme.png").convert_alpha()

	def generation(self):
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau

	def affichage(self, fenetre):
		image_pac_gomme = pygame.image.load("pac_gomme.png").convert_alpha()
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * 30
				y = num_ligne * 30
				if sprite == 'm':
					num_case += 1
				if sprite == 'l':		   #m = Mur
					fenetre.blit(image_pac_gomme, (x,y))
					num_case += 1
				if sprite == 'r':
					num_case += 1
				if sprite == 'q':
					num_case += 1
				if sprite == 'p':
					num_case += 1
			num_ligne += 1

class Baie:
	def __init__(self, design, niveau):
		self.design = pygame.image.load(design).convert_alpha()
		self.niveau = niveau
		self.case_x = 2
		self.case_y = 2
		self.x = 30
		self.y = 30
		self.direction = self.design
