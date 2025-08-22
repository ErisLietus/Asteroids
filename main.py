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
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
player.Player.containers = (updatable, drawable)
# groups to hold mutliple objects 

ship = player.Player(x = SCREEN_WIDTH/ 2, y = SCREEN_HEIGHT / 2) # setting the screen size

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
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
