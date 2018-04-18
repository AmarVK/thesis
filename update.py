# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 16:07:24 2018

@author: Suchitra Chandar
"""

def y(action,y1,L,alpha_sens,prev_value,read_value,ymin,ymax):
    if action == "Dorsi":
        y1 = L - alpha_sens*prev_value
        y1actual = L - alpha_sens*read_value
        if y1 < ymin:
            y1 = ymin
        if y1actual < ymin:
            y1actual = ymin
        barh = 400*(y1actual-L)/(ymin-L)
    elif action == "Plantar":
        y1 = L + alpha_sens*prev_value
        y1actual = L + alpha_sens*read_value
        if y1 > ymax:
            y1 = ymax
        if y1actual > ymax:
            y1actual = ymax
        barh = 400*(y1actual-L)/(ymax-L)
    return y1,y1actual,barh

def score(action,y1,score):
    if action == "Dorsi":
        if y1 > 266: score = 0
        if y1 < 266 and y1 > 190: score = 2
        if y1 < 190 and y1 > 106: score = 5
        if y1 < 106: score = 10
    elif action == "Plantar":
        if y1+50 < 335: score = 0
        if y1+50 > 335 and y1+50 < 413: score = 2
        if y1+50 > 413 and y1+50 < 490: score = 5
        if y1+50 > 490: score = 10
    return score
    