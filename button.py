import pygame.font
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from alien_invasion import AlienInvasion


class Button:
    def __int__(self, game: 'AlienInvasion', msg):
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, self.settings.button_font_size )
        self.rect = pygame.Rect(0,0, self.settings.alien_w, self.settings.buttom_h)
        self.rect.center = self.boundaries.center
