import pygame, sys, random
from pygame.locals import *
pygame.init()

#Colores

MYSTERY=(247,184,37)
CHARACTER=(255,30,70)
TEXTCOLOR=(200,100,0)
# Game Setup
FPS =60
fpsClock=pygame.time.Clock()
WINDOW_WIDTH=400
WINDOW_HEIGHT=300

WINDOW=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('PYGAME TEST ARG')
BOTTOMLINEHEIGHT = 20
# Fuentes de texto
#Fuente default
#fontObj=pygame.font.Font(None,32)
#si usamos fuente local###==>ver fuentesInst.py
#fontObj=pygame.font.SysFont('fuente_lista',32)
#si usamos fuente que este dentro del proyecto en carpeta ej "nombreProyecto/fonts"
fontObj= pygame.font.Font('fonts/PressStart2P-Regular.ttf',16)
"""
four arguments :
The text to render ('blah blah')
If we are antialaising the text or not (True)
The colour of the text (TEXTCOLOUR)
The background colour of the surface (None - which means transparent)
"""
textSufaceObj=fontObj.render('blah blah',True,TEXTCOLOR,None)
#PONER TEXTO EN RECTANGULO
textRectObj=textSufaceObj.get_rect()
textRectObj.midbottom=(WINDOW_WIDTH // 2,WINDOW_HEIGHT -BOTTOMLINEHEIGHT - 15)
#funcion principal
def main():
	looping=True
	# The main game loop
	while looping:	
		# INPUTS
	
		for event in pygame.event.get():
			if event.type == QUIT :
				pygame.quit()
				sys.exit()
		
		#processing
		
		# RENDER 
		WINDOW.fill(MYSTERY)
		WINDOW.blit(textSufaceObj,textRectObj)
		pygame.draw.line(WINDOW, TEXTCOLOR, (0, WINDOW_HEIGHT - BOTTOMLINEHEIGHT), (WINDOW_WIDTH, WINDOW_HEIGHT - BOTTOMLINEHEIGHT), 3)
		pygame.display.update()
		fpsClock.tick(FPS)
		
		
	
	
main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
