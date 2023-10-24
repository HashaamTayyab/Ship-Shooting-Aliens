class Settings:
    """A class to store all the settings for Hashaam's game"""
    def __init__(self):
        # Game window screen size
        self.screen_width = 750
        self.screen_height = 800
        
        # Screen background color
        self.bg_color = (230, 230, 230)
        
        # Ship speed settings
        self.ship_speed = 7