# Asteroids Game
# Dependencies: pygame 2.6.1
# To install: uv add pygame==2.6.1
import pygame
from constants import *
import player

pygame.init()
clock = pygame.time.Clock()
dt = 0
#To make the frame rate and the ship move as a consistance speed in different frame rates 

ship = player.Player(x = SCREEN_WIDTH/ 2, y = SCREEN_HEIGHT / 2)

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
        pygame.Surface.fill(screen,(0,0,0))
        ship.update(dt)
        ship.move(dt)
        ship.move(-dt)
        ship.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
