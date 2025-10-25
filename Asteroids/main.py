import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids Game...")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Initialize Pygame
    pygame.init()
    #Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #Game loop
    while True:
        #Handle events, like quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Start with a black screen
        screen.fill((0, 0, 0))

        #Draw the player
        player.draw(screen)

        #Update the display
        pygame.display.flip()

        #It will pause the game loop until 1/60th of a second has passed.
        #Caps the frame rate at 60 FPS and calculates the time delta
        #Divided by 1000 to convert milliseconds to seconds
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()

