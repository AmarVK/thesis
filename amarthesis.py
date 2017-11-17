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

import pygame, eztext
import xlrd
from scipy import stats
import numpy as np	

pygame.init()										#	Initialize all imported pygame - modules (pygame constructor) 

screen = pygame.display.set_mode((800,600))             #	 Initialize a window or screen for display
black = [0, 0, 0]                                       #   Defining Black color for game rudiments
white = [255, 255, 255]                                 #   Defining White color for game rudiments
green = [0, 150, 0]                                     #   Defining Green color for game rudiments
bright_green = [0, 255, 0]                              #   Defining bright Green color for game rudiments
red = [150, 0 ,0]                                       #   Defining Red color for game rudiments
bright_red = [255, 0 ,0]                                #   Defining brigh Red color for game rudiments
screencolor = black                                     #   Defining screen color as black
pygame.display.set_caption('Game On!')      				#   Set the current window caption
clock = pygame.time.Clock()						           	#	Create an object - 'clock' to help track time

#   Football field image
fieldimg = pygame.image.load('./data/field.png')               #   load image from data folder
fieldimg = pygame.transform.scale(fieldimg, (716, 500))        #   scale image by pixels
startlineimg = pygame.image.load('./data/startline.png')
startlineimg = pygame.transform.scale(startlineimg,(716,76))
#Ball image
ballimg = pygame.image.load('./data/ball.png')
ballimg = pygame.transform.scale(ballimg, (50, 50))
# Goal image
goalimg = pygame.image.load('./data/goal.png')

def display_rudiments(x,y,linex,liney,x1,y1,x2,y2):
    screen.blit(fieldimg, (x,y))
    screen.blit(startlineimg, (linex,liney))
    linew = 716
    lineh = 5
    startline(linex, liney, linew, lineh)
    screen.blit(ballimg, (x1,y1))
    screen.blit(goalimg, (x2,y2))

#   Defining bar as an object with multiple inputs
def bar(barx, bary, barw, barh):
    pygame.draw.rect(screen, white, [barx-2, bary-2, barw+4, 404])
    pygame.draw.rect(screen, black, [barx, bary, barw, 400])
    pygame.draw.rect(screen, white, [barx, bary, barw, barh])
    
#   Defining start-line as an object with multiple inputs
def startline(linex, liney, linew, lineh):
    pygame.draw.rect(screen, red, [linex, liney, linew, lineh])

#   Defining kickpower as an object with power input to display the kick power on the top right corner of the window
def kickpower(power):
    font = pygame.font.Font('./data/font.ttf', 40)
    kickmeter = font.render('Kickmeter',1,white)
    text = font.render("Power: "+str(power)+ "%", True, white)
    screen.blit(text,(590,10))
    screen.blit(kickmeter,(30,10))

#   Extracting torque data from the excel file
file_location = "./data/Robot_data1.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_name('Trial 1')
#   Extracting Column 7 from the sheet
torque = sheet.col_values(6)
footswitch = sheet.col_values(19)

#   Extracting meaningful values of torque
tlength = len(torque)
for i in range(0,tlength):
    if torque[i] > 0:
        torque[i] = 0.00
    else:
        torque[i] = (-1)*torque[i]
for i in range(0,tlength):
    if footswitch[i] < 0.3:
        torque[i] = 0
        footswitch[i] = 0


action = "None"	

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != "None":
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font('./data/font.ttf',20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
    
def game_intro():

    largeText = pygame.font.Font('./data/font.ttf',115)
    TextSurf, TextRect = text_objects("Game On!", largeText)
    TextRect.center = ((800/2),100)
    smallText = pygame.font.Font('./data/font.ttf',40)
    txtbx1 = eztext.Input(x=200, y=250, font=smallText, maxlength=5, color=(0,0,0), restricted = '1234567890.', prompt='Start difficulty: ')
    txtbx2 = eztext.Input(x=200, y=300, font=smallText, maxlength=5, color=(0,0,0), restricted = '1234567890.', prompt='Torque sensitivity: ')
    txtbx3 = eztext.Input(x=200, y=350, font=smallText, maxlength=5, color=(0,0,0), restricted = '1234567890.', prompt='Progression: ')
    intro = True

    while intro:
        events = pygame.event.get()
        for event in events:
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(white)
        # update txtbx
        txtbx1.update(events)
        txtbx2.update(events)
        txtbx3.update(events)
        screen.blit(TextSurf, TextRect)
        txtbx1.draw(screen)
        txtbx2.draw(screen)
        txtbx3.draw(screen)

        button("Start",150,450,100,50,green,bright_green,"play")
        button("Exit",550,450,100,50,red,bright_red,"quit")    

        pygame.display.update()
        clock.tick(15)
        
#	The game loop logic runs as long as there is no crash
def game_loop():
    x =  42                 #   Field x position
    y = 50                  #   Field y position
    L = 250                 #   Initial Start position
    Lmax = 400              #   Max start positiom
    Lmin = 50               #   Min start position position
    deltaL = 0               #   actual pixel offset for machine learning
    beta = 50               #   Default pixel offset
    linex = x               #   Start-line x position (same as field)
    liney = L               #   Initial Start-line y position (same as Start position)
    x1 = 376                #   Initial Ball x position (center of the field)
    y1 = L                  #   Initial Ball y position (same as Initial Start position)
    y1actual = 0            #   Initial y value wrt torque profile
    ymax = 488              #   Max y position of ball
    x2 =  300               #   Net x position
    y2 =  490               #   Net y position
    alpha_sens = 41.66      #   Sensitivity from dialog box (pixels/Nm)
    barx = 8                #   Power bar x position   
    bary = 8                #   Power bar y position
    barw = 20               #   Power bar width in pixels   
    barh = 2                #   Power bar height in pixels
    power = 0.00            #   Percentage of human torque wrt total torque
    count = 0               #   Used for indexing data from .xlsx file
    read_value = 0          #   Initializing current torque value
    prev_value = 0          #   Initializing max torque value in the current gait cycle
    gait_cycle = 0          #   Initializing gait_cycle count
    print(gait_cycle+1)
    sample_size = 5         #   Setting the window size for machine learning
    max_torque = [0]*sample_size            #   Initializing an empty list of length= sample_size to store max torque values of every iteration
    index = [0]*sample_size 
    flag = True             #   Used to detect change in gait_cycle
    average_torque = 0      # Initializing average torque value for machine learning
    crashed = False         #	Initialize the boolean - 'crashed' to false
    while not crashed:									#	The game loop begins
            
        for event in pygame.event.get():				#	Gets all the events from the game
            if event.type == pygame.QUIT:			#	If the event is 'pygame.QUIT' - pressing of the 'X' button on the display window, the boolean crashed is flagged to a true value
                crashed = True	
                pygame.quit()
                quit()
                
            if count == tlength:
                crashed = True
                pygame.quit()
                quit()
                
        read_value = torque[count]
        count += 1
        index[gait_cycle] = gait_cycle + 1
        if flag == False:           #   Swing phase: no ball movement
            prev_value = 0          #   New gait_cycle detected; set max torque value to zero
            if footswitch[count] != 0:          #   Wait for stance phase 
                flag = True
        elif flag == True:          #   Stance phase
            if read_value>prev_value:
                prev_value = read_value
            if footswitch[count] == 0:          #   New gait cycle detected
                flag = False
                gait_cycle += 1
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
#                elif average_torque > max_torque[sample_size-1]:
#                    print('Decline')
#                    deltaL = beta*R
#                    print(deltaL)
#                    L = L + deltaL
#                    if L > Lmax:
#                        L = Lmax
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
                 elif r_value < 0:
                     print('Decline')
                     deltaL = beta*r_value
                     print(deltaL)
                     L = L - deltaL
                     if L > Lmax:
                         L = Lmax
                 gait_cycle = 0                      #   Reset gait_cycle
                 print(gait_cycle+1)
                 index = [0]*sample_size
                 index[gait_cycle] = gait_cycle + 1
                 max_torque = [0]*sample_size        #   Reset max_torque
        #   Update y position of ball & start line and power bar height
        y1 = L + alpha_sens*prev_value
        y1actual = L + alpha_sens*read_value
        if y1 > ymax:
            y1 = ymax
        if y1actual > ymax:
            y1actual = ymax
        liney = L
        barh = 400*(y1actual-L)/(ymax-L)
        power = 100*(y1actual-L)/(ymax-L)
        screen.fill(screencolor)
        display_rudiments(x,y,linex,liney,x1,y1,x2,y2)      						
        bar(barx, bary, barw, barh)
        kickpower(power)
        pygame.display.update()						#	Updates the display screen only in the places where the event has changed
        clock.tick(200)								#	Max framerate of the game
    
    pygame.quit()										#	Unitialize all pygame modules (pygame destructor)
    quit()												#	Quit Python
game_intro()