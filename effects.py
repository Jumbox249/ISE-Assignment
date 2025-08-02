import pygame
import random
from settings import *

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color, lifetime):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.lifetime = lifetime
        self.spawn_time = pygame.time.get_ticks()
        self.velocity = pygame.math.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))

    def update(self):
        if pygame.time.get_ticks() - self.spawn_time > self.lifetime:
            self.kill()
        self.rect.move_ip(self.velocity)

class EffectsManager:
    def __init__(self):
        self.particles = pygame.sprite.Group()

    def create_explosion(self, x, y):
        for _ in range(20):
            particle = Particle(x, y, NEON_MAGENTA, 500)
            self.particles.add(particle)

    def create_tire_smoke(self, x, y):
        particle = Particle(x, y, ASPHALT_GREY, 200)
        self.particles.add(particle)

    def update(self):
        self.particles.update()

    def draw(self, surface):
        self.particles.draw(surface)