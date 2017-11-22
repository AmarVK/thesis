# =============================================================================
# Import Modules
# =============================================================================
from Tkinter import *
import ttk
import numpy as np
import os

# =============================================================================
# Importing pygame
# =============================================================================
import pygame, eztext
import xlrd
# =============================================================================

# Deffine Fonts
# =============================================================================
HEADER_FONT = ("Verdana",12)
FONT = ("Verdana",10)
# Initialize window
# =============================================================================
window = Tk()                                           #   Creating a Tkinter object
window.title("Penalty Shooter")                         #   Creating a title
window.geometry("500x470+0+0")                          #   Creating a screen x -> the dimensions and +gives the initial position location 
# window.wm_iconbitmap('ball.xbm')                      #   TODO Fix this


# =============================================================================
# Extracting torque from excel
# =============================================================================
file_location = "/home/amarvk/projects/thesis/data/Robot_Data1.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_name('Trial 1')
#   Extracting Column 7 from the sheet
torque = sheet.col_values(6)
footswitch = sheet.col_values(19)

# =============================================================================
# Extracting meaningful torque inputs
# =============================================================================
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

alpha = 0
tau = 0
beta = 0
n = 0

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
        tau = float(input3entry1.get())
    
    if len(input3entry2.get()) == 0:
        n = 5
    else:
        n = float(input3entry2.get())
        
    
    game_loop()

def mlParams():        
    input3Text1 = Label(window,text = input3, font = FONT).grid(row=8, column =0, sticky=W)
    input3entry1.grid(row=9, column =0, sticky=W)
    
    input3Text2 = Label(window,text = input5, font = FONT).grid(row=8, column =1, sticky=W)
    input3entry2.grid(row=9, column =1, sticky=W)

def game_loop():
    x =  42                 #   Field x position
    y = 50                  #   Field y position
    L = 250                 #   Initial Start position
    Lmax = 250              #   Max start positiom
    Lmin = 50               #   Min start position position
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
    sample_size = n         #   Setting the window size for machine learning
    print sample_size
    max_torque = [0]*sample_size            #   Initializing an empty list of length= sample_size to store max torque values of every iteration
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
            else:
                #   Compare last sample with the average of the rest and decide improvement and declining
                average_torque = sum(max_torque[:sample_size-1])/(sample_size-1)
                if average_torque < max_torque[sample_size-1]:
                    print('Improvement')
                    L = L - 50
                    if L < Lmin:
                        L = Lmin
                elif average_torque > max_torque[sample_size-1]:
                    print('Decline')
                    L = L + 50
                    if L > Lmax:
                        L = Lmax
                elif average_torque == max_torque[sample_size-1]:
                    L = L
                gait_cycle = 0                      #   Reset gait_cycle
                print(gait_cycle+1)
                max_torque = [0]*sample_size        #   Reset max_torque
        #   Update y position of ball & start line and power bar height
        y1 = L + alpha*prev_value
        y1actual = L + alpha*read_value
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
    quit()	
        
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

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


# =============================================================================
# Define text and photo inputs
# =============================================================================
logo = PhotoImage(file='/home/amarvk/projects/thesis/images/fire-soccer.gif')
header_text = """Penalty Shooter Game !
Robot Assisted Soccer Game"""
input1 = """Sensitivity (pixels/Nm)"""
input2 = """Threshold (Nm)"""
input3 = """Default Pixel Offset"""
input4 = """Machine Learning"""
input5 = """Window Size"""
checkbox1 = """None"""
checkbox2 = """Average"""
checkbox3 = """Regression"""
game_button = """Go to Game !"""
blanker = """-------------------------------------------------------------------------------------------"""
team = """Team :"""
team_members="""Amar Vamsi Krishna
Suchitra Chander
Rahul Subramonian"""
advisor = """Advisor:"""
advisor_name = """Dr. Anindo Roy"""
footer_image = PhotoImage(file='/home/amarvk/projects/thesis/images/umd.gif')
# =============================================================================
# Setting up the grid UI
# =============================================================================
introText = Label(window,text = header_text, justify = LEFT, font = HEADER_FONT).grid(row=0, column =0, sticky=W)
topLogo = Label(window, image = logo).grid(row =0, column = 1, sticky = W+E+N+S)
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

btn = StringVar()
input4Text = Label(window,text = input4, font = FONT).grid(row=5, column =0, sticky=W)
input4entry1 = ttk.Radiobutton(window, text=checkbox1, variable = btn , value =1).grid(row=5, column =1, sticky =W)


input4entry2 = ttk.Radiobutton(window, text=checkbox2, variable = btn, value =2,command =lambda: mlParams()).grid(row=6, column =1, sticky =W)


input4entry3 = ttk.Radiobutton(window, text=checkbox3, variable = btn, value =3,command =lambda: mlParams()).grid(row=7, column =1, sticky =W)
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
fieldimg = pygame.image.load('./data/field.png')               #   load image from data folder
fieldimg = pygame.transform.scale(fieldimg, (716, 500))        #   scale image by pixels
startlineimg = pygame.image.load('./data/startline.png')
startlineimg = pygame.transform.scale(startlineimg,(716,76))
#Ball image
ballimg = pygame.image.load('./data/ball.png')
ballimg = pygame.transform.scale(ballimg, (50, 50))
# Goal image
goalimg = pygame.image.load('./data/goal.png')



action = "None"	
# =============================================================================
# =============================================================================
# # End of UI
# =============================================================================
# =============================================================================

window.mainloop()                                       #   The window won't appear until we enter the Tkinter event loop: Our script will remain in the event loop until we close the window



