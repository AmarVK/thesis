#	ENSE 799 - Master's thesis
#	Amar Vamsi Krishna - UID : 114921871
#	University of Maryland, College Park
#	Date : 13th November, 2017
#	Advisor : Dr. Anindo Roy
#	Topic : Development of a novel interactive visual task for robot assisted gait training in stroke
#	Task 2.1: Programming - Create a Video game - create a screen cursor and visual environment
#	Version-1 : Creating a window using pygame and displaying the events (Keyboard presses and mouse movements) on the terminal window
#	Configuration and Dependancies - Uses python version2.7.12 and pygame version 1.9.3. Currently using Spyder IDE and Sublime Text editor for development
#	Source for the tutorial : https://pythonprogramming.net/pygame-python-3-part-1-intro/

import pygame
import xlrd

import display
import analysis
import update

pygame.init()										#	Initialize all imported pygame - modules (pygame constructor) 

screen = pygame.display.set_mode((800,600))             #	 Initialize a window or screen for display
pygame.display.set_caption('Game On!')      				#   Set the current window caption
clock = pygame.time.Clock()						           	#	Create an object - 'clock' to help track time

def game_intro():
    intro = True
    
    while intro:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        action = display.intro(screen)
        if action != "None":
            game_loop(action)
        pygame.display.update()
        clock.tick(200)
        
def game_loop(action):
    if action == "Dorsi":
                
        L = 300                 #   Initial Start position
        ymin = 67               #   Min y position of ball
        ymax = 488
        flag = False             #   Used to detect change in gait_cycle
                
    elif action == "Plantar":
       
        L = 250                 #   Initial Start position
        ymax = 488              #   Max y position of ball
        ymin = 67               #   Min y position of ball
        flag = True             #   Used to detect change in gait_cycle
        
        
    footswitch = []
    torque = []
    
    avg = 0
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
    score_display_max = 70
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
        count += 1
        
        if torque[count] < 0:
            torque[count] = 0.00
        else:
            torque[count] = torque[count]

        if footswitch[count] > 0.3:
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
                 alpha_sens,L = analysis.ml(action,avg,max_torque,sample_size,beta,L,alpha_sens,index)
                 gait_cycle = 0                      #   Reset gait_cycle
                 print(gait_cycle+1)
                 index = [0]*sample_size
                 index[gait_cycle] = gait_cycle + 1
                 max_torque = [0]*sample_size        #   Reset max_torque
        #   Update y position of ball & start line and power bar height
        y1,y1actual,barh = update.y(action,y1,L,alpha_sens,prev_value,read_value,ymin,ymax)
        score = update.score(action,y1,score)
        liney = L
        action1 = display.game(screen,liney,y1,action,barh,total_score)
        if action1 == "Menu":
            game_intro()
        if score == 10:
            display.goal(screen)
        if score_display < score_display_max and flag == False:
            display.Score(screen,score)
        count += 1
        pygame.display.update()						#	Updates the display screen only in the places where the event has changed
#        clock.tick()								#	Max framerate of the game
    
    pygame.quit()										#	Unitialize all pygame modules (pygame destructor)
    quit()												#	Quit Python

print(raw_input())
print(raw_input())
print(raw_input())
print(raw_input())
print(raw_input())
print(raw_input())
print(raw_input())
action = "Dorsi"        
game_loop(action)