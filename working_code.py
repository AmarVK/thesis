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
import random
import numpy as np

pygame.init()										#	Initialize all imported pygame - modules (pygame constructor) 

d = np.loadtxt('/home/amarvk/Desktop/test.txt')
d = -d
peak= np.amax(d)
#gameDisplay = pygame.display.set_mode((800,600))	#	Initialize a window or screen for display
screen = pygame.display.set_mode((800,600))
black = [0, 0, 0]
white = [255, 255, 255]
yellow = [255, 255, 0]
red = [255, 0, 0]
screencolor = black
screen.fill(screencolor)
pygame.display.set_caption('Game On!')				#	Set the current window caption
clock = pygame.time.Clock()							#	Create an object - 'clock' to help track time

#   Football field Background
fieldimg = pygame.image.load('/home/amarvk/projects/thesis/field.png')
fieldimg = pygame.transform.scale(fieldimg, (716, 500))

# Goal image
goalimg = pygame.image.load('/home/amarvk/projects/thesis/goal.png')

#Ball image
ballimg = pygame.image.load('/home/amarvk/projects/thesis/ball.png')
ballimg = pygame.transform.scale(ballimg, (50, 50))

def field(x,y):
    screen.blit(fieldimg, (x,y))
x =  42
y = 50

def goal(x2,y2):
    screen.blit(goalimg, (x2,y2))
x2 =  300
y2 =  490

def ball(x1,y1):
    screen.blit(ballimg, (x1,y1))
x1 = 376
y1 = 50
y_change = 0.0
y_end = 0.0
y_step = 10

def bar(barx, bary, barw, barh, color):
    pygame.draw.rect(screen, color, [barx, bary, barw, barh])
bar_startx = 8
bar_starty = 8
bar_width = 20
bar_height = 2
bar_hchange = 50
bar_max = 0

def kickpower(power_count):
    font = pygame.font.Font('/home/amarvk/projects/thesis/font.ttf', 40)
    kickmeter = font.render('Kickmeter',1,white)
    text = font.render("Power: "+str(power_count)+ "%", True, white)
    screen.blit(text,(600,10))
    screen.blit(kickmeter,(30,10))
power_count = 0.00

crashed = False										#	Initialize the boolean - 'crashed' to false 	

#	The game loop logic runs as long as there is no crash
i =0
np.a = np.zeros(d.size)
while not crashed:									#	The game loop begins

    
    while(i<d.size):
        np.a[i]=d[i]/20  
        y_change = np.a[i]*10
        print np.a[i]
        i=i+1
        



        power_count = y_change*10
        y_end = 475*(y_change/10)
        bar_max = 500*(y_change/10)
        while (y1 < y_end):
            y1 += y_step
            bar_height += bar_hchange
            if bar_height > bar_max:
                bar_hchange = 0
            screen.fill(screencolor)
            field(x,y)        						
            ball(x1,y1)
            goal(x2,y2)
            bar(bar_startx, bar_starty, bar_width, bar_height, white)
            kickpower(power_count)
            pygame.display.update()						#	Updates the display screen only in the places where the event has changed
            clock.tick(10)								#	Max framerate of the game
#        pygame.time.delay(200)
#        y_change = 0.0
#        bar_height = 2
#        bar_hchange = 20
#        bar_max = 0
#        y1 = 33
#        screen.fill(screencolor)
#        field(x,y)        						
#        ball(x1,y1)
#        goal(x2,y2)
#        bar(bar_startx, bar_starty, bar_width, bar_height, white)
#        kickpower(power_count)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:				#	If the event is 'pygame.QUIT' - pressing of the 'X' button on the display window, the boolean crashed is flagged to a true value
                crashed = True
#    print (event) 								#	Displays the event log on the terminal screen
    pygame.display.update()						#	Updates the display screen only in the places where the event has changed
    clock.tick(10)								#	Max framerate of the game

pygame.quit()										#	Unitialize all pygame modules (pygame destructor)
quit()												#	Quit Python