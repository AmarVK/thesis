#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 13:59:27 2017

@author: amarvk
"""
# =============================================================================
# Import Modules
# =============================================================================
from Tkinter import *
import numpy as np
import os
# =============================================================================
# Deffine Fonts
# =============================================================================
HEADER_FONT = ("Verdana",12)
FONT = ("Verdana",10)
# Initialize window
# =============================================================================
window = Tk()                                        #   Creating a Tkinter object
window.title("Penalty Shooter")                         #   Creating a title
window.geometry("500x420+0+0")                          #   Creating a screen x -> the dimensions and +gives the initial position location 
# window.wm_iconbitmap('ball.xbm')                      #   TODO Fix this
# =============================================================================
# Define text and photo inputs
# =============================================================================
logo = PhotoImage(file='/home/amarvk/projects/thesis/images/fire-soccer.gif')
header_text = """Penalty Shooter Game !
Robot Assisted Soccer Game"""
menu_heading = """ Please enter the game parameters"""
input1 = """Sensitivity (pixels/Nm)"""
input2 = """Threshold (Nm)"""
input3 = """Default Pixel Offset"""
input4 = """Machine Learning"""
checkbox1 = """None"""
checkbox2 = """Average"""
# =============================================================================
# checkbox3 = """Maximum"""
# =============================================================================
checkbox4 = """Regression"""
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
# =============================================================================
# menuHeading = Label(window,text = menu_heading, font = FONT).grid(row=1, sticky=W+E+N+S)
# =============================================================================

input1Text = Label(window,text = input1, font = FONT).grid(row=2, column =0, sticky=W)
input1entry = Entry(window)
input1entry.grid(row=2, column =1, sticky=W)


input2Text = Label(window,text = input2, font = FONT).grid(row=3, column =0, sticky=W)
input2entry = Entry(window)
input2entry.grid(row=3, column =1, sticky=W)

input3Text = Label(window,text = input3, font = FONT).grid(row=4, column =0, sticky=W)
input3entry = Entry(window)
input3entry.grid(row=4, column =1, sticky=W)

cb_val1 = IntVar()
cb_val1.set(0)
input3Text = Label(window,text = input4, font = FONT).grid(row=5, column =0, sticky=W)
input3entry1 = Checkbutton(window, text=checkbox1, variable = cb_val1, onvalue =1, offvalue =0).grid(row=5, column =1, sticky =W)

cb_val2 = IntVar()
cb_val2.set(0)
input3entry2 = Checkbutton(window, text=checkbox2, variable = cb_val2, onvalue =1, offvalue =0).grid(row=6, column =1, sticky =W)
# =============================================================================
# 
# cb_val3 = IntVar()
# cb_val3.set(0)
# input3entry3 = Checkbutton(window, text=checkbox3, variable = cb_val3, onvalue =1, offvalue =0).grid(row=6, column =1, sticky =W)
# =============================================================================

cb_val4 = IntVar()
cb_val4.set(0)
input3entry4 = Checkbutton(window, text=checkbox4, variable = cb_val4, onvalue =1, offvalue =0).grid(row=7, column =1, sticky =W)

def gameAction():
    alpha = float(input1entry.get())
    tau = float(input2entry.get())
# =============================================================================
#     print cb_val1.get(), cb_val2.get(), cb_val3.get(), cb_val4.get()
# =============================================================================
    os.system('python amarthesis.py')
    
gameButton = Button(window, text = game_button, command =lambda: gameAction()).grid (row = 8,column = 0, columnspan =2)
# =============================================================================
# Setting up the footer UI
# =============================================================================
divider = Label(window,text = blanker, font = FONT).grid(row=9, column = 0, columnspan =2, sticky = N+E+W+S)
teamText = Label(window,text = team, font = FONT).grid(row=10, column = 0, columnspan =2, sticky = N+E+W+S)
teamMembers = Label(window,text = team_members, font = FONT).grid(row=11, column = 0, columnspan =2, sticky = N+E+W+S)
divider = Label(window,text = blanker, font = FONT).grid(row=12, column = 0, columnspan =2, sticky = N+E+W+S)
advisorText = Label(window,text = advisor, font = FONT).grid(row=13, column = 0, columnspan =2, sticky = N+E+W+S)
advisorName = Label(window,text = advisor_name, font = FONT).grid(row=14, column = 0, columnspan =2, sticky = N+E+W+S)
bottomLogo = Label(window, image = footer_image).grid(row =15, column = 0, columnspan = 2, sticky = W+E+N+S)
divider = Label(window,text = blanker, font = FONT).grid(row=16, column = 0, columnspan =2, sticky = N+E+W+S)


window.mainloop()                                       #   The window won't appear until we enter the Tkinter event loop: Our script will remain in the event loop until we close the window

s = input1entry.get()
print s
