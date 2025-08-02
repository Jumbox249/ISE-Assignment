import pygame
from settings import *
from vehicle import Vehicle

class AIOpponent(Vehicle):
    def __init__(self, image_path, start_pos, waypoints):
        super().__init__(image_path, start_pos)
        self.waypoints = waypoints
        self.current_waypoint_index = 0

    def update(self):
        self.navigate()
        super().update()

    def navigate(self):
        # Simple waypoint navigation
        if self.waypoints:
            target_waypoint = self.waypoints[self.current_waypoint_index]
            target_vector = pygame.math.Vector2(target_waypoint) - self.position
            distance = target_vector.length()

            if distance < 50:
                self.current_waypoint_index = (self.current_waypoint_index + 1) % len(self.waypoints)

            # Steer towards the target
            desired_angle = target_vector.angle_to(pygame.math.Vector2(1, 0))
            angle_diff = (desired_angle - (-self.angle)) % 360
            if angle_diff > 180:
                angle_diff -= 360

            if angle_diff > 5:
                self.angle -= TURN_SPEED
            elif angle_diff < -5:
                self.angle += TURN_SPEED

            # Control speed
            self.accelerate()