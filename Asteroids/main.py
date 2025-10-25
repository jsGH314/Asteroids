import pygame
from constants import *

def main():
    print("Starting Asteroids Game...")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Initialize Pygame
    pygame.init()
    #Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Game loop
    while True:
        #Handle events, like quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Start with a black screen
        screen.fill((0, 0, 0))
        #Update the display
        pygame.display.flip()



if __name__ == "__main__":
    main()

