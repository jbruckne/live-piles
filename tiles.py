import time
import pygame
from framework import *

class DateTimeTile(BasicTile):
    time = None
    textcolor = (0, 0, 0)
    formatstring = ""
    size = 1/5.0
    
    def __init__(self, posx, posy, width, height, bgcolor, textcolor, formatstring, size):
        BasicTile.__init__(self, posx, posy, width, height, bgcolor)
        self.textcolor = textcolor
        self.formatstring = formatstring
        self.size = size
        
    def draw(self, screen):
        BasicTile.draw(self, screen)
        
        x = self.getx()
        y = self.gety()
        
        w = self.getw()
        h = self.geth()
        
        myfont = pygame.font.SysFont("", int(min(w, h*2) * self.size))
        label = myfont.render(time.strftime(self.formatstring), 1, self.textcolor)
        
        textx = x + 0.5 * (w - label.get_width())
        texty = y + 0.5 * (h - label.get_height())
        screen.blit(label, (textx, texty))
        
        
