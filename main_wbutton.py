#Following on how to setup and use pygame to set up game development
#src: https://www.digitalocean.com/community/tutorials/how-to-install-pygame-and-create-a-template-for-developing-games-in-python-3

import pygame
import msvcrt as m
from pygame.locals import *

pygame.init()

display_width = 1000
display_height = 1000

R1 = pygame.image.load("RH/right1.png")
R2 = pygame.image.load("RH/right2.png")
R3 = pygame.image.load("RH/right3.png")
R4 = pygame.image.load("RH/right4.png")
R5 = pygame.image.load("RH/right5.png")
DR = pygame.image.load("RH/deadRH.png")

L1 = pygame.image.load("LH/left1.png")
L2 = pygame.image.load("LH/left2.png")
L3 = pygame.image.load("LH/left3.png")
L4 = pygame.image.load("LH/left4.png")
L5 = pygame.image.load("LH/left5.png")
DL = pygame.image.load("LH/deadLH.png")

#Setting up display surface
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Bloody Chopsticks')

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BRIGHT_RED = (255,127,127)

X_CENTER=display_width/2 - 100/2
Y_CENTER=display_height/2 - 50/2
w=100
h=50
ac=BRIGHT_RED
ic=RED

#Updating the Display
#Creating the animations frame by frame using flip()
game_display.fill(WHITE)
game_display.blit(L5, (0, 0))
game_display.blit(R5, (500, 0))

mouse = pygame.mouse.get_pos()
#input("Press any KEY to START!")

#BUTTON CODE
#def button(msg,X_CENTER,Y_CENTER,w,h,ic,ac):
	#mouse = pygame.mouse.get_pos()
	#if X_CENTER+100 > mouse[0] > X_CENTER and Y_CENTER+50 > mouse[1] > Y_CENTER:
		#pygame.draw.rect(game_display, BRIGHT_RED,(X_CENTER,Y_CENTER + 200,w,h))
	#else:
		#pygame.draw.rect(game_display, RED,(X_CENTER,Y_CENTER + 200,w,h))
	
	#smallText = pygame.font.Font("freesansbold.ttf", 20)
	#textSurf, textRect = text_objects(msg, smallText)
	#textRect.center = ( (x+(w/2)), (y+(h/2)) )
    #game_display.blit(textSurf, textRect)

#button("Start",X_CENTER,Y_CENTER + 200,w,h,ic,ac)
pygame.display.update()
#flip() updates the whole display surface to the screen
#pygame.display.flip()
#update() used more frequently as it updates portions of the screen

#Creating the Game Loop
while True:
	#for loop to iterate through the user events within the event queue
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			quit()
	#pygame.display.update()

#start
#L5 R5
#glitchy flicker effect maybe? into 
#showing 2 pairs of hands facing each other
#slicing effect with screams, to begin with 1 finger each hand

#NPC Coming Soon
	#if Easy mode, randomized number of fingers to add
	#if Hard mode, can think of the rules to think ahead
#2 player game
#p1: can either tap p2's L1 or R1 and increment 1 finger on one of their hands.
#p2: can either tap p1's L1 or R1 to increment 2 or 1, depending on which hand they use
	#if p2 R2 to p1 R1, then p1 R3
	#if p2 R2 to p1 L1, then p1 L3
	#if p2 L1 to p1 R1, then p1 R2
	#if p2 L1 to p1 L1, then p1 L2



#rules
#if ((L2 | L4) & DR) | ((R2 | R4) & DL) BUMP
#	if L2, then display L1 & R1
#	if L4, then display L2 & R2
#	if R2, then display L1 & R1
#	if R4, then display L2 & R2


