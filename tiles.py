import time
import pygame
from framework import *

class ClockTile(BasicTile):
    time = None;
    
    def update(self):
        BasicTile.update(self)
        
    def draw(self, screen):
        BasicTile.draw(self, screen)
        
        x = self.getx()
        y = self.gety()
        
        w = self.getw()
        h = self.geth()
        
        myfont = pygame.font.SysFont("monospace", int(min(w, h) / 4.5))
        label = myfont.render(time.strftime('%I:%M:%S%p'), 1, (255,255,255))
        
        textx = x + 0.5 * (w - label.get_width())
        texty = y + 0.5 * (h - label.get_height())
        screen.blit(label, (textx, texty))