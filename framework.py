import pygame

SCREEN_DIMENSIONS = 0;
PADDING = 32;
TILE_WIDTH = 256;

class Background:
    bg = None;
    
    def __init__(self, bg):
        self.bg = bg;
    
    def update(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.bg, (0, 0))

class BasicTile:
    bgcolor = (0, 0, 0);
    rect = None;
    
    def __init__(self, posx, posy, width, height, bgcolor):
        self.rect = pygame.Rect(posx, posy, width, height)
        self.bgcolor = bgcolor
    
    def getx(self):
        return self.rect.x * (TILE_WIDTH + PADDING) + PADDING
    
    def gety(self):
        return self.rect.y * (TILE_WIDTH + PADDING) + PADDING
    
    def getw(self):
        return self.rect.w * (TILE_WIDTH + PADDING) - PADDING
    
    def geth(self):
        return self.rect.h * (TILE_WIDTH + PADDING) - PADDING
    
    def update(self):
        pass
    
    def draw(self, screen):
        x = self.getx()
        y = self.gety()
        w = self.getw()
        h = self.geth()
        
        s = pygame.Surface((w, h))
        s.set_alpha(175)
        s.fill(self.bgcolor, pygame.Rect(0, 0, w, h))
        screen.blit(s, (x,y))
        
from tiles import *

class Framework:
    bg = None
    tiles = [];
    
    def __init__(self):
        global SCREEN_DIMENSIONS
        global PADDING
        global TILE_WIDTH
        
        w = pygame.display.Info().current_w
        h = pygame.display.Info().current_h
        
        SCREEN_HEIGHT = h;
        PADDING = SCREEN_HEIGHT * 0.03;
        TILE_WIDTH = SCREEN_HEIGHT / 4 - PADDING * 1.25;
        
        pygame.mouse.set_visible(False)
        bg = pygame.transform.smoothscale(pygame.image.load("bg.jpg"), (w, h));
        self.bg = Background(bg)
    
    def update(self):
        self.bg.update()
        for tile in self.tiles:
            tile.update()

    def draw(self, screen):
        self.bg.draw(screen)
        for tile in self.tiles:
            tile.draw(screen)
        
