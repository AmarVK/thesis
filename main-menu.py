# =============================================================================
# Import Modules
# =============================================================================
from Tkinter import *
import ttk
import numpy as np
import os
# =============================================================================
# import amarthesis as at
# =============================================================================
# =============================================================================
# Importing pygame
# =============================================================================
import pygame
import xlrd
from scipy import stats
# =============================================================================

# Deffine Fonts
# =============================================================================
HEADER_FONT = ("Verdana",12)
FONT = ("Verdana",10)
# Initialize window
# =============================================================================
window = Tk()                                           #   Creating a Tkinter object
window.title("Penalty Shooter")                         #   Creating a title
window.geometry("600x470+0+0")                          #   Creating a screen x -> the dimensions and +gives the initial position location 
# window.wm_iconbitmap('ball.xbm')                      #   TODO Fix this

global alpha
global tau
global beta
global n
global avg
alpha = 0
tau = 0
beta = 0
n = 3
avg =-1

def gameAction():
    global alpha
    global tau
    global beta
    global n
    if len(input1entry.get()) == 0:
        alpha = 25
    else:
        alpha = float(input1entry.get())
        
    if len(input2entry.get()) == 0:
        tau = 0.75
    else:
        tau = float(input2entry.get())
        
    if len(input3entry1.get()) == 0:
        beta = 50
    else:
        beta = float(input3entry1.get())
    
    if len(input3entry2.get()) == 0:
        n = 5
    else:
        n = int(input3entry2.get())
        
     
    game_loop()

def mlParams1():        
    global avg
    input3Text1 = Label(window,text = input3, font = FONT).grid(row=8, column =0, sticky=W)
    input3entry1.grid(row=9, column =0, sticky=W)
    
    input3Text2 = Label(window,text = input5, font = FONT).grid(row=8, column =1, sticky=W)
    input3entry2.grid(row=9, column =1, sticky=W)
 
    avg =1
    return avg
    
def mlParams2():
    global avg        
    input3Text1 = Label(window,text = input3, font = FONT).grid(row=8, column =0, sticky=W)
    input3entry1.grid(row=9, column =0, sticky=W)
    
    input3Text2 = Label(window,text = input5, font = FONT).grid(row=8, column =1, sticky=W)
    input3entry2.grid(row=9, column =1, sticky=W)
    avg =0
    return avg


def game_loop():
    
    L = 250                 #   Initial Start position
    Lmax = 400              #   Max start position
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
                if avg == 1:
                    #   Compare last sample with the average of the rest and decide improvement and declining
                    average_torque = sum(max_torque[:sample_size-1])/(sample_size-1)
                    R = (max_torque[sample_size-1]/average_torque)
                    if average_torque < max_torque[sample_size-1]:
                        print('Improvement')
                        deltaL = beta*R
                        print(deltaL)
                        L = L - deltaL
                        if L < Lmin:
                            L = Lmin
                            alpha_sens = 0.9*alpha_sens
                    elif average_torque > max_torque[sample_size-1]:
                        print('Decline')
                        deltaL = beta*R
                        print(deltaL)
                        L = L + deltaL
                        if L > Lmax:
                            L = Lmax
                            alpha_sens = 1.1*alpha_sens
                    elif average_torque == max_torque[sample_size-1]:
                        L = L
                elif avg == 0:
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
        liney = L
        screen.fill(screencolor)
        display_rudiments(liney,y1)     						
        bar(barh)
        kickpower(total_score)
        if score == 10:
            goaltext = pygame.font.Font('./fonts/font.ttf',50)
            GoalSurf, GoalRect = text_objects("GOAL!", goaltext, white)
            GoalRect.center = ((800/2),575)
            screen.blit(GoalSurf, GoalRect)
        if score_display < score_display_max and flag == False:
            scoretext = pygame.font.Font('./fonts/font.ttf',70)
            scoreSurf, scoreRect = text_objects("Score:" +str(score), scoretext, white)
            scoreRect.center = ((800/2),200)
            screen.blit(scoreSurf, scoreRect)
        button("Main Menu",675,560,100,30,red,bright_red,"Menu")
        count += 1
        pygame.display.update()						#	Updates the display screen only in the places where the event has changed
        clock.tick()								#	Max framerate of the game
    
    pygame.quit()										#	Unitialize all pygame modules (pygame destructor)
    quit()	
        
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def display_rudiments(liney,y1):
    #   Football field image
    fieldimg = pygame.image.load('./images/field.png')               #   load image from data folder
    fieldimg = pygame.transform.scale(fieldimg, (716, 500))        #   scale image by pixels
    #Ball image
    ballimg = pygame.image.load('./images/ball.png')
    ballimg = pygame.transform.scale(ballimg, (50, 50))
    # Goal image
    goalimg = pygame.image.load('./images/goal.png')
    
    x =  42                 #   Field x position
    y = 50                  #   Field y position
    linex = x               #   Start-line x position (same as field)
    x1 = 376                #   Initial Ball x position (center of the field)
    x2 =  300               #   Net x position
    y2 =  490               #   Net y position
    linew = 716             #   Start line width
    lineh = 5               #   Start line height
    screen.blit(fieldimg, (x,y))
    startline(linex, liney+25, linew, lineh)
    screen.blit(ballimg, (x1,y1))
    screen.blit(goalimg, (x2,y2))
    
#   Defining bar as an object with multiple inputs
def bar(barh):
    barx = 8                #   Power bar x position   
    barw = 20               #   Power bar width in pixels
    bary = 8                #   Power bar y position
    pygame.draw.rect(screen, white, [barx-2, bary-2, barw+4, 404])
    pygame.draw.rect(screen, black, [barx, bary, barw, 400])
    pygame.draw.rect(screen, white, [barx, bary, barw, barh])
    
#   Defining start-line as an object with multiple inputs
def startline(linex, liney, linew, lineh):
    pygame.draw.rect(screen, red, [linex, liney, linew, lineh])

#   Defining kickpower as an object with power input to display the kick power on the top right corner of the window
def kickpower(total_score):
    font = pygame.font.Font('./fonts/font.ttf', 40)
    kickmeter = font.render('Kickmeter',1,white)
    text = font.render("Total Score: "+str(total_score), True, white)
    screen.blit(text,(600,10))
    screen.blit(kickmeter,(30,10))

# =============================================================================
# Define text and photo inputs
# =============================================================================
logo1 = PhotoImage(file='./images/fire-soccer.gif')
header_text = """Penalty Shooter Game !
Robot Assisted Soccer Game"""
input1 = """Sensitivity (pixels/Nm)"""
input2 = """Threshold (Nm)"""
input3 = """Pixel increment"""
input4 = """Machine Learning"""
input5 = """Number of Cycles"""
input6 = """Game Mode"""
checkbox1 = """None"""
checkbox2 = """Average"""
checkbox3 = """Regression"""
game_button = """Go to Game !"""
blanker = """-------------------------------------------------------------------------------------------"""
team = """Team :"""
team_members="""Amar Vamsi Krishna
Suchitra Chandar
Rahul Subramonian"""
advisor = """Advisor:"""
advisor_name = """Dr. Anindo Roy"""
footer_image = PhotoImage(file='./images/umd.gif')
# =============================================================================
# Setting up the grid UI
# =============================================================================
introText = Label(window,text = header_text, justify = LEFT, font = HEADER_FONT).grid(row=0, column =0, sticky=W)
topLogo = Label(window, image = logo1).grid(row =0, column = 1, sticky = W+E+N+S)
input1Text = Label(window,text = input1, font = FONT).grid(row=2, column =0, sticky=W)
input1entry = ttk.Entry(window)
input1entry.grid(row=2, column =1, sticky=W)


input2Text = Label(window,text = input2, font = FONT).grid(row=3, column =0, sticky=W)
input2entry = ttk.Entry(window)
input2entry.grid(row=3, column =1, sticky=W)

# =============================================================================
# input3Text = Label(window,text = input3, font = FONT).grid(row=4, column =0, sticky=W)
# input3entry = ttk.Entry(window)
# input3entry.grid(row=4, column =1, sticky=W)
# =============================================================================
btn2 = StringVar()
input5Text = Label(window,text = input6, font = FONT).grid(row=5, column =0, sticky=W)
#input5entry = ttk.Radiobutton(window, text=checkbox4, variable = btn2 , value =1).grid(row=5, column =1, sticky =W)
#input5entry1 = ttk.Radiobutton(window, text=checkbox5, variable = btn2 , value =2).grid(row=6, column =1, sticky =W)

btn = StringVar()
input4Text = Label(window,text = input4, font = FONT).grid(row=7, column =0, sticky=W)
input4entry1 = ttk.Radiobutton(window, text=checkbox1, variable = btn , value =1).grid(row=7, column =1, sticky =W)


input4entry2 = ttk.Radiobutton(window, text=checkbox2, variable = btn, value =2,command =lambda: mlParams1()).grid(row=8, column =1, sticky =W)


input4entry3 = ttk.Radiobutton(window, text=checkbox3, variable = btn, value =3,command =lambda: mlParams2()).grid(row=9, column =1, sticky =W)
gameButton = Button(window, text = game_button, command =lambda: gameAction()).grid (row = 10,column = 0, columnspan =2)
# =============================================================================
# Setting up the footer UI
# =============================================================================
divider = Label(window,text = blanker, font = FONT).grid(row=11, column = 0, columnspan =2, sticky = N+E+W+S)
teamText = Label(window,text = team, font = FONT).grid(row=12, column = 0, columnspan =2, sticky = N+E+W+S)
teamMembers = Label(window,text = team_members, font = FONT).grid(row=13, column = 0, columnspan =2, sticky = N+E+W+S)
divider = Label(window,text = blanker, font = FONT).grid(row=14, column = 0, columnspan =2, sticky = N+E+W+S)
advisorText = Label(window,text = advisor, font = FONT).grid(row=15, column = 0, columnspan =2, sticky = N+E+W+S)
advisorName = Label(window,text = advisor_name, font = FONT).grid(row=16, column = 0, columnspan =2, sticky = N+E+W+S)
bottomLogo = Label(window, image = footer_image).grid(row =17, column = 0, columnspan = 2, sticky = W+E+N+S)
divider = Label(window,text = blanker, font = FONT).grid(row=18, column = 0, columnspan =2, sticky = N+E+W+S)
input3entry1 = ttk.Entry(window)
input3entry2 = ttk.Entry(window)

# =============================================================================
# Pygame inits
# =============================================================================
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
fieldimg = pygame.image.load('./images/field.png')               #   load image from data folder
fieldimg = pygame.transform.scale(fieldimg, (716, 500))        #   scale image by pixels
startlineimg = pygame.image.load('./images/startline.png')
startlineimg = pygame.transform.scale(startlineimg,(716,76))
#Ball image
ballimg = pygame.image.load('./images/ball.png')
ballimg = pygame.transform.scale(ballimg, (50, 50))
# Goal image
goalimg = pygame.image.load('./images/goal.png')


# =============================================================================
# =============================================================================
# # End of UI
# =============================================================================
# =============================================================================

window.mainloop()                                       #   The window won't appear until we enter the Tkinter event loop: Our script will remain in the event loop until we close the window



