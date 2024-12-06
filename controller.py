import pygame
import sys
from .model import LevelAt
from .view import Gamein

class Key:
    def __init__(self):
        self.state = LevelAt()
        self.view = Gamein()
        self.current_screen = "title"
        self.current_player_name = ""

    def screen(self):
        start_button = self.view.first_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    self.current_screen = "player_input"
        return True

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.current_player_name:
                    self.state.naming(self.current_player_name)
                    self.current_screen = "game"
                elif event.key == pygame.K_BACKSPACE:
                    self.current_player_name = self.current_player_name[:-1]
                else:
                    self.current_player_name += event.unicode
        self.view.dplayers(self.current_player_name)
        return True

    def location(self):
        buttons = self.view.event_screen(self.state)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.state.show_description:
                    if buttons.collidepoint(event.pos):
                        self.state.aknldge()
                else:
                    for button, action in buttons:
                        if button.collidepoint(event.pos):
                            self.state.player.actions(action)
                            if self.state.player.icheck():
                                self.current_screen = "game_over"
                            elif not self.state.ncontd():
                                self.current_screen = "victory"
        return True

    def run(self):
        running = True
        while running:
            if self.current_screen == "title":
                running = self.screen()
            elif self.current_screen == "player_input":
                running = self.input()
            elif self.current_screen == "game":
                running = self.location()
            elif self.current_screen in ["game_over", "victory"]:
                message = "You Graduated!"
                if self.current_screen == "game_over":
                    if self.state.player.hunger <= 0:
                        message = "You starved to death!"
                    elif self.state.player.grade <= 0:
                        message = "You failed out of Binghamton!"
                self.view.game_end(message)
                for event in pygame.event.get():
                    if event.type in [pygame.QUIT, pygame.KEYDOWN]:
                        running = False
        pygame.quit()