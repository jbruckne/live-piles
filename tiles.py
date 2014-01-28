import time
import pygame
from framework import *

class ClockTile(BasicTile):
    time = None;
    textcolor = (0, 0, 0);
    
    def getFormatString(self):
        return '%I:%M:%S%p';
    
    def getSizeScalar(self):
        return 1 / 4.5;
    
    def __init__(self, posx, posy, width, height, bgcolor, textcolor):
        BasicTile.__init__(self, posx, posy, width, height, bgcolor)
        self.textcolor = textcolor
        
        
    def draw(self, screen):
        BasicTile.draw(self, screen)
        
        x = self.getx()
        y = self.gety()
        
        w = self.getw()
        h = self.geth()
        
        myfont = pygame.font.SysFont("", int(min(w, h*2) * self.getSizeScalar()))
        label = myfont.render(time.strftime(self.getFormatString()), 1, self.textcolor)
        
        textx = x + 0.5 * (w - label.get_width())
        texty = y + 0.5 * (h - label.get_height())
        screen.blit(label, (textx, texty))

class DateTile(ClockTile):
    def getFormatString(self):
        return '%a %b %d, %Y';
    
    def getSizeScalar(self):
        return 1 / 5.5;
