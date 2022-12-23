import pygame, sys, random
from pygame.locals import *
pygame.init()

#Colores

MYSTERY=(247,184,37)
CHARACTER=(255,30,70)
# Game Setup
FPS =60
fpsClock=pygame.time.Clock()
WINDOW_WIDTH=400
WINDOW_HEIGHT=300

WINDOW=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('PYGAME TEST ARG')


#funcion principal
def main():
	looping=True
	characterX=10
	characterY=30
	characterWidth=50
	characterHeight=70
	
	
	# The main game loop

	while looping:
	
		# INPUTS
		# keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == QUIT :
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN and event.key== K_r:
				characterX=10
				characterY=30
			if event.type == pygame.KEYUP and event.key==K_r:
				characterX=340
				characterY=200
					
			pressed =pygame.key.get_pressed()
			if (pressed[K_RIGHT] or pressed[K_d]):
				characterX=characterX+3
			if (pressed[K_LEFT] or pressed[K_a]):
				characterX=characterX-3	
			if (pressed[K_DOWN] or pressed[K_s]):
				characterY=characterY+3
			if (pressed[K_UP] or pressed[K_w]):
				characterY=characterY-3
		#processing
		#limite derecho
		if (characterX+characterWidth >WINDOW_WIDTH):
			characterX=characterX-3
		#limite izq
		if (characterX<0):
			#characterX=0
			characterX=characterX+3	
		#limite abajo	
		if (characterY+characterHeight >WINDOW_HEIGHT):
			characterY=WINDOW_HEIGHT-characterHeight	
		
		#limite arriba y salta abajo
		if(characterY<0):
			characterY=WINDOW_HEIGHT-characterHeight
			
		character=pygame.Rect(characterX,characterY,characterWidth,characterHeight)
		
		
		
		# RENDER 
		WINDOW.fill(MYSTERY)
		pygame.draw.rect(WINDOW,CHARACTER,character)
		pygame.display.update()
		
		fpsClock.tick(FPS)

main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
