import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # If that is not the case, then spawn two smaller asteroids....
        # Create two new velocities by rotating the current velocity by a random angle
        random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        # Compute the new radius of the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # Create two new Asteroid objects at the current asteroid position with the new radius.
        # Set the first's velocity to the first new vector, but make it move faster by scaling it up (multiplying) by 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        # Do the same for the second asteroid, but with the second new vector.
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2
