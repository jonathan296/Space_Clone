import pygame
from settings import Settings
import sys
from ship import Ship


class SpaceClone:

    def __init__(self):
        pygame.init()  # initializes py game
        self.settings = Settings()  # initializes settings file

        # creates display window (adjust in settings.py)
        self.display_screen = pygame.display.set_mode((self.settings.screen_x, self.settings.screen_y))

        # window caption for game (adjust in settings.py)
        pygame.display.set_caption(self.settings.window_caption)

        self.ship = Ship(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.display_screen.fill(self.settings.background_RGB)  # RGB background color picker
            self.ship.blitme()

            pygame.display.flip()


# runs game
if __name__ == '__main__':
    ai = SpaceClone()
    ai.run_game()
