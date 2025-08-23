"""
AsteroidField class for the Asteroids game.

Manages asteroid spawning at the edges of the screen and controls their introduction into the game.
"""

import pygame
import random
from asteroid import Asteroid
from constants import *

class AsteroidField(pygame.sprite.Sprite):
    # Each edge is defined by a direction and a function to compute spawn position
    edges = [
        [pygame.Vector2(1, 0), lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT)],
        [pygame.Vector2(-1, 0), lambda y: pygame.Vector2(SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT)],
        [pygame.Vector2(0, 1), lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS)],
        [pygame.Vector2(0, -1), lambda x: pygame.Vector2(x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS)],
    ]

    def __init__(self):
        """
        Initialize the AsteroidField.
        Sets up the spawn timer for asteroid spawning.
        """
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        """
        Create and add a new Asteroid to the game.

        Args:
            radius (float): The radius of the new asteroid.
            position (pygame.Vector2): The position where the asteroid will spawn.
            velocity (pygame.Vector2): The velocity vector for the asteroid's motion.
        """
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        """
        Update the field's internal timer. Spawn new asteroids at random intervals/edges.
        
        Args:
            dt (float): Time delta since the last frame, for consistent spawning.
        """
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # Spawn a new asteroid at a random edge with random speed/direction
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)