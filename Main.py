import pygame   # Import Pygame for game development
import sys  # Import sys for system exit
from Settings import *  # Import game settings and constants
from player import Player   # Import Player class for player character
from level1 import Level1       # Import Level1 class for the first level
from level2 import Level2   # Import Level2 class for the second level

class Game:
    """Main game class to manage game states and levels."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(SCREEN_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_level_index = 0
        self.levels = [
            {"name": "Neon City Circuit", "class": Level1, "start_pos": LEVEL1_START_POS},
            {"name": "Lava Dome Arena", "class": Level2, "start_pos": LEVEL2_START_POS}
        ]
        self.current_level = None
        self.player = None
        self.load_level()

    def load_level(self):
        """Loads the current level based on the index."""
        if self.current_level_index < len(self.levels):
            level_info = self.levels[self.current_level_index]
            print(f"Loading {level_info['name']}...")
            self.current_level = level_info["class"]()
            self.current_level.init_level()
            self.player = Player(level_info["start_pos"])
            # TODO: Play level transition sound effect or display a transition screen
        else:
            print("All levels completed! Game Over.")
            self.running = False # End game after all levels

    def next_level(self):
        """Advances to the next level."""
        self.current_level_index += 1
        self.load_level()

    def run(self):
        """Main game loop."""
        while self.running:
            self._handle_events()
            self._update_game_state()
            self._draw_elements()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def _handle_events(self):
        """Handles Pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update_game_state(self):
        """Updates game logic for player, levels, and collisions."""
        self.player.update()
        self.current_level.update()

        # Collision detection with obstacles
        collided_obstacles = pygame.sprite.spritecollide(self.player, self.current_level.obstacles, False)
        for obstacle in collided_obstacles:
            self.player.handle_collision(obstacle)

        # Collision detection with boost pads
        collided_boost_pads = pygame.sprite.spritecollide(self.player, self.current_level.boost_pads, True) # True to remove boost pad after use
        for boost_pad in collided_boost_pads:
            self.player.activate_boost()
            # TODO: Add visual effect for boost pad activation (e.g., particles, light)
            # TODO: Play SFX_POWERUP

        # Collision detection with hazards
        collided_hazards = pygame.sprite.spritecollide(self.player, self.current_level.hazards, False)
        for hazard in collided_hazards:
            if isinstance(hazard, OilSlick):
                self.player.apply_oil_slick_effect()
            elif isinstance(hazard, FireHazard):
                self.player.apply_fire_hazard_effect()
            # TODO: Add visual effect for hazard interaction

        # Example: Check for level completion (e.g., player reaches a certain point)
        # For now, let\"s just transition after a set time or key press for testing
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]: # Press Enter to go to next level (for testing)
            self.next_level()

    def _draw_elements(self):
        """Draws all game elements on the screen."""
        self.screen.fill(BLACK) # Clear screen
        self.current_level.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
        pygame.display.flip() # Update the full display

# TODO: Add a TODO section for visual/audio implementation
"""TODO: Visuals and Audio
- Implement smooth transitions between levels (fade in/out, wipe effects).
- Play SFX_COUNTDOWN at the start of a level.
- Play SFX_LEVEL_COMPLETE when a level is finished.
- Add visual effects for boost pad activation.
- Add visual effects for hazard interactions.
"""

if __name__ == "__main__":
    game = Game()
    game.run()
