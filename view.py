import pygame

class Gamein:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Binghamton Trail")
        self.font = pygame.font.Font(None, 36)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)

    def information(self, text, x, y, color=None, centered=False):
        if color is None:
            color = self.BLACK
        text_surface = self.font.render(text, True, color)
        if centered:
            text_rect = text_surface.get_rect(center=(x, y))
            self.screen.blit(text_surface, text_rect)
        else:
            self.screen.blit(text_surface, (x, y))

    def options(self, text, x, y, width=200, height=50):
        button = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, self.BLUE, button)
        text_surface = self.font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect(center=button.center)
        self.screen.blit(text_surface, text_rect)
        return button

    def first_screen(self):
        self.screen.fill(self.WHITE)
        self.information("Binghamton Trail", 300, 200)
        start_button = self.options("Start Game", 300, 300)
        pygame.display.flip()
        return start_button

    def dplayers(self, current_name):
        self.screen.fill(self.WHITE)
        self.information("Enter Your Name:", 300, 200)
        self.information(current_name + "_", 300, 250)
        pygame.display.flip()

    def periods(self, event, player):
        self.screen.fill(self.WHITE)
        event_text = event['time'] + " - " + event['name']
        description = event['description']
        stats_text = "Hunger: " + str(player.hunger) + "% Grade: " + str(player.grade) + "%"
        self.information(stats_text, 400, 50, centered=True)
        self.information(event_text, 400, 150, centered=True)
        self.information(description, 400, 200, centered=True)
        button = self.options("Continue", 300, 400)
        pygame.display.flip()
        return button

    def event_screen(self, state):
        self.screen.fill(self.WHITE)
        event = state.get_lev()
        if state.show_description:
            return self.periods(event, state.player)
        self.information(f"{event['time']} - {event['name']}", 50, 50)
        self.information(f"Hunger: {state.player.hunger} Grade: {state.player.grade}", 50, 100)
        buttons = []
        actions = ["study", "eat", "rest"]
        y = 400
        for action in actions:
            button = self.options(action.title(), 50, y)
            buttons.append((button, action))
            y += 60
        pygame.display.flip()
        return buttons

    def game_end(self, message):
        self.screen.fill(self.WHITE)
        self.information(message, 300, 250, centered=True)
        self.information("Thank you for playing my game!", 300, 350, centered=True)
        pygame.display.flip()