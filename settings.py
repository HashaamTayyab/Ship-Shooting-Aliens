class Settings:
    """A class to store all the settings for Hashaam's game"""
    def __init__(self):
        """Initialize the game static settings."""
        # Game window screen size
        self.screen_width = 800
        self.screen_height = 800
        
        # Screen background color
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed = 7
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_speed = 4.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 13
        
        # ALien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # How quickly the game speeds up.
        self.speedup_scale = 1.1
        
        # How quickly the alien point value increases.
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 7.0
        self.bullet_speed = 4.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # Score settings for shooting down aliens.
        self.alien_points = 50
        
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        