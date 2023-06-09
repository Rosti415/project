import sys

import pygame

import Source.constants as constants

from Source.mario import Mario
from Source.wall import Wall
from Source.wall import Pin
from Source.wall import lava


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        self.clock = pygame.time.Clock()

        self.current_background = constants.BACKGROUND_IMAGE

        self.mario = Mario((constants.MARIO_WIDTH, constants.MARIO_HEIGHT), (constants.START_X, constants.START_Y),
                           5, 3, constants.MARIO_IMAGE)
        self.ok = True
        self.wall_list = [
            Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (constants.WALL_X, constants.WALL_Y),
                 constants.WALL_IMAGE),
            Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (constants.WALL_X + 200, constants.WALL_Y),
                 constants.WALL_IMAGE),
            Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (constants.WALL_X + 400, constants.WALL_Y - 100),
                 constants.WALL_IMAGE),
            Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (constants.WALL_X + 600, constants.WALL_Y - 200),
                 constants.WALL_IMAGE),
        ]
        self.pin_list = [
            Pin((constants.PIN_WIDTH, constants.PIN_HEIGHT), (constants.PIN_X, constants.PIN_Y),
                constants.PIN_IMAGE),
        ]
        self.lava_list = [
            lava((constants.LAVA_WIDTH, constants.LAVA_HEIGHT), (constants.LAVA_X, constants.LAVA_Y),
                 constants.LAVA_IMAGE),
        ]

        '''class Object:
            all_objects = [self.wall_list,
                           self.pin_list,
                           self.lava_list,]
            def __init__(self, x, y):
                self.x = x
                self.y = y
                Object.all_objects.append(self)'''

        pygame.display.set_caption('Mario')


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()




                self.screen.blit(self.current_background, (0, 0))
                if self.mario.get_coordinates()[0] > 850:
                    self.ok = False
                    self.current_background = constants.BACKGROUND_SKY_IMAGE
                    self.mario.change_coordinates(constants.START_X,constants.START_Y)
                    self.wall_list.clear()
                    self.pin_list.clear()
                    self.lava_list.clear()



                if self.mario.rect_.collidelist([lava.rect_ for lava in self.lava_list]) != -1:
                    self.mario.rect_.x = 100
                    self.mario.rect_.y = 100
                if self.mario.rect_.collidelist([Pin.rect_ for Pin in self.pin_list]) != -1:
                    self.mario.rect_.x = 100
                    self.mario.rect_.y = 100
                self.action_time = 2000
                self.last_action_time = 0
                self.current_time = pygame.time.get_ticks()
                if self.current_time - self.last_action_time >= self.action_time:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.mario.jump()
                    self.last_action_time = self.current_time
            if self.mario.rect_.collidelist([wall.rect_ for wall in self.wall_list]) == -1:
                self.mario.fall()
            if self.ok:
                self.screen.blit(constants.BACKGROUND_IMAGE, (0, 0))
            self.mario.draw(self.screen)
            for wall in self.wall_list:
                wall.draw(self.screen)
            for Pin in self.pin_list:
                Pin.draw(self.screen)
            for lava in self.lava_list:
                lava.draw(self.screen)
            self.mario.move(pygame.key.get_pressed())

            pygame.display.update()
            self.clock.tick(constants.FPS)
