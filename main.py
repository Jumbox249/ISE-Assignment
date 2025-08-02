import pygame
from settings import *
from vehicle import Vehicle
from level import Level
from effects import EffectsManager
from ai import AIOpponent
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_state = "RACING"  # Start in RACING state for now

        self.create_placeholder_assets()

        # Level setup
        waypoints1 = [(150, 150), (WIDTH - 150, 150), (WIDTH - 150, HEIGHT - 150), (150, HEIGHT - 150)]
        finish_line1 = (100, 150, 10, 100)
        self.levels = [
            Level(TRACK_IMAGE_1, waypoints1, finish_line1),
            Level(TRACK_IMAGE_2, [], (0,0,0,0)) # Placeholder for level 2
        ]
        self.current_level_index = 0
        self.level = self.levels[self.current_level_index]

        # Player and AI setup
        self.player = Vehicle(PLAYER_IMAGE, (150, 200))
        self.ai1 = AIOpponent(AI_IMAGE, (150, 250), self.level.waypoints)
        self.ai2 = AIOpponent(AI_IMAGE, (150, 300), self.level.waypoints)
        self.all_sprites = pygame.sprite.Group(self.player, self.ai1, self.ai2)
        self.vehicles = pygame.sprite.Group(self.player, self.ai1, self.ai2)

        self.effects_manager = EffectsManager()
        self.sounds = {}
        self.load_sounds()

    def load_sounds(self):
        # Create placeholder sound files
        import os
        if not os.path.exists("assets"):
            os.makedirs("assets")
        
        with open("assets/crash.wav", "wb") as f:
            f.write(b'RIFF\x24\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x22\x56\x00\x00\x44\xac\x00\x00\x02\x00\x10\x00data\x00\x00\x00\x00')
        with open("assets/boost.wav", "wb") as f:
            f.write(b'RIFF\x24\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x22\x56\x00\x00\x44\xac\x00\x00\x02\x00\x10\x00data\x00\x00\x00\x00')

        self.sounds["crash"] = pygame.mixer.Sound("assets/crash.wav")
        self.sounds["boost"] = pygame.mixer.Sound("assets/boost.wav")

    def play_sound(self, name):
        if name in self.sounds:
            self.sounds[name].play()

    def create_placeholder_assets(self):
        import os
        if not os.path.exists("assets"):
            os.makedirs("assets")

        player_img = pygame.Surface((50, 30), pygame.SRCALPHA)
        player_img.fill(PLAYER_COLOR)
        pygame.image.save(player_img, PLAYER_IMAGE)

        ai_img = pygame.Surface((50, 30), pygame.SRCALPHA)
        ai_img.fill(AI_COLOR)
        pygame.image.save(ai_img, AI_IMAGE)

        track_img_1 = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(track_img_1, NEON_MAGENTA, (50, 50, WIDTH - 100, HEIGHT - 100), 10)
        pygame.image.save(track_img_1, TRACK_IMAGE_1)

        track_img_2 = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.ellipse(track_img_2, NEON_CYAN, (100, 100, WIDTH - 200, HEIGHT - 200), 10)
        pygame.image.save(track_img_2, TRACK_IMAGE_2)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        if self.game_state == "RACING":
            self.handle_input()
            self.all_sprites.update()
            self.check_collisions()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.accelerate()
        if keys[pygame.K_DOWN]:
            self.player.brake()
        if keys[pygame.K_LEFT]:
            self.player.turn('left')
        if keys[pygame.K_RIGHT]:
            self.player.turn('right')
        
        # Create tire smoke when turning
        if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and self.player.speed > 1:
            self.effects_manager.create_tire_smoke(self.player.rect.centerx, self.player.rect.centery)

    def check_collisions(self):
        # Check for collisions between vehicles and track boundaries
        for vehicle in self.vehicles:
            offset_x = int(vehicle.rect.left)
            offset_y = int(vehicle.rect.top)
            if self.level.track_mask.overlap(vehicle.mask, (offset_x, offset_y)):
                self.reset_vehicle(vehicle)
            
            # Check for lap completion
            if vehicle.rect.colliderect(self.level.finish_line):
                # Ensure the vehicle has passed all waypoints before incrementing the lap
                if vehicle.current_waypoint_index == len(self.level.waypoints) - 1:
                    vehicle.lap += 1
                    vehicle.current_waypoint_index = 0 # Reset for the next lap
                    if vehicle.lap > 3: # 3 laps to win
                        self.game_state = "RACE_OVER"

    def reset_vehicle(self, vehicle):
        # Find the last waypoint the vehicle passed
        last_waypoint_index = (vehicle.current_waypoint_index - 1) % len(self.level.waypoints)
        last_waypoint = self.level.waypoints[last_waypoint_index]
        
        # Reset the vehicle's position and state
        vehicle.position = pygame.math.Vector2(last_waypoint)
        vehicle.speed = 0
        vehicle.angle = 0 # Or calculate a better angle based on the track
        self.play_sound("crash")

    def draw(self):
        self.screen.fill(ASPHALT_GREY)
        self.level.draw(self.screen)
        self.all_sprites.draw(self.screen)
        self.effects_manager.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()