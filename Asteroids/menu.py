from http.client import GATEWAY_TIMEOUT
from constants import *
import sys
import pygame

class Menu:
    
    def __init__(self):
        # Ensure pygame is initialized before creating fonts.
        # Expectation: caller (main) calls pygame.init() before instantiating Menu.
        # Do not call pygame.init() here to avoid surprising import-time side-effects.
        self.FONT = pygame.font.Font(None, 74)
        self.SMALL_FONT = pygame.font.Font(None, 50)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)
        self.DARK_GRAY = (100, 100, 100)

    # Main menu loop
    def main_menu(self, screen):
        menu_running = True
        while menu_running:
            screen.fill(self.BLACK)  # Background

            self.draw_text("Asteroids!", self.FONT, self.WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

            # Button positions
            start_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
            quit_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 70, 200, 50)

            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()
        
            # Draw Start Button
            if start_button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, self.DARK_GRAY, start_button_rect)
            else:
                pygame.draw.rect(screen, self.GRAY, start_button_rect)
            self.draw_text("Start Game", self.SMALL_FONT, self.BLACK, screen, start_button_rect.centerx, start_button_rect.centery)

            # Draw Quit Button
            if quit_button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, self.DARK_GRAY, quit_button_rect)
            else:
                pygame.draw.rect(screen, self.GRAY, quit_button_rect)
            self.draw_text("Quit", self.SMALL_FONT, self.BLACK, screen, quit_button_rect.centerx, quit_button_rect.centery)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # On click events (start, quit)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button_rect.collidepoint(mouse_pos):
                        menu_running = False  # Exit menu, start game
                        self.difficulty_menu(screen)
                    if quit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()

    def pause_menu(self, screen):
        paused = True
        while paused:
            screen.fill(self.BLACK)

            self.draw_text("Paused!", self.FONT, self.WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

            resume_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
            main_menu_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 70, 200, 50)

            mouse_pos = pygame.mouse.get_pos()
            # Draw Resume Button
            if resume_button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, self.DARK_GRAY, resume_button_rect)
            else:
                pygame.draw.rect(screen, self.GRAY, resume_button_rect)
            self.draw_text("Resume", self.SMALL_FONT, self.BLACK, screen, resume_button_rect.centerx, resume_button_rect.centery)

            # Draw Main Menu Button
            if main_menu_button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, self.DARK_GRAY, main_menu_button_rect)
            else:
                pygame.draw.rect(screen, self.GRAY, main_menu_button_rect)
            self.draw_text("Main Menu", self.SMALL_FONT, self.BLACK, screen, main_menu_button_rect.centerx, main_menu_button_rect.centery)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # On click events (resume, main menu)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if resume_button_rect.collidepoint(mouse_pos):
                        paused = False
                    if main_menu_button_rect.collidepoint(mouse_pos):
                        self.main_menu(screen)
                        paused = False

            pygame.display.flip()

    def game_over(self,screen):
        game_over = True
        while game_over:
            screen.fill(self.BLACK)

            self.draw_text("Game Over!", self.FONT, self.WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

            main_menu_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
            quit_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 70, 200, 50)

            mouse_pos = pygame.mouse.get_pos()
            # Draw Main Menu Button
            if main_menu_button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, self.DARK_GRAY, main_menu_button_rect)
            else:
                pygame.draw.rect(screen, self.GRAY, main_menu_button_rect)
            self.draw_text("Main Menu", self.SMALL_FONT, self.BLACK, screen, main_menu_button_rect.centerx, main_menu_button_rect.centery)

            # Draw Quit Button
            if quit_button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, self.DARK_GRAY, quit_button_rect)
            else:
                pygame.draw.rect(screen, self.GRAY, quit_button_rect)
            self.draw_text("Quit", self.SMALL_FONT, self.BLACK, screen, quit_button_rect.centerx, quit_button_rect.centery)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # On click events (resume, main menu)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if main_menu_button_rect.collidepoint(mouse_pos):
                        paused = False
                        self.main_menu(screen)
                    if quit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()            

            pygame.display.flip()

    def difficulty_menu(self, screen):
        difficulty_running = True
        while difficulty_running:
            screen.fill(self.BLACK)
            self.draw_text("Select Difficulty", self.FONT, self.WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

            # Button positions
            normal_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
            hard_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 70, 200, 50)

            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()

            # Draw Normal Button
            if normal_button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, self.DARK_GRAY, normal_button_rect)
            else:
                pygame.draw.rect(screen, self.GRAY, normal_button_rect)
            self.draw_text("Normal", self.SMALL_FONT, self.BLACK, screen, normal_button_rect.centerx, normal_button_rect.centery)

            # Draw Hard Button
            if hard_button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, self.DARK_GRAY, hard_button_rect)
            else:
                pygame.draw.rect(screen, self.GRAY, hard_button_rect)
            self.draw_text("Hard", self.SMALL_FONT, self.BLACK, screen, hard_button_rect.centerx, hard_button_rect.centery)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # On click events (normal, hard)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if normal_button_rect.collidepoint(mouse_pos):
                        difficulty_running = False
                    if hard_button_rect.collidepoint(mouse_pos):
                        difficulty_running = False

            pygame.display.flip()

    def draw_text(self, text, font, color, surface, x, y):
        # Helper function to draw text on the screen.
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        surface.blit(textobj, textrect)




