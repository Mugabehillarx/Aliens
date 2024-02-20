class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 650
        self.screen_height = 1200
        self.bg_color = (128, 128, 128)

        # Ship settings
        self.ship_speed = 7.0

        # Bullet settings 
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3