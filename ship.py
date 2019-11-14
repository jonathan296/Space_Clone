import pygame


class Ship:

    def __init__(self, ai_game):

        self.display_screen = ai_game.display_screen
        self.screen_rect = ai_game.display_screen.get_rect()

        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.display_screen.blit(self.image, self.rect)
