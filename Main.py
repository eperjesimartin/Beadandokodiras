import pygame, sys
from settings import *
from level import Level

class Game:
    def init(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Survivor game')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('Black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if name == 'main':
    game = Game()
    game.run()