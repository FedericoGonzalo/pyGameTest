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
	
	tom =pygame.image.load('images/tom_standing.png').convert_alpha()
	
	
	tomX=10
	tomY=40
	
	tom = pygame.transform.scale(tom,(50,95))
	tomLeft=pygame.transform.flip(tom,True,False)
	tomRunning=tom
	tomJumpVelocity=-21
	jumpStrength=20
	
	
	characterWidth=50
	characterHeight=95
	
	
	# The main game loop

	while looping:
	
		# INPUTS
		# keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == QUIT :
				pygame.quit()
				sys.exit()
			
					
		pressed = pygame.key.get_pressed()
		if (pressed[K_RIGHT] or pressed[K_d]):
			tomX=tomX+3
			tomRunning=tom
		if (pressed[K_LEFT] or pressed[K_a]):
			tomX=tomX-3
			tomRunning=tomLeft
		if (pressed[K_SPACE] and tomJumpVelocity < -jumpStrength):
			tomJumpVelocity=jumpStrength
			
		#processing
		if tomJumpVelocity >= -jumpStrength:
			tomY= tomY - tomJumpVelocity
			tomJumpVelocity= tomJumpVelocity -1
		
		
		
		
		
		# RENDER 
		WINDOW.fill(MYSTERY)
		WINDOW.blit(tomRunning,(tomX,tomY))
		
		pygame.display.update()
		
		fpsClock.tick(FPS)

main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
