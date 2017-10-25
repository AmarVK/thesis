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

pygame.init()										#	Initialize all imported pygame - modules (pygame constructor) 
gameDisplay = pygame.display.set_mode((800,600))	#	Initialize a window or screen for display
pygame.display.set_caption('Game On!')				#	Set the current window caption
clock = pygame.time.Clock()							#	Create an object - 'clock' to help track time

crashed = False										#	Initialize the boolean - 'crashed' to false 	

#	The game loop logic runs as long as there is no crash

while not crashed:									#	The game loop begins
        
    for event in pygame.event.get():				#	Gets all the events from the game
        if event.type == pygame.QUIT:				#	If the event is 'pygame.QUIT' - pressing of the 'X' button on the display window, the boolean crashed is flagged to a true value
            crashed = True							
        
        print event 								#	Displays the event log on the terminal screen
        pygame.display.update()						#	Updates the display screen only in the places where the event has changed
        clock.tick(60)								#	Max framerate of the game

pygame.quit()										#	Unitialize all pygame modules (pygame destructor)
quit()												#	Quit Python