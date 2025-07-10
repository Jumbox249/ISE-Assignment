import pygame

# TODO: Add visual assets (images) here
# Example: PLAYER_IMAGE = "player.png"

# TODO: Add audio assets (sound effects) here
# Example: BOOST_SFX = "boost.wav"

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Rocket Runners: Turbo Track Showdown"

# Game settings
FPS = 60
PLAYER_SPEED = 5
PLAYER_BOOST_SPEED = 10
PLAYER_ROTATION_SPEED = 3

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NEON_BLUE = (0, 255, 255)
LAVA_RED = (255, 69, 0)

# Asset Placeholders (replace with actual paths later)
PLAYER_CAR_IMAGE = "assets/player_car.png"
OBSTACLE_CONE_IMAGE = "assets/obstacle_cone.png"
BOOST_PAD_IMAGE = "assets/boost_pad.png"
OIL_SLICK_IMAGE = "assets/oil_slick.png"
FIRE_HAZARD_IMAGE = "assets/fire_hazard.png"

LEVEL1_BACKGROUND_IMAGE = "assets/neon_city_background.png"
LEVEL2_BACKGROUND_IMAGE = "assets/lava_dome_background.png"

SFX_BOOST = "assets/sfx_boost.wav"
SFX_COLLISION = "assets/sfx_collision.wav"
SFX_POWERUP = "assets/sfx_powerup.wav"
SFX_COUNTDOWN = "assets/sfx_countdown.wav"
SFX_LEVEL_COMPLETE = "assets/sfx_level_complete.wav"

# Fonts
FONT_PATH = None # Default Pygame font
FONT_SIZE_LARGE = 72
FONT_SIZE_MEDIUM = 48
FONT_SIZE_SMALL = 24

# Level specific settings (placeholders)
LEVEL1_START_POS = (100, 100)
LEVEL2_START_POS = (100, 100)

# TODO: Add more game settings as needed
