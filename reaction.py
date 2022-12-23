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
	tileSprite=pygame.image.load('images/reaction_sprite.png').convert_alpha()
	tileX=125
	tileY=75
	cropX=0
	cropY=0
	cropWidth=150
	cropHeight=150
	
	selectedTile=random.randint(0,7)
	timeTaken=0
	totalScore=0
	found=False
	gameRound=0
	
	
	# The main game loop

	while looping:
	
		# INPUTS
	
		for event in pygame.event.get():
			if event.type == QUIT :
				pygame.quit()
				sys.exit()
			
					
			if found ==False and event.type == pygame.KEYDOWN:
				if (event.key == K_UP and selectedTile ==0):
					found=True
				if (event.key == K_LEFT and selectedTile ==1):
					found=True
				if (event.key == K_DOWN and selectedTile ==2):
					found =True
				if (event.key == K_RIGHT and selectedTile ==3):
					found= True
				if (event.key == K_w and selectedTile ==4):
					found =True
				if (event.key == K_a and selectedTile ==5):
					found= True
				if (event.key == K_s and selectedTile == 6):
					found =True
				if (event.key== K_d and selectedTile == 7):
					found=True
		
		#processing
		if found ==True:
			gameRound=gameRound +1
			print(f"Round: {gameRound},Score:{timeTaken}")
			totalScore=totalScore+timeTaken
			timeTaken=0
			selectedTile=random.randint(0,7)
			found=False
		if gameRound ==10:
			looping=False
		else:
			timeTaken=timeTaken+1
		if selectedTile<4:
			cropY=0
			cropX= selectedTile*150
		else:
			cropY=150
			cropX=(selectedTile -4) *150
		# RENDER 
		WINDOW.fill(MYSTERY)
		WINDOW.blit(tileSprite, (tileX, tileY), (cropX, cropY, cropWidth, cropHeight))
		
		
		pygame.display.update()
		fpsClock.tick(FPS)
		
		
	print(f"Total score: {totalScore}!")
	
main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
