"""
Asteroids Game
---------------
Main script for the Asteroids game.
Handles initialization, the main game loop, rendering, user input, and collisions.

Dependencies:
    - pygame 2.6.1 (install with: uv add pygame==2.6.1)
"""


import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

pygame.init()
clock = pygame.time.Clock()
dt = 0  # Frame time delta (for consistent speed across framerates)

# Sprite groups for updating and drawing game objects
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

# Assign groups to relevant sprite classes
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (shots, updatable, drawable)

# Initialize game objects
ship = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
asteroid_field = AsteroidField()

def main(): 
    """
    Initializes the game window and runs the main loop.
    - Handles events and input.
    - Updates game state (player, asteroids, shots).
    - Detects collisions between ship, asteroids, and shots.
    - Renders all drawable objects each frame.
    """
    # Game initialization and loop follows...
    
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000 # Frame rate and pace control
        screen.fill((0,0,0))

        updatable.update(dt) # Updating the inputs to e.g move ship forward pressing W
        for asteroid in asteroids: 
            if ship.collision(asteroid):
                print("Game over!")
                sys.exit() # Ends game on collision

            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill() # Removes shot on collision
                    asteroid.split() # split asteroid into smaller ones
                  

        for drawing in drawable: # Draws all objects on the screen
            drawing.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
