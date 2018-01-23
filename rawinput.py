# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 09:25:13 2018

@author: Suchitra Chandar
"""

flag = 1
count = 0
torque_values = []
footswitch_values = []
while flag == 1:
    footswitch = raw_input("Footswitch:  ")
    torque = raw_input("Torque:  ")
    footswitch_values.append(footswitch)
    print footswitch_values[count]
    torque_values.append(torque)
    print torque_values[count]
    count += 1