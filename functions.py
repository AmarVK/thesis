# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 11:27:54 2018

@author: Suchitra Chandar
"""

def display(liney,y1,action):
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
    
    if action == "Dorsi":
        x2 =  300               #   Net x position
        y2 =  59                #   Net y position
        linew = 716             #   Start line width
        lineh = 5               #   Start line height
        fieldimg = pygame.transform.flip(fieldimg, False, True)          #   Flip field image
        goalimg = pygame.transform.flip(goalimg, False, True)            #   Flip field image
        screen.blit(fieldimg, (x,y))
        startline(linex, liney+25, linew, lineh)
        screen.blit(ballimg, (x1,y1))
        screen.blit(goalimg, (x2,y2))
    else:
        x2 =  300               #   Net x position
        y2 =  490               #   Net y position
        linew = 716             #   Start line width
        lineh = 5               #   Start line height
        screen.blit(fieldimg, (x,y))
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
def kickpower(total_score):
    font = pygame.font.Font('./fonts/font.ttf', 40)
    kickmeter = font.render('Kickmeter',1,white)
    text = font.render("Total Score: "+str(total_score), True, white)
    screen.blit(text,(600,10))
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
            elif action == "Menu":
                game_intro()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font('./fonts/font.ttf',20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)