#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:58:22 2017

@author: amarvk
"""

import pygame
import main-menu 

class App:
    def __init__(self):
        self.running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640,400
        
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DUBLEBUF)
        self._running = True
            
    def on_execute(self):
        pass
    
if __name__ == "__main__":
    theApp = App()
    theApp.on_init()
    theApp.on_execute()
    