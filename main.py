import pygame
import math
from math import pi

# Innitialize the program
pygame.init()

# Windows and font setting
window = pygame.display.set_mode( ( 800, 600 ) )
myfont = pygame.font.SysFont( "monospace", 15 )

# Caption setting
pygame.display.set_caption("GroundStation Window")

# Color setting
colorblack = ( 0, 0, 0 )
colorwhite = (255,255,255)
colorgreen = ( 0, 255, 0 )
colorblue  = ( 0, 0, 255 )
colorred   = ( 255, 0, 0 )

# Map insert
image = pygame.image.load("image/map/map_n_001.jpg").convert_alpha()

gameLoop = True
clock = pygame.time.Clock()

# The main-loop
while gameLoop :
	clock.tick(10)

	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			gameLoop = False
	
	window.fill( colorwhite )
	window.blit( image, ( 0, 0 ) )
	
	for phase in range( 0, 314, 4 ):

		#
		clock.tick(1)	
	
		#
		window.fill( colorwhite )
		window.blit( image, ( 0, 0 ) )

		#
		aat = 100
		labelaa1 = myfont.render( ( "Altitde: %s" % aat ) , 1, colorblack )
		window.blit( labelaa1, ( 10, 420 ) )

		sep = 10
		labelaa2 = myfont.render( ( "  Speed: %s" % sep ), 1, colorblack )
		window.blit( labelaa2, ( 10, 440 ) )

		# Producing the fake GPS location
		GPSX = round( 440 + 10 * math.cos( phase / ( 10 * pi ) ) )
		GPSY = round( 220 - 10 * math.sin( phase / ( 10 * pi ) ) )

		labelaa3 = myfont.render( ( "  GPS.X: %s" % GPSX ) , 1, colorblack )
		window.blit( labelaa3, ( 10, 460 ) )

		labelaa4 = myfont.render( ( "  GPS.Y: %s" % GPSY ) , 1, colorblack )
		window.blit( labelaa4, ( 10, 480 ) )
	
		# Sketch the circle, but it should be the GPS posotion
		pygame.draw.circle( window, colorred, ( GPSX, GPSY ), 3, 3 )
		pygame.draw.circle( window, colorred, ( 700, 100 ), 50, 2 )
		pygame.draw.circle( window, colorred, ( 700, 200 ), 50, 2 )
	
		# Sketch the arc. The definition of location for arc sketch 
		# are ( cornor of x, cornor of y, length of x, length of y ) 
		# pygame.draw.arc( window, colorgreen, ( 650, 50, 100, 100 ), 0, pi/2, 10 )

		

		# Go ahead and update the screen with what we've drawn.
		# This MUST happen after all the other drawing commands.
		pygame.display.flip()

# Font setting function, T.B.D.

#	
pygame.quit()
