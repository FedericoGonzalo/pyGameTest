import pygame, sys, random
from pygame.locals import *
pygame.init()

#Colores

MYSTERY=(247,184,37)
TEXTCOLOR=(200,100,0)
# Game Setup
FPS =60
fpsClock=pygame.time.Clock()
WINDOW_WIDTH=400
WINDOW_HEIGHT=300

WINDOW=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('PYGAME TEST ARG')

# Fuentes de texto
fontObj= pygame.font.Font('fonts/PressStart2P-Regular.ttf',16)
derTex=fontObj.render('DERECHA VIDELISTA',True,TEXTCOLOR,None)
izqTex=fontObj.render('IZQUIERDA SUBVERSIVA',True,TEXTCOLOR,None)
#PONER TEXTO EN RECTANGULO
derTexRectObj=derTex.get_rect()
izqTexRectObj=izqTex.get_rect()
#CENTRALIZAR LOS TEXTOS
derTexRectObj.center=(WINDOW_WIDTH //2,WINDOW_HEIGHT //2)
izqTexRectObj.center=(WINDOW_WIDTH //2,WINDOW_HEIGHT //2)
#SELECTOR DERECHA O IZQUIERDA
def elige_lado():
	lado=''
	elegido=random.randint(0,1)
	if elegido == 1:
		lado='DERECHA VIDELISTA'
	else:
		lado='IZQUIERDA SUBVERSIVA'
	return lado
#funcion principal
def main():
	looping=True
	
	victima =  elige_lado()
	vuelta=0
	puntos=0
	ronda=10
	activo=True
	
	# The main game loop
	while looping:
		ladoElegido=''	
		# INPUTS
		for event in pygame.event.get():
			if event.type == QUIT :
				pygame.quit()
				sys.exit()
		pressed = pygame.key.get_pressed()
		if pressed[K_RIGHT]:
			ladoElegido='DERECHA VIDELISTA'
		elif pressed[K_LEFT]:
			ladoElegido='IZQUIERDA SUBVERSIVA'
			
		#processing
		if ladoElegido != '' and ladoElegido != victima and activo == True :
			print('ALCOYANA ALCOYANA')
			vuelta=vuelta+1
			puntos=puntos+1
			activo=False
		elif ladoElegido == victima and activo == True :
			print('MAL AHI EH')
			vuelta=vuelta+1
			activo=False
		elif activo == False and ladoElegido == '':
			activo=True
			victima=elige_lado()
		if vuelta == ronda:
			looping=False
			
		
		# RENDER 
		WINDOW.fill(MYSTERY)
		if victima == 'DERECHA VIDELISTA' and activo == True:
			WINDOW.blit(derTex,derTexRectObj)
		elif victima == 'IZQUIERDA SUBVERSIVA' and activo == True:
			WINDOW.blit(izqTex,izqTexRectObj)
			
		pygame.display.update()
		fpsClock.tick(FPS)
	print ('JUEGO FINALIZADO')
	print (f'Tus puntos : {puntos}')
		
		
	
	
main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
