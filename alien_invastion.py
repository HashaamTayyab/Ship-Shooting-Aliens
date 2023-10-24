import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # Settings class instance used to dynamically change the self.screen attribute
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        pygame.display.set_caption("Hashaam's Game")
        #Creating the instance of the Ship class from ship.py
        self.ship = Ship(self)
        self.clock = pygame.time.Clock()
        
        
    def run_game(self):
        """Start the main while loop for the game."""
        while True:
            #Helper function call (It can only be used within the class)
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
            
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        #For loop watches for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                    
                      
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #Fill the color with the color set in settings.py
        self.screen.fill(self.settings.bg_color)
        #Draws the ship on the screen
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()