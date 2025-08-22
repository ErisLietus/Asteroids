# Asteroids Game
# Dependencies: pygame 2.6.1
# To install: uv add pygame==2.6.1
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

pygame.init()
clock = pygame.time.Clock()
dt = 0
#To make the frame rate and the ship move as a consistance speed in different frame rates 
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
# groups to hold mutliple objects 

ship = Player(x = SCREEN_WIDTH/ 2, y = SCREEN_HEIGHT / 2) # making our space ship

asteroid_field = AsteroidField() # making the asteroids

def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

        screen.fill((0,0,0))

        updatable.update(dt)
        for asteroid in asteroids:
            if ship.collision(asteroid):
                print("Game over!")
                sys.exit()

        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
