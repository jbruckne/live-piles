import time
import pygame
from framework import *

class ClockTile(BasicTile):
    time = None;
    textcolor = (0, 0, 0);
    
    def __init__(self, posx, posy, width, height, bgcolor, textcolor):
        BasicTile.__init__(self, posx, posy, width, height, bgcolor)
        self.textcolor = textcolor
        
        
    def draw(self, screen):
        BasicTile.draw(self, screen)
        
        x = self.getx()
        y = self.gety()
        
        w = self.getw()
        h = self.geth()
        
        myfont = pygame.font.SysFont("", int(min(w, h*2) / 4.5))
        label = myfont.render(time.strftime('%I:%M:%S%p'), 1, self.textcolor)
        
        textx = x + 0.5 * (w - label.get_width())
        texty = y + 0.5 * (h - label.get_height())
        screen.blit(label, (textx, texty))
