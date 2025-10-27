from turtle import backward
import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot
from menu import Menu


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        # Add a rotation field
        self.rotation = 0
        self.shot_limit = 0


    # Draw the player as a triangle
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # Rotate the player by dt multiplied by turn speed
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # Move the player forward in the direction it's facing
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def update(self, dt):
        self.shot_limit -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Rotate left with -dt
            self.rotate(dt=-dt)
        if keys[pygame.K_d]:
            # Rotate right
            self.rotate(dt=dt)
        if keys[pygame.K_w]:
            # Move forward
            self.move(dt)
        if keys[pygame.K_s]:  
            # Move backward with -dt
            self.move(dt=-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_ESCAPE]:
            Menu().pause_menu(pygame.display.get_surface())


    def shoot(self):
        if self.shot_limit > 0:
            return
        self.shot_limit = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


    # A player will look like a triangle, 
    # even though we'll use a circle to represent its hitbox.
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]