import sys
import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
from player import Player
from shot import Shot

# TODO add main menu and game over screen
# TODO add scoring system
# TODO add extra lives

def main():
    print("Starting Asteroids Game...")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize Pygame
    pygame.init()

    # Delay importing Menu until after pygame.init() to avoid "font not initialized"
    from menu import Menu

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids: the pygame remake")
    # Create a clock to manage the frame rate
    clock = pygame.time.Clock()
    dt = 0

    menus = Menu()

    # Create sprite groups for updatable and drawable objects (player, asteroids, bullets)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set the containers for the Player class
    # This ensures that any new Player instance will be added to these groups automatically
    Player.containers = (updatable, drawable)
    # Set the containers for the Asteroid class
    # This ensures that any new Asteroid instance will be added to these groups automatically
    Asteroid.containers = (asteroids, updatable, drawable)
    # Set the containers for the AsteroidField class
    AsteroidField.containers = (updatable)
    # Set the containers for the Shot class
    Shot.containers = (shots, updatable, drawable)

    # Create the player and asteroid field instances
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    menus.main_menu(screen)

    # Game loop
    while True:
        # Handle events, like quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all updatable objects
        updatable.update(dt)

        # Check for collisions between the player and asteroids
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            # Check for collisions between shots and asteroids
            for shot in shots:
                if asteroid.collides_with(shot):
                    # Remove the shot from screen using built in kill() method
                    shot.kill()
                    # Split the asteroid into smaller ones
                    asteroid.split()

        # Start with a black screen
        screen.fill("black")

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()

        # It will pause the game loop until 1/60th of a second has passed.
        # Caps the frame rate at 60 FPS and calculates the time delta
        # Divided by 1000 to convert milliseconds to seconds
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()

