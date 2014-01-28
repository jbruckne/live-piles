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
        
    def update(self):
        pass
    
    def draw(self, screen):
        x = self.rect.x * (TILE_WIDTH + PADDING) + PADDING
        y = self.rect.y * (TILE_WIDTH + PADDING) + PADDING
        w = self.rect.w * (TILE_WIDTH + PADDING) - PADDING
        h = self.rect.h * (TILE_WIDTH + PADDING) - PADDING
        screen.fill(self.bgcolor, pygame.Rect(x, y, w, h))
        pass

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
        
        for x in range(3):
            self.tiles.append(BasicTile(x, 0, 1, 1, (0, 0, 0)))
            self.tiles.append(BasicTile(x, 3, 1, 1, (0, 0, 0)))
            self.tiles.append(BasicTile(3, x, 1, 1, (0, 0, 0)))
        self.tiles.append(BasicTile(0, 1, 3, 2, (0, 0, 255)))
    
    def update(self):
        self.bg.update()
        for tile in self.tiles:
            tile.update()

    def draw(self, screen):
        self.bg.draw(screen)
        for tile in self.tiles:
            tile.draw(screen)
        
