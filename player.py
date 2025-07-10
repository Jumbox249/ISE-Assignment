import pygame
from Settings import *

class Player(pygame.sprite.Sprite):
    """Represents the player\'s car in the game."""

    def __init__(self, start_pos):
        """Initializes the player with a starting position."""
        super().__init__()
        # Player image placeholder
        # self.image = pygame.image.load(PLAYER_CAR_IMAGE) # TODO: Load actual image
        self.original_image = pygame.Surface((50, 80), pygame.SRCALPHA) # Dummy surface
        self.original_image.fill(NEON_BLUE) # Example color
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = PLAYER_SPEED
        self.angle = 0
        self.boost_active = False
        self.boost_timer = 0

    def update(self):
        """Updates the player\'s position and handles boost logic."""
        self._handle_input()
        self._move()
        self._handle_boost()

    def _handle_input(self):
        """Handles player input for movement and rotation."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self._rotate(PLAYER_ROTATION_SPEED)
        if keys[pygame.K_RIGHT]:
            self._rotate(-PLAYER_ROTATION_SPEED)
        if keys[pygame.K_UP]:
            self.speed = PLAYER_SPEED # Move forward
        elif keys[pygame.K_DOWN]:
            self.speed = -PLAYER_SPEED / 2 # Move backward (slower)
        else:
            self.speed = 0 # Stop if no movement key is pressed

        if keys[pygame.K_SPACE] and not self.boost_active:
            self.activate_boost()

    def _move(self):
        """Moves the player based on current speed and angle."""
        # Calculate movement vector based on angle
        rad_angle = pygame.math.Vector2(0, -1).rotate(-self.angle)
        self.rect.x += rad_angle.x * self.speed
        self.rect.y += rad_angle.y * self.speed

        # Keep player within screen bounds
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH: self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT: self.rect.bottom = SCREEN_HEIGHT

    def _rotate(self, amount):
        """Rotates the player\'s car."""
        self.angle += amount
        self.image = pygame.transform.rotate(self.original_image, self.angle) # Rotate the original dummy image
        self.rect = self.image.get_rect(center=self.rect.center)

    def activate_boost(self):
        """Activates the player\'s boost."""
        self.boost_active = True
        self.boost_timer = pygame.time.get_ticks() # Start boost timer
        self.speed = PLAYER_BOOST_SPEED
        # TODO: Play boost sound effect (SFX_BOOST)
        # TODO: Add boost visual effect (e.g., exhaust flames)

    def _handle_boost(self):
        """Handles the duration and deactivation of the boost."""
        if self.boost_active:
            if pygame.time.get_ticks() - self.boost_timer > 1000: # Boost lasts for 1 second
                self.boost_active = False
                self.speed = PLAYER_SPEED # Reset speed after boost
                # TODO: Stop boost visual effect

    def handle_collision(self, obstacle):
        """Handles collision with an obstacle."""
        # TODO: Play collision sound effect (SFX_COLLISION)
        # TODO: Add collision visual effect (e.g., sparks, screen shake)
        print(f"Collision with {obstacle.__class__.__name__}! ")
        # Example: Reduce speed on collision
        self.speed = PLAYER_SPEED / 2

    def apply_oil_slick_effect(self):
        """Applies the effect of hitting an oil slick."""
        # TODO: Add visual effect for oil slick (e.g., car spinning)
        print("Hit an oil slick! Loss of control.")
        # Example: Temporarily reduce rotation control or make car slide

    def apply_fire_hazard_effect(self):
        """Applies the effect of hitting a fire hazard."""
        # TODO: Add visual effect for fire hazard (e.g., car burning)
        print("Hit a fire hazard! Taking damage.")
        # Example: Reduce player health or slow down significantly

# TODO: Add a TODO section for visual/audio implementation
"""TODO: Visuals and Audio
- Replace PLAYER_CAR_IMAGE with actual car sprite.
- Implement proper image rotation without reloading the image every time.
- Add visual effects for boost (exhaust flames, blur).
- Add visual effects for collision (sparks, screen shake).
- Add visual effects for oil slick (car spinning, distorted movement).
- Add visual effects for fire hazard (car burning, smoke).
- Play SFX_BOOST when boost is activated.
- Play SFX_COLLISION on collision.
"""
