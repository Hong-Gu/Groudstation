import pygame

pygame.init()

# Windows setting
window = pygame.display.set_mode((800,600))

# Caption setting
pygame.display.set_caption("GroundStation Window")

# Color setting
color_black = ( 0, 0, 0 )
color_white = (255,255,255)
color_green = ( 0, 255, 0 )
color_blue  = ( 0, 0, 255 )
color_red   = ( 255, 0, 0 )

# Map insert
image = pygame.image.load("image/map/map_n_001.jpg").convert_alpha()

gameLoop = True

# The main-loop
while gameLoop :
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            gameLoop = False


    window.fill(color_white)

    window.blit( image, ( 0, 0 ) )

    # Sketch the circle
    pygame.draw.circle( window, color_red, ( 480, 220 ), 5, 5 )
    pygame.draw.circle( window, color_red, ( 700, 100 ), 50, 2 )
    pygame.draw.circle( window, color_red, ( 700, 200 ), 50, 2 )
	
    # Need study...
    pygame.display.flip()

pygame.quit()
