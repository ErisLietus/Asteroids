"""
Represents a projectile (shot) fired by the player to destroy asteroids.

Inherits from CircleShape for collision detection and shared interface.
"""

import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        """
        Render the shot as a white circle on the screen.
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        """
        Move the shot forward at its current velocity.
        """
        self.position += self.velocity * dt