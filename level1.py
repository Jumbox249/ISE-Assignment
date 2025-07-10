import pygame
from Settings import *

class Obstacle(pygame.sprite.Sprite):
    """Base class for obstacles in the game."""
    def __init__(self, image_path, size, pos):
        super().__init__()
        # self.image = pygame.image.load(image_path) # TODO: Load actual image
        self.image = pygame.Surface(size, pygame.SRCALPHA) # Dummy surface
        self.image.fill((100, 100, 100)) # Example color for obstacles
        self.rect = self.image.get_rect(center=pos)

class BoostPad(Obstacle):
    """Represents a boost pad that gives the player a temporary speed boost."""
    def __init__(self, pos):
        super().__init__(BOOST_PAD_IMAGE, (60, 60), pos)
        self.image.fill(NEON_BLUE) # Example color for boost pads

class OilSlick(Obstacle):
    """Represents an oil slick that causes the player to lose control."""
    def __init__(self, pos):
        super().__init__(OIL_SLICK_IMAGE, (50, 50), pos)
        self.image.fill((50, 50, 50)) # Example color for oil slicks

class FireHazard(Obstacle):
    """Represents a fire hazard that damages the player."""
    def __init__(self, pos):
        super().__init__(FIRE_HAZARD_IMAGE, (70, 70), pos)
        self.image.fill(LAVA_RED) # Example color for fire hazards

class Level1:
    """Defines the layout, obstacles, and events for Neon City Circuit."""

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.boost_pads = pygame.sprite.Group()
        self.hazards = pygame.sprite.Group()
        # self.background_image = pygame.image.load(LEVEL1_BACKGROUND_IMAGE) # TODO: Load actual background
        self.background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)) # Dummy background
        self.background_image.fill(BLACK) # Example background color

    def init_level(self):
        """Initializes the elements for Level 1: Neon City Circuit."""
        print("Initializing Level 1: Neon City Circuit")

        # Add obstacles
        obstacle1 = Obstacle(OBSTACLE_CONE_IMAGE, (40, 40), (200, 200))
        obstacle2 = Obstacle(OBSTACLE_CONE_IMAGE, (40, 40), (400, 300))
        self.obstacles.add(obstacle1, obstacle2)
        self.all_sprites.add(obstacle1, obstacle2)

        # Add boost pads
        boost_pad1 = BoostPad((100, 400))
        self.boost_pads.add(boost_pad1)
        self.all_sprites.add(boost_pad1)

        # Add hazards
        oil_slick1 = OilSlick((500, 150))
        fire_hazard1 = FireHazard((300, 500))
        self.hazards.add(oil_slick1, fire_hazard1)
        self.all_sprites.add(oil_slick1, fire_hazard1)

        # TODO: Define track layout and boundaries for Neon City Circuit
        # This could involve drawing lines or using a tilemap system

    def draw(self, screen):
        """Draws the level elements on the screen."""
        screen.blit(self.background_image, (0, 0))
        self.all_sprites.draw(screen)

    def update(self):
        """Updates level-specific logic (e.g., moving obstacles, events)."""
        # TODO: Implement dynamic level elements or events specific to Neon City
        pass

# TODO: Add a TODO section for visual/audio implementation
"""TODO: Visuals and Audio
- Replace LEVEL1_BACKGROUND_IMAGE with actual Neon City background.
- Replace OBSTACLE_CONE_IMAGE, BOOST_PAD_IMAGE, OIL_SLICK_IMAGE, FIRE_HAZARD_IMAGE with actual sprites.
- Implement visual effects for boost pads (e.g., glowing, particles).
- Implement visual effects for oil slicks (e.g., shimmering, slippery animation).
- Implement visual effects for fire hazards (e.g., flames, heat distortion).
"""
