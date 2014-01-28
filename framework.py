import pygame

SCREEN_DIMENSIONS = 0;
PADDING = 32;
TILE_WIDTH = 256;

class Background:
    bgcolor = (50, 50, 50)
    
    def update(self):
        pass
    
    def draw(self, screen):
        screen.fill(self.bgcolor)
        pass

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
        screen.fill(self.bgcolor, pygame.Rect(x, y, w, h))

from tiles import *

class Framework:
    bg = None
    tiles = [];
    
    def __init__(self):
        global SCREEN_DIMENSIONS
        global PADDING
        global TILE_WIDTH
        
        SCREEN_HEIGHT = pygame.display.Info().current_h;
        PADDING = SCREEN_HEIGHT * 0.03;
        TILE_WIDTH = SCREEN_HEIGHT / 4 - PADDING * 1.25;
        
        pygame.mouse.set_visible(False)
        self.bg = Background()
        
        for x in range(5):
            self.tiles.append(ClockTile(x, x, 1, 1, (0, 0, 255)))
    
    def update(self):
        self.bg.update()
        for tile in self.tiles:
            tile.update()

    def draw(self, screen):
        self.bg.draw(screen)
        for tile in self.tiles:
            tile.draw(screen)
        
