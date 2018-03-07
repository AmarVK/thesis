# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 11:42:50 2018

@author: Suchitra Chandar
"""

import pygame
import xlrd
from scipy import stats

import display

pygame.init()										#	Initialize all imported pygame - modules (pygame constructor) 

screen = pygame.display.set_mode((800,600))             #	 Initialize a window or screen for display
pygame.display.set_caption('Game On!')      				#   Set the current window caption
clock = pygame.time.Clock()						           	#	Create an object - 'clock' to help track time

def game_intro():
    intro = True
    action = "None"
    
    while intro:
        events = pygame.event.get()
        for event in events:
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        action1 = display.intro(screen,action)
        if action1 == "Dorsi":
            game_loop(action1)
        elif action1 == "Plantar":
            game_loop(action1)
        pygame.display.update()
        clock.tick(200)
        
def game_loop(action):
    if action == "Dorsi":
                       
        L = 300                 #   Initial Start position
        Lmax = 550              #   Max start positiom
        Lmin = 100              #   Min start position position
        ymin = 67               #   Min y position of ball
        ymax = 488
        flag = False             #   Used to detect change in gait_cycle
                
    elif action == "Plantar":
        
        L = 250                 #   Initial Start position
        Lmax = 400              #   Max start positiom
        Lmin = 50               #   Min start position position
        ymax = 488              #   Max y position of ball
        flag = True             #   Used to detect change in gait_cycle
        
    footswitch = []
    torque = []
    
    deltaL = 0              #   actual pixel offset for machine learning
    beta = 50               #   Default pixel offset
    liney = L               #   Initial Start-line y position (same as Start position)
    y1 = L                  #   Initial Ball y position (same as Initial Start position)
    y1actual = 0            #   Initial y value wrt torque profile
    alpha_sens = 41.66      #   Sensitivity from dialog box (pixels/Nm)  
    barh = 2                #   Power bar height in pixels
    count = 0               #   Used for indexing data from .xlsx file
    read_value = 0          #   Initializing current torque value
    prev_value = 0          #   Initializing max torque value in the current gait cycle
    gait_cycle = 0          #   Initializing gait_cycle count
    print(gait_cycle+1)
    sample_size = 7         #   Setting the window size for machine learning
    max_torque = [0]*sample_size            #   Initializing an empty list of length= sample_size to store max torque values of every iteration
    index = [0]*sample_size 
    score = 0
    total_score = 0
    score_display_max = 100
    score_display = 0
    crashed = False         #	Initialize the boolean - 'crashed' to false
    while not crashed:									#	The game loop begins
            
        for event in pygame.event.get():				#	Gets all the events from the game
            if event.type == pygame.QUIT:			#	If the event is 'pygame.QUIT' - pressing of the 'X' button on the display window, the boolean crashed is flagged to a true value
                crashed = True	
                pygame.quit()
                quit()
                
        footswitch_values = float (raw_input())
        torque_values = float(raw_input())
        footswitch.append(footswitch_values)
        torque.append(torque_values)
        
        if torque[count] > 0:
            torque[count] = 0.00
        else:
            torque[count] = (-1)*torque[count]

        if footswitch[count] < 0.3:
            torque[count] = 0
            footswitch[count] = 0
        else: footswitch[count] = 1
        
        read_value = torque[count]
        index[gait_cycle] = gait_cycle + 1
        
        if flag == False:           #   Phase not under consideration: no ball movement
            score_display +=1
            if score_display > score_display_max:
                prev_value = 0          #   New gait_cycle detected; set max torque value to zero
                score = 0
            if footswitch[count] != 0:          #   Wait for stance phase 
                flag = True
        elif flag == True:          #   Phase under consideration
            score_display = 0
            if read_value>prev_value:
                prev_value = read_value
            if footswitch[count] == 0:          #   New gait cycle detected
                flag = False
                gait_cycle += 1
                total_score = total_score + score
                print(max_torque)
                if gait_cycle < sample_size: print(gait_cycle+1)
            if gait_cycle < sample_size:
                max_torque[gait_cycle] = prev_value            #   save max_torque for gait_cycle < sample size
                index[gait_cycle] = gait_cycle + 1
            else:
#                #   Compare last sample with the average of the rest and decide improvement and declining
#                average_torque = sum(max_torque[:sample_size-1])/(sample_size-1)
#                R = (max_torque[sample_size-1]/average_torque)
#                if average_torque < max_torque[sample_size-1]:
#                    print('Improvement')
#                    deltaL = beta*R
#                    print(deltaL)
#                    L = L - deltaL
#                    if L < Lmin:
#                        L = Lmin
#                        alpha_sens = 0.9*alpha_sens
#                elif average_torque > max_torque[sample_size-1]:
#                    print('Decline')
#                    deltaL = beta*R
#                    print(deltaL)
#                    L = L + deltaL
#                    if L > Lmax:
#                        L = Lmax
#                        alpha_sens = 1.1*alpha_sens
#                elif average_torque == max_torque[sample_size-1]:
#                    L = L
                 slope, intercept, r_value, p_value, std_err = stats.linregress(index,max_torque)
                 print(r_value)
                 if r_value > 0:
                     print('Improvement')
                     deltaL = beta*r_value
                     print(deltaL)
                     L = L - deltaL
                     if L < Lmin:
                         L = Lmin
                         alpha_sens = 0.9*alpha_sens
                 elif r_value < 0:
                     print('Decline')
                     deltaL = beta*r_value
                     print(deltaL)
                     L = L - deltaL
                     if L > Lmax:
                         L = Lmax
                         alpha_sens = 1.1*alpha_sens
                 gait_cycle = 0                      #   Reset gait_cycle
                 print(gait_cycle+1)
                 index = [0]*sample_size
                 index[gait_cycle] = gait_cycle + 1
                 max_torque = [0]*sample_size        #   Reset max_torque
        #   Update y position of ball & start line and power bar height
        if action == "Plantar":
            y1 = L + alpha_sens*prev_value
            y1actual = L + alpha_sens*read_value
            if y1 > ymax:
                y1 = ymax
            if y1actual > ymax:
                y1actual = ymax
            if y1+50 < 335: score = 0
            if y1+50 > 335 and y1+50 < 413: score = 2
            if y1+50 > 413 and y1+50 < 490: score = 5
            if y1+50 > 490: score = 10
            barh = 400*(y1actual-L)/(ymax-L)
        else:
            y1 = L - alpha_sens*prev_value
            y1actual = L - alpha_sens*read_value
            if y1 < ymin:
                y1 = ymin
            if y1actual < ymin:
                y1actual = ymin
            if y1 > 266: score = 0
            if y1 < 266 and y1 > 190: score = 2
            if y1 < 190 and y1 > 106: score = 5
            if y1 < 106: score = 10
            barh = 400*(y1actual-L)/(ymin-L)
        liney = L
        display.game(screen,liney,y1,action,barh,total_score)
        if score == 10:
            display.goal(screen)
        if score_display < score_display_max and flag == False:
            display.Score(screen,score)
        count += 1
        pygame.display.update()						#	Updates the display screen only in the places where the event has changed
#        clock.tick()								#	Max framerate of the game
    
    pygame.quit()										#	Unitialize all pygame modules (pygame destructor)
    quit()												#	Quit Python
        
game_intro()