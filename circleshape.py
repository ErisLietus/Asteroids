"""
CircleShape base class.

Represents all game objects as circles to simplify collision detection and interactions.
- This class was provided by the lesson.
- The `collision` function and its documentation were implemented by me.
"""

import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Initialize sprite and assign it to sprite groups if 'containers' is defined
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # To be implemented by sub-classes: Draw shape on the given screen
        pass

    def update(self, dt):
        # To be implemented by sub-classes: Update shape's state
        pass

    def collision(self, target):
        """
        Checks if this circular object collides with another circle-shaped target.

        Args:
            target (CircleShape): The other game object to check collision with.

        Returns:
            bool: True if the objects overlap, False otherwise.
        """
        # Use vector distance to check for overlapping circles (collision)
        return self.position.distance_to(target.position) <= self.radius + target.radius