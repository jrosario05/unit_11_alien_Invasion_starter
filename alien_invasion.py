import sys
import pygame

class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        self.running = True

    def run_game(self):
        #Game loop
        while self.running:
            for event in pygame.event



if __name__ == '__main__':
    ai = AlienInvasion()


