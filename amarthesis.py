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
from scipy import stats

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


def display_rudiments(liney,y1,action):
    #   Football field image
    fieldimg = pygame.image.load('./data/field.png')               #   load image from data folder
    fieldimg = pygame.transform.scale(fieldimg, (716, 500))        #   scale image by pixels
    #Ball image
    ballimg = pygame.image.load('./data/ball.png')
    ballimg = pygame.transform.scale(ballimg, (50, 50))
    # Goal image
    goalimg = pygame.image.load('./data/goal.png')
    
    x =  42                 #   Field x position
    y = 50                  #   Field y position
    linex = x               #   Start-line x position (same as field)
    x1 = 376                #   Initial Ball x position (center of the field)
    
    if action == "Dorsi":
        x2 =  300               #   Net x position
        y2 =  59                #   Net y position
        fieldimg = pygame.transform.flip(fieldimg, False, True)            #   Flip field image
        goalimg = pygame.transform.flip(goalimg, False, True)            #   Flip field image
        screen.blit(fieldimg, (x,y))
        linew = 716
        lineh = 5
        startline(linex, liney+25, linew, lineh)
        screen.blit(ballimg, (x1,y1))
        screen.blit(goalimg, (x2,y2))
    else:
        x2 =  300               #   Net x position
        y2 =  490               #   Net y position
        screen.blit(fieldimg, (x,y))
        linew = 716
        lineh = 5
        startline(linex, liney+25, linew, lineh)
        screen.blit(ballimg, (x1,y1))
        screen.blit(goalimg, (x2,y2))

#   Defining bar as an object with multiple inputs
def bar(barh,action):
    barx = 8                #   Power bar x position   
    barw = 20               #   Power bar width in pixels
    if action == "Plantar":
        bary = 8                #   Power bar y position
        pygame.draw.rect(screen, white, [barx-2, bary-2, barw+4, 404])
        pygame.draw.rect(screen, black, [barx, bary, barw, 400])
        pygame.draw.rect(screen, white, [barx, bary, barw, barh])
    else:
        bary = 409 - barh
        pygame.draw.rect(screen, white, [barx-2, 6, barw+4, 404])
        pygame.draw.rect(screen, black, [barx, 8, barw, 400])
        pygame.draw.rect(screen, white, [barx, bary, barw, barh])
    
#   Defining start-line as an object with multiple inputs
def startline(linex, liney, linew, lineh):
    pygame.draw.rect(screen, red, [linex, liney, linew, lineh])

#   Defining kickpower as an object with power input to display the kick power on the top right corner of the window
def kickpower(score):
    font = pygame.font.Font('./data/font.ttf', 40)
    kickmeter = font.render('Kickmeter',1,white)
    text = font.render("Score: "+str(score), True, white)
    screen.blit(text,(680,10))
    screen.blit(kickmeter,(30,10))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != "None":
            if action == "Dorsi":
                game_loop(action)
            elif action == "Plantar":
                game_loop(action)
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font('./data/font.ttf',20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
    
def game_intro():

    largeText = pygame.font.Font('./data/font.ttf',115)
    TextSurf, TextRect = text_objects("Game On!", largeText, black)
    TextRect.center = ((800/2),200)
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
        screen.blit(TextSurf, TextRect)

        button("Dorsiflexion",150,450,100,50,green,bright_green,"Dorsi")
        button("Plantarflexion",550,450,100,50,red,bright_red,"Plantar")    

        pygame.display.update()
        clock.tick(15)
        
#	The game loop logic runs as long as there is no crash
def game_loop(action):
    if action == "Dorsi":
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
            if torque[i] < 0:
                torque[i] = 0.00
            else:
                torque[i] = torque[i]
        for i in range(0,tlength):
            if footswitch[i] > 0.3:
                torque[i] = 0
                footswitch[i] = 0
            else:
                footswitch[i] = 1
                
        L = 300                 #   Initial Start position
        Lmax = 550              #   Max start positiom
        Lmin = 100              #   Min start position position
        ymin = 67               #   Min y position of ball
        ymax = 488
                
    elif action == "Plantar":
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
        
        L = 250                 #   Initial Start position
        Lmax = 400              #   Max start positiom
        Lmin = 50               #   Min start position position
        ymax = 488              #   Max y position of ball
        
        
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
    flag = True             #   Used to detect change in gait_cycle
    crashed = False         #	Initialize the boolean - 'crashed' to false
    while not crashed:									#	The game loop begins
            
        for event in pygame.event.get():				#	Gets all the events from the game
            if event.type == pygame.QUIT:			#	If the event is 'pygame.QUIT' - pressing of the 'X' button on the display window, the boolean crashed is flagged to a true value
                crashed = True	
                pygame.quit()
                quit()
                
            if count == tlength-1:
                crashed = True
                pygame.quit()
                quit()  
            print event
        read_value = torque[count]
        count += 1
        index[gait_cycle] = gait_cycle + 1
        if flag == False:           #   Phase not under consideration: no ball movement
            prev_value = 0          #   New gait_cycle detected; set max torque value to zero
            score = 0
            if footswitch[count] != 0:          #   Wait for stance phase 
                flag = True
        elif flag == True:          #   Phase under consideration
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
        screen.fill(screencolor)
        display_rudiments(liney,y1,action)      						
        bar(barh,action)
        kickpower(score)
        if score == 10:
            goaltext = pygame.font.Font('./data/font.ttf',50)
            GoalSurf, GoalRect = text_objects("GOAL!", goaltext, white)
            GoalRect.center = ((800/2),575)
            screen.blit(GoalSurf, GoalRect)
        pygame.display.update()						#	Updates the display screen only in the places where the event has changed
        clock.tick(200)								#	Max framerate of the game
    
    pygame.quit()										#	Unitialize all pygame modules (pygame destructor)
    quit()												#	Quit Python
action = "None"	
game_intro()