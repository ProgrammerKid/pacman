import pygame
import time

#height and width of the screen: defualt presets
height = 500
width = 500

#actually creates the screen/surface the new surfaces name is called screen
screen = pygame.display.set_mode((height,width))

screen.fill((255,255,255)) #fills the surface with the color white
running = 1 #sets running to 1. 1 will always evaluate to true. whereas 0 will always evaluate to false.
#x represents the XLocation of the line
x = 20
y = 20
while running: #while running is allowed do this:
	event = pygame.event.poll() #will get all occurring events
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_UP:
			y = y - 10
		if event.key == pygame.K_DOWN:
			y = y + 10
		if event.key == pygame.K_RIGHT:
			x = x + 10
		if event.key == pygame.K_LEFT:
			x = x - 10
	pygame.draw.line(screen , (0,0,0) , (x,y) , (x,y+20)) #draws the line
	pygame.display.flip()
	screen.fill((255,255,255))
	time.sleep(.01)

	if event.type == pygame.QUIT: #when pygame is supposed to close it will change running to 0, which will evaluate to false. =)
		running = 0
