#!/usr/bin/python3
# -*- coding: Utf-8 -*
import pygame
from pygame.locals import *
from classes import *
from random import *
import time
pygame.init()

#Affichage page d'accueil
fenetre = pygame.display.set_mode((400, 400))
icone = pygame.image.load("icone.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("PacMan ISN La Merci : Lukas Deronzier, Mathieu Dumarcel, Jules Majoulet")

#Déplacement continu
pygame.key.set_repeat(200, 20)
derniere_touche = ""
#variable lors de K_ESCAPE
em=0
eh=0
h=0

#variable pour la boucle
continuer = 1
#Début boucle principale
while continuer:
    accueil = pygame.image.load("Title screen/title screen.png").convert()
    fenetre.blit(accueil,(0,0))
    pygame.display.flip()

    continuer_jeu = 1
    continuer_accueil = 1


    while continuer_accueil == 1:

        pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == QUIT:
                continuer_jeu = 0
                continuer_accueil = 0
                continuer = 0

            #Echappe du menu
            if h==0 and event.type == KEYDOWN and event.key == K_ESCAPE or h==0 and event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]<108 and event.pos[0]>20 and event.pos[1]<267 and event.pos[1]>232 :
                echappe_menu = pygame.image.load("Echappe/Echappe.png").convert()
                fenetre.blit(echappe_menu,(0,133))
                pygame.display.flip()
                em=1
                choix = 0

            #Oui ou Non du Echappe du menu
            if em==1 and event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]<147 and event.pos[0]>71 and event.pos[1]<232 and event.pos[1]>201:
                continuer_jeu = 0
                continuer_accueil = 0
                continuer = 0

            if em == 1 and event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]<332 and event.pos[0]>243 and event.pos[1]<232 and event.pos[1]>201:
                fenetre.blit(accueil,(0,0))
                pygame.display.flip()
                em=0

            #Help pages
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]<109 and event.pos[0]>20 and event.pos[1]<225 and event.pos[1]>192:
                help1=pygame.image.load("Help screen/Help1.png").convert()
                fenetre.blit(help1,(0,0))
                pygame.display.flip()
                h=1

            #Echappe du Help
            if h==1 and event.type == KEYDOWN and event.key == K_ESCAPE:
                echappe_help = pygame.image.load("Echappe/Echappe help.png").convert()
                fenetre.blit(echappe_help,(0,133))
                pygame.display.flip()
                eh=1

            #Oui ou Non du Echappe du Help
            if eh==1 and event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]<137 and event.pos[0]>72 and event.pos[1]<233 and event.pos[1]>208:
                fenetre.blit(accueil,(0,0))
                pygame.display.flip()
                eh=0
                h=0

            if eh == 1 and event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]<322 and event.pos[0]>246 and event.pos[1]<230 and event.pos[1]>209:
                fenetre.blit(help1,(0,0))
                pygame.display.flip()

            #Lorsque l'on appuie sur PLAY
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]<108 and event.pos[0]>19 and event.pos[1]<184 and event.pos[1]>151:
                continuer_accueil = 0
                choix = 'n1'

    if choix != 0:
        fenetre_jeu = pygame.display.set_mode((810,750))
        fond = pygame.image.load("Structure/fond.jpg").convert()
        fenetre_jeu.blit(fond,(0,0))
        niveau = Niveau(choix)
        niveau.generer()
        niveau.afficher(fenetre)
        Pacman = Perso("Perso/droite.png", "Perso/gauche.png", "Perso/haut.png", "Perso/bas.png", niveau)
        Ghost_red = Ghost_red("Ghost/Red/droite.png", "Ghost/Red/gauche.png", "Ghost/Red/haut.png", "Ghost/Red/bas.png", niveau)
        Ghost_pink = Ghost_pink("Ghost/Pink/droite.png", "Ghost/Pink/gauche.png", "Ghost/Pink/haut.png", "Ghost/Pink/bas.png", niveau)
        Ghost_cyan = Ghost_cyan("Ghost/Cyan/droite.png", "Ghost/Cyan/gauche.png", "Ghost/Cyan/haut.png", "Ghost/Cyan/bas.png", niveau)
        Ghost_orange = Ghost_orange("Ghost/Orange/droite.png", "Ghost/Orange/gauche.png", "Ghost/Orange/haut.png", "Ghost/Orange/bas.png", niveau)

        Baie = Baie("baie.png", niveau)

    pygame.key.get_pressed()

    while continuer_jeu == 1:

		#Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)
        Ghost_red.ghost_deplacer()
        Ghost_orange.ghost_deplacer()
        Ghost_pink.ghost_deplacer()
        Ghost_cyan.ghost_deplacer()

        for event in pygame.event.get():

            if event.type == QUIT:
                continuer_jeu = 0
                continuer = 0
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    Pacman.deplacer('droite')
                    #derniere_touche = "right"
                if event.key == K_LEFT or event.key == K_a: #a car pygame est en qwerty, a correspond à q sur un clavier azerty
                    Pacman.deplacer('gauche')
                    #derniere_touche = "left"
                if event.key == K_DOWN or event.key == K_s:
                    Pacman.deplacer('bas')
                    #derniere_touche = "down"
                if event.key == K_UP or event.key == K_w: #w car pygame est en qwerty, w correspond à z sur un clavier azerty
                    Pacman.deplacer('haut')
                    #derniere_touche = "up"
                if event.key == K_ESCAPE or event.key == K_F4 and bool(event.mod & KMOD_ALT):
                    #echappe_jeu = pygame.image.load("Echappe/Echappe jeu.png").convert()
                    #fenetre_jeu.blit(echappe_jeu,(690,540))
                    #pygame.display.flip()
                    continuer = 0
                    continuer_accueil = 0
                    continuer_jeu = 0
                #while not pygame.key.get_focused():
                #    if derniere_touche == "right":
                #        Pacman.deplacer('droite')
                #    if derniere_touche == "left":
                #        Pacman.deplacer('gauche')
                #    if derniere_touche == "down":
                #        Pacman.deplacer('bas')
                #    if derniere_touche == "up":
                #        Pacman.deplacer('haut')

		#Affichages aux nouvelles positions
        fenetre.blit(fond, (0,0))
        niveau.afficher(fenetre)
        fenetre.blit(Baie.direction, (Baie.x, Baie.y))
        fenetre.blit(Pacman.direction, (Pacman.x, Pacman.y))
        fenetre.blit(Ghost_red.direction, (Ghost_red.x, Ghost_red.y))
        fenetre.blit(Ghost_pink.direction, (Ghost_pink.x, Ghost_pink.y))
        fenetre.blit(Ghost_orange.direction, (Ghost_orange.x, Ghost_orange.y))
        fenetre.blit(Ghost_cyan.direction, (Ghost_cyan.x, Ghost_cyan.y))
        pygame.display.flip()


pygame.quit()