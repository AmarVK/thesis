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
import tkFont
# =============================================================================
# Deffine Fonts
# =============================================================================
HEADER_FONT = ("Verdana",12)
FONT = ("Verdana",10)
# =============================================================================
# Initialize window
# =============================================================================
window = Tk()                                        #   Creating a Tkinter object
window.title("Penalty Shooter")                         #   Creating a title
window.geometry("600x420+0+0")                          #   Creating a screen x -> the dimensions and +gives the initial position location 
# window.wm_iconbitmap('ball.xbm')                      #   TODO Fix this
# =============================================================================
# Define text and photo inputs
# =============================================================================
logo = PhotoImage(file='/home/amarvk/projects/thesis/images/fire-soccer.gif')
header_text = """Penalty Shooter Game !
A game to engage the plantarflexion movement 
of the stroke patient using soccer"""
menu_heading = """ Please enter the game parameters"""
input1 = """Sensitivity - α"""
input2 = """Threshold torque - τ"""
input3 = """Level Progression parameter"""
checkbox1 = """None"""
checkbox2 = """Average"""
checkbox3 = """Maximum"""
checkbox4 = """Regression"""
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
menuHeading = Label(window,text = menu_heading, font = FONT).grid(row=1, sticky=W+E+N+S)

input1Text = Label(window,text = input1, font = FONT).grid(row=2, column =0, sticky=W)
input1entry = Entry(window).grid(row=2, column =1, sticky=W)

input2Text = Label(window,text = input2, font = FONT).grid(row=3, column =0, sticky=W)
input2entry = Entry(window).grid(row=3, column =1, sticky=W)

input3Text = Label(window,text = input3, font = FONT).grid(row=4, column =0, sticky=W)
input3entry1 = Checkbutton(window, text=checkbox1).grid(row=4, column =1, sticky =W)
input3entry2 = Checkbutton(window, text=checkbox2).grid(row=5, column =1, sticky =W)
input3entry3 = Checkbutton(window, text=checkbox3).grid(row=6, column =1, sticky =W)
input3entry4 = Checkbutton(window, text=checkbox4).grid(row=7, column =1, sticky =W)
# =============================================================================
# Setting up the footer UI
# =============================================================================
divider = Label(window,text = blanker, font = FONT).grid(row=8, column = 0, columnspan =2, sticky = N+E+W+S)
teamText = Label(window,text = team, font = FONT).grid(row=9, column = 0, columnspan =2, sticky = N+E+W+S)
teamMembers = Label(window,text = team_members, font = FONT).grid(row=10, column = 0, columnspan =2, sticky = N+E+W+S)
divider = Label(window,text = blanker, font = FONT).grid(row=11, column = 0, columnspan =2, sticky = N+E+W+S)
advisorText = Label(window,text = advisor, font = FONT).grid(row=12, column = 0, columnspan =2, sticky = N+E+W+S)
advisorName = Label(window,text = advisor_name, font = FONT).grid(row=13, column = 0, columnspan =2, sticky = N+E+W+S)
bottomLogo = Label(window, image = footer_image).grid(row =14, column = 0, columnspan = 2, sticky = W+E+N+S)
divider = Label(window,text = blanker, font = FONT).grid(row=15, column = 0, columnspan =2, sticky = N+E+W+S)

# =============================================================================
# widget3 = Label(window, text="Sensitivity - alpha")
# widget3.pack( side = LEFT)
# widget4 = Entry(window, bd =5)
# widget4.pack(side = RIGHT)
# =============================================================================

window.mainloop()                                       #   The window won't appear until we enter the Tkinter event loop: Our script will remain in the event loop until we close the window