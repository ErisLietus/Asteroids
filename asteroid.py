"""
Defines the Asteroid class for the Asteroids game.

Controls asteroid rendering, movement, and splitting upon being shot.
"""

import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    """
    Asteroid object that can move, be drawn, and split into smaller asteroids.
    Inherits from CircleShape.
    """

    def __init__(self, x, y, radius):
        """
        Initialize an asteroid at position (x, y) with a given radius.
        """
        super().__init__(x, y, radius)

    def draw(self, screen):
        """
        Draw the asteroid as a white outlined circle.
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        """
        Update the asteroid's position based on its velocity and the elapsed time.
        """
        self.position += self.velocity * dt

    def split(self):
        """
        Split the asteroid into two smaller asteroids when destroyed,
        unless it's already at the minimum size. If already at minimum size,
        the asteroid is simply removed.

        Returns:
            tuple of Asteroid or None: The two new asteroids, or None if the asteroid is already at minimum size.
        """
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None
        random_angle = random.uniform(20, 50)
        new_vector1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
        new_vector2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_vector1 * 1.2

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_vector2 * 1.2

        return (new_asteroid1, new_asteroid2)