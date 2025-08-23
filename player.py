"""
Player spaceship for the Asteroids game.

Handles movement, rotation, shooting, and boundary wrapping.
- Triangle geometry code adapted from the Boot.dev lesson; all control logic and documentation are my own.
"""

import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        """
        Initialize the player at the given position.
        Sets rotation, shooting timer, and base radius.
        """
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def rotate(self, dt):
        """
        Rotate the ship based on turn speed and time delta.
        """
        self.rotation += PLAYER_TURN_SPEED * dt 

    def update(self, dt):
        """
        Handle user input for movement, rotation, and shooting.
        Update ship position and wrap around screen edges.
        """
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
            
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_SPACE]:
            if self.timer <= 0 :
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN
            
        
        self.warp()
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
         
         
    def warp(self): # This keeps the ship inside the frame 

        self.position.x = self.position.x % SCREEN_WIDTH

        self.position.y = self.position.y % SCREEN_HEIGHT
       
    def shoot(self): # This makes sure the shots fire come from the player ship
        player_shot = Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0,1)
        velocity = velocity.rotate(self.rotation) * PLAYER_SHOOT_SPEED
        player_shot.velocity = velocity


    def triangle(self): # In the player class code below was provided by lesson
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def draw(self,screen): # This draws in the player and sets the colour
        pygame.draw.polygon(screen,"white",self.triangle(), width=2)

    