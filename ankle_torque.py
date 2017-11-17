#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 04:58:50 2017

@author: amarvk
"""

import numpy as np
import os, sys

path = "/home/amarvk/projects/thesis/ankle_data"
dirs = os.listdir(path)

list = np.asarray(dirs,dtype=str)

i = 0
for names in list:
    curr_path = '/home/amarvk/projects/thesis/ankle_data/' + names
    if i ==0:
        torque_vals = np.loadtxt(curr_path)[:,6]
        for i in range(0,torque_vals.shape[0]):
            if torque_vals[i] > 0:
                torque_vals[i] = 0
       # torque_vals = np.absolute(torque_vals)
        i+=1
    else:
        temp_vals = np.absolute(np.loadtxt(curr_path)[:,6])
        x = torque_vals.shape[0]
        y = temp_vals.shape[0]
    
        if x < y:
            diff = y-x
            torque_vals = np.lib.pad(torque_vals, (0,diff),'constant',constant_values=(0,0))
        elif x > y:
            diff = x-y
            temp_vals = np.lib.pad(temp_vals, (0,diff),'constant',constant_values=(0,0))                
        torque_vals = np.column_stack((torque_vals,temp_vals))
        i+=1

np.savetxt('torque_values.txt',torque_vals, delimiter = ' ', newline = '\n')
np.savetxt('torque_values.xlsx',torque_vals, delimiter = '\t', newline = '\n')