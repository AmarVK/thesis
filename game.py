#	ENSE 799 - Master's thesis
#	Amar Vamsi Krishna - UID : 114921871
#	University of Maryland, College Park
#	Date : 25th October, 2017
#	Advisor : Dr. Anindo Roy
#	Topic : Development of a novel interactive visual task for robot assisted gait training in stroke
#	Task 2.1: Programming - Create a Video game - create a screen cursor and visual environment
#	Version-1 : Creating a window using pygame and displaying the events (Keyboard presses and mouse movements) on the terminal window
#	Configuration and Dependancies - Uses python version2.7.12 and pygame version 1.9.3. Currently using Spyder IDE and Sublime Text editor for development
#	Source for the tutorial : https://pythonprogramming.net/pygame-python-3-part-1-intro/

import pygame

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

ballImg = pygame.image.load('/home/amarvk/projects/thesis/football.png')								#	Importing the football image into the game
ballImg = pygame.transform.scale(ballImg, (ball_size, ball_size))

goalImg = pygame.image.load('/home/amarvk/projects/thesis/goalpost.png')

def ball(x,y):															#	Creating a function - ball that displays the ball on given coordinates
	gameDisplay.blit(ballImg,(x,y))

x = (display_width * 0.45)												#	Setting the values of position of the ball
y = (display_height*0.8)

y_change = 0

crashed = False															#	Initialize the boolean - 'crashed' to false 	

#	The game loop logic runs as long as there is no crash

while not crashed:														#	The game loop begins
        
	for event in pygame.event.get():									#	Gets all the events from the game
		if event.type == pygame.QUIT:									#	If the event is 'pygame.QUIT' - pressing of the 'X' button on the display window, the boolean crashed is flagged to a true value
			crashed = True	

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				y_change =-5

			if event.key == pygame.K_DOWN:
				y_change = 5

        if event.type == pygame.KEYUP:
        	if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        		y_change = 0
	
	y += y_change

	gameDisplay.fill(green)												#	Background color 
																#	Display the ball
	gameDisplay.blit(goalImg,(270,0))
	ball(x,y)

	print event
	pygame.display.update()												#	Updates the display screen only in the places where the event has changed
	clock.tick(60)														#	Max framerate of the game

pygame.quit()															#	Unitialize all pygame modules (pygame destructor)
quit()																	#	Quit Python