import os
import sys
import pygame
import time
import random
from pygame.locals import *
from framework import *
import default;

class Pyscope:
    screen = None;
    clock = None;
    framework = None;
    
    def __init__(self):
        # Initialize a new pygame screen using the framebuffer
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print "X display = {0}".format(disp_no)
        
        # Check which frame buffer drivers are available
        drivers = ['fbcon', 'directfb', 'svgalib']
        found = False
        for driver in drivers:
            # Make sure that SDL_VIDEODRIVER is set
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print 'Driver: {0} failed.'.format(driver)
                continue
            found = True
            break
    
        if not found:
            raise Exception('No suitable video driver found!')
        
        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print "Framebuffer size: %d x %d" % (size[0], size[1])
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        
        # Clear the screen to start
        self.screen.fill((0, 0, 0))        
        
        # Initialise font support
        pygame.font.init()
        
        # Render the screen
        pygame.display.update()
        
        # Initialize the clock
        self.clock = pygame.time.Clock()
        
        # Initialize the framework which will do all the work
        self.framework = Framework()
        default.setup(self.framework)
    
    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."
    
    def draw(self):
        self.framework.draw(self.screen)
        
        # Update the display
        pygame.display.update()

    def update(self):
        # Main update loop
        self.clock.tick(30)

    def input(self, events):
        # Input handling
        for event in events:
			
			# Close button
            if event.type == QUIT:
                exit()
            
            # Key pressed
            if event.type == KEYDOWN:
				
				# Escape key
                if event.key == K_ESCAPE:
                    exit()

# Create an instance of the PyScope class
scope = Pyscope()

# Application loop
while True:
    scope.input(pygame.event.get())
    scope.update()
    scope.draw()
