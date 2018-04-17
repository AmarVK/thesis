#! /usr/bin/env python2

from Tkinter import *
import ttk
import numpy as np
import os

window = Tk()                                           #   Creating a Tkinter object
window.title("Penalty Shooter")                         #   Creating a title
window.geometry("600x470+0+0")  

HEADER_FONT = ("Verdana",12)
FONT = ("Verdana",10)

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

bg_image = PhotoImage(file='./images/umd.gif')
bg_label = Label(window, image = bg_image)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

introText = Label(window,text = header_text, justify = LEFT, font = HEADER_FONT).grid(row=0, column =0, sticky=W)
topLogo = Label(window, image = logo1).grid(row =0, column = 1, sticky = W+E+N+S)
input1Text = Label(window,text = input1, font = FONT).grid(row=2, column =0, sticky=W)
input1entry = ttk.Entry(window)
input1entry.grid(row=2, column =1, sticky=W)


input2Text = Label(window,text = input2, font = FONT).grid(row=3, column =0, sticky=W)
input2entry = ttk.Entry(window)
input2entry.grid(row=3, column =1, sticky=W)

btn2 = StringVar()
input5Text = Label(window,text = input6, font = FONT).grid(row=5, column =0, sticky=W)

btn = StringVar()
input4Text = Label(window,text = input4, font = FONT).grid(row=7, column =0, sticky=W)
input4entry1 = ttk.Radiobutton(window, text=checkbox1, variable = btn , value =1).grid(row=7, column =1, sticky =W)


input4entry2 = ttk.Radiobutton(window, text=checkbox2, variable = btn, value =2,command =lambda: mlParams1()).grid(row=8, column =1, sticky =W)


input4entry3 = ttk.Radiobutton(window, text=checkbox3, variable = btn, value =3,command =lambda: mlParams2()).grid(row=9, column =1, sticky =W)
gameButton = Button(window, text = game_button, command =lambda: gameAction()).grid (row = 10,column = 0, columnspan =2)

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

window.mainloop()                                       #   The window won't appear until we enter the Tkinter event loop: Our script will remain in the event loop until we close the window
