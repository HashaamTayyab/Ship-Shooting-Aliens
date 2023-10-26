class GameStats:
    """Track stats for the game."""
    def __init__(self, ai_game):
        """Initialize the statistics."""
        self.settingss = ai_game.settings
        self.reset_stats()
        
    def reset_stats(self):
        """Initializing stats that can change during the game."""
        self.ships_left = self.settingss.ship_limit