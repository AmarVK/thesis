#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:57:31 2017

@author: amarvk
"""

class Game:
    def _init_(self, mode):
        self.gamemode = self.mode

class Dorsiflexion(Game):
    def _init_(self, max_angle, progression, beta, window_size ):
        self.max_angle = max_angle
        self.progression = progression
        self.beta = beta
        self.window_size = window_size
        
class Plantarflexion(Game):
    def _init_(self, max_torque, threshold, progression, beta, window_size):
        self.max_torque = max_torque
        self.threshold = threshold
        self.progression = progression
        self.beta = beta
        self.window_size = window_size