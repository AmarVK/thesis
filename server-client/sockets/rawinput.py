import numpy as np
import pygame

    
# Game
i = 0

display_width = 800														#	Set display screen width	
display_height = 600													#	Set display screen height

ball_size = display_width/10

#	Initialize colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

pygame.init()															#	Initialize all imported pygame - modules (pygame constructor) 
gameDisplay = pygame.display.set_mode((display_width,display_height))	#	Initialize a window or screen for display
pygame.display.set_caption('Game On!')									#	Set the current window caption
clock = pygame.time.Clock()												#	Create an object - 'clock' to help track time

ballImg = pygame.image.load('/home/amarvk/projects/thesis/images/football.png')								#	Importing the football image into the game
ballImg = pygame.transform.scale(ballImg, (ball_size, ball_size))

goalImg = pygame.image.load('/home/amarvk/projects/thesis/images/goalpost.png')

def ball(x,y):															#	Creating a function - ball that displays the ball on given coordinates
	gameDisplay.blit(ballImg,(x,y))

x = (display_width * 0.45)												#	Setting the values of position of the ball
y = (display_height*0.8)

y_change = 0

crashed = False															#	Initialize the boolean - 'crashed' to false 	

#	The game loop logic runs as long as there is no crash

while not crashed:														#	The game loop begins
        
    for event in pygame.event.get():
        a = np.array([0,0,0])
        #while 1:# 
        #print "Enter something:"
        s = raw_input()
        try: 
            #print "You entered:", s
            a = np.hstack((a,float(s)))
            #print "The cumulative array is:", a
        except ValueError:
            pass
	    
        if event.type == pygame.QUIT:									#	If the event is 'pygame.QUIT' - pressing of the 'X' button on the display window, the boolean crashed is flagged to a true value
			crashed = True

        if (a[i] > a[i-1]):
				y_change =-5

        if (a[i] < a[i-1]):
				y_change = 5

        if (a[i] == a[i-1]):
        		y_change = 0
        i = i+1
	
	y += y_change

	gameDisplay.fill(green)												#	Background color 
																#	Display the ball
	gameDisplay.blit(goalImg,(270,0))
	ball(x,y)

	if (y_change!=0):
		print y_change
	pygame.display.update()												#	Updates the display screen only in the places where the event has changed
	clock.tick(60)														#	Max framerate of the game

pygame.quit()															#	Unitialize all pygame modules (pygame destructor)
quit()																	#	Quit Python
