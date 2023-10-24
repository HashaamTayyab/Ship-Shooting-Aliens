import pygame

class Ship:
    """A class to manage the ship"""
    
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #Loads the ship image and get its rect
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
        # Movement flag starts with a ship that is not moving
        self.moving_right = False
        
    def update(self):
        """Update the ships position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1
    
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)