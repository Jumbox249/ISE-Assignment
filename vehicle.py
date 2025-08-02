import pygame
import math
from settings import *

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image_path, start_pos):
        super().__init__()
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=start_pos)
        self.mask = pygame.mask.from_surface(self.image)

        self.position = pygame.math.Vector2(start_pos)
        self.velocity = pygame.math.Vector2(0, 0)
        self.angle = 0
        self.speed = 0
        self.lap = 1
        self.current_waypoint_index = 0

    def accelerate(self):
        self.speed += ACCELERATION

    def brake(self):
        self.speed += BRAKING

    def turn(self, direction):
        if self.speed > 0.1:
            if direction == 'left':
                self.angle += TURN_SPEED
            elif direction == 'right':
                self.angle -= TURN_SPEED

    def update(self):
        # Apply friction
        if self.speed > 0:
            self.speed += FRICTION
        
        # Clamp speed
        self.speed = max(0, min(self.speed, MAX_SPEED))

        # Update velocity and position
        self.velocity.from_polar((self.speed, -self.angle))
        self.position += self.velocity

        # Update image rotation and rect
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.position)
        self.mask = pygame.mask.from_surface(self.image)