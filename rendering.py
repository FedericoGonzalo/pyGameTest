import pygame, sys, random
from pygame.locals import *
pygame.init()

#Colores
BACKGROUND =(255, 255,255)
FULLRED=(255,0,0)
FULLGREEN=(0,255,0)
FULLBLUE=(0,0,255)
MYSTERY=(247,184,37)
RED=(255,30,70)
BLUE=(10,20,200)
GREEN=(50,230,40)

# Game Setup
FPS =60
fpsClock=pygame.time.Clock()
WINDOW_WIDTH=400
WINDOW_HEIGHT=400

WINDOW=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('PYGAME TEST ARG')


#funcion principal
def main():
	looping=True
	
	# The main game loop

	while looping:
		#filter = True 
		
		# INPUTS
		for event in pygame.event.get():
			if event.type == QUIT :
				pygame.quit()
				sys.exit()
		#processing
		#RECTANGULOS
		#pygame.Rect(Xcoordinate, Ycoordinate, width, height)
		rectan1=pygame.Rect(10,30,50,70)
		rectan2=pygame.Rect(30,40,70,50)
		rectan3=pygame.Rect(20,50,50,70)
		#DETALLES DE Rect
		"""
		
		Attribute name	        Attribute value
		rectangle1.left	        The X coordinate of the left side of the rectangle.
		rectangle1.right	The x coordinate of the right side fo the rectangle.
		rectangle1.top	        The Y coordinate of the top side of the rectangle.
		rectangle1.bottom	The Y coordinate of the bottom side of the rectangle.
		rectangle1.width	The width of the rectangle.
		rectangle1.height	The height of the rectangle
		rectangle1.size	        A tuple of two values, the width and height of the rectangle.
		rectangle1.topleft	A tuple of the X, Y coordinates of the top left of the rectangle.
		rectangle1.topright	A tuple of the X, Y coordinates of the top right of the rectangle.
		rectangle1.bottomleft	A tuple of the X, Y coordinates of the bottom left of the rectangle.
		rectangle1.bottomright	A tuple of the X, Y coordinates of the bottom right of the rectangle.
		rectangle1.midleft	A tuple of the X, Y coordinates of the middle of the left side of the rectangle.
		rectangle1.midright	A tuple of the X, Y coordinates of the middle of the right side of the rectangle.
		rectangle1.midtop	A tuple of the X, Y coordinates of the middle of the top side of the rectangle.
		rectangle1.midbottom	A tuple of the X, Y coordinates of the middle of the bottom side of the rectangle.
		rectangle1.centerx	The X coordinate of the center of the rectangle.
		rectangle1.centery	The Y coordinate of the center of the rectangle.
		rectangle1.center	A tuple of the X, Y coordinates of the center of the rectangle.

		"""
		
		
			
		#ELIPSES primero como un rectangulo
		elipse1=pygame.Rect(70,200,40,100)
		
		
		# RENDER 
		WINDOW.fill(MYSTERY)
		pygame.draw.rect(WINDOW,RED,rectan1,1)
		pygame.draw.rect(WINDOW,GREEN,rectan2,2)
		pygame.draw.rect(WINDOW,BLUE,rectan3,3)
		
		#CIRCULOS
		#pygame.draw.circle(surface, colour, center, radius, width) 		
		# width is optional
		pygame.draw.circle(WINDOW,GREEN,(160,70),30)
		pygame.draw.circle(WINDOW,BLUE,(200,90),50,4)
		#CIRCULO DIVIDIDO EN CUADRANTES
		#pygame.draw.circle(surface, colour, center, radius, width, 
		#topRight, topLeft, bottomLeft, bottomRight)
		pygame.draw.circle(WINDOW,RED,(200,220),50,2,True,False,True,False)
		#ELIPSIS RENDER
		#pygame.draw.ellipse (surface, colour, rect, width)
		# width is optional
		pygame.draw.ellipse(WINDOW,RED,elipse1)
		pygame.draw.ellipse(WINDOW,BLUE,elipse1,6)
		#LINEAS
		#pygame.draw.line(surface, colour, (startX, startY), (endX, endY), width)
		pygame.draw.line(WINDOW,GREEN,(0,200),(400,200),10)
		pygame.draw.line(WINDOW,RED,(200,0),(200,400),10)
		#POLIGONO
		#pygame.draw.polygon(surface, colour, points, width) 
		# width is optional
		pygame.draw.polygon(WINDOW,BLUE,((100,140),(120,120),(130,160),(120,200),(110,180)))
		pygame.draw.polygon(WINDOW,RED,((100,140),(120,120),(130,160),(120,200),(110,180)),5)
		pygame.display.update()
		
		fpsClock.tick(FPS)

main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
