import pygame
from settings import *

class Level:
    def __init__(self, track_image_path, waypoints, finish_line_rect):
        self.track_image = pygame.image.load(track_image_path).convert_alpha()
        self.track_mask = pygame.mask.from_surface(self.track_image)
        self.waypoints = waypoints
        self.finish_line = pygame.Rect(finish_line_rect)

    def draw(self, surface):
        surface.blit(self.track_image, (0, 0))