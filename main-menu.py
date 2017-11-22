# =============================================================================
# Import Modules
# =============================================================================
from Tkinter import *
import ttk
import numpy as np
import os
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
# =============================================================================
# # End of UI
# =============================================================================
# =============================================================================

window.mainloop()                                       #   The window won't appear until we enter the Tkinter event loop: Our script will remain in the event loop until we close the window



def gameAction():
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

def mlParams():        
    input3Text1 = Label(window,text = input3, font = FONT).grid(row=8, column =0, sticky=W)
    input3entry1.grid(row=9, column =0, sticky=W)
    
    input3Text2 = Label(window,text = input5, font = FONT).grid(row=8, column =1, sticky=W)
    input3entry2.grid(row=9, column =1, sticky=W)

        
