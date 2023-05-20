import sys

import pygame

import Source.constants as constants

from Source.mario import Mario
from Source.wall import Wall
from Source.wall import Pin

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        self.clock = pygame.time.Clock()

        self.mario = Mario((constants.MARIO_WIDTH, constants.MARIO_HEIGHT), (constants.START_X, constants.START_Y),
                           5, 3, constants.MARIO_IMAGE)

        self.wall_list = [
            Wall((constants.WALL_WIDTH,constants.WALL_HEIGHT),(constants.WALL_X,constants.WALL_Y),
            constants.WALL_IMAGE),
            Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (constants.WALL_X+200, constants.WALL_Y),
                 constants.WALL_IMAGE),
        ]
        self.pin_list = [
            Pin((constants.PIN_WIDTH,constants.PIN_HEIGHT),(constants.PIN_X,constants.PIN_Y),
            constants.PIN_IMAGE),
        ]


        pygame.display.set_caption('Mario')



    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.mario.jump()

            self.mario.fall()

            self.screen.blit(constants.BACKGROUND_IMAGE, (0, 0))
            self.mario.draw(self.screen)
            for wall in self.wall_list:
                wall.draw(self.screen)
            self.mario.move(pygame.key.get_pressed())

            pygame.display.update()
            self.clock.tick(constants.FPS)
