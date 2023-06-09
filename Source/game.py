import sys

import pygame

from pygame import mixer
import Source.constants as constants

from Source.mario import Mario
from Source.wall import Wall
from Source.wall import Pin
from Source.wall import lava
from Source.wall import castle


pygame.mixer.init()
pygame.mixer.music.load(constants.MARIO_SOUND)
pygame.mixer.music.play(-1)
class Background:
    def __init__(self):
        self.current_screen_image = constants.BACKGROUND_IMAGE
        self.screen_images = [constants.BACKGROUND_IMAGE, constants.BACKGROUND_SKY_IMAGE,
                              constants.BACKGROUND_FINAL_IMAGE]
        self.screen_index = 0
        self.walls = {
            constants.BACKGROUND_IMAGE: [
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (constants.WALL_X, constants.WALL_Y),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (constants.WALL_X + 200, constants.WALL_Y),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (constants.WALL_X + 400, constants.WALL_Y - 100),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (constants.WALL_X + 600, constants.WALL_Y - 200),
                     constants.WALL_IMAGE),
            ],
            constants.BACKGROUND_SKY_IMAGE: [
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (15, 200),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (250, 250),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (485, 200),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (750, 250),
                     constants.WALL_IMAGE), ],

            constants.BACKGROUND_FINAL_IMAGE: [
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (0, 450),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (175, 450),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (355, 450),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (535, 450),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (715, 450),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (85, 450),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (265, 450),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (445, 450),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (625, 450),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (805, 450),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (200, 350),
                     constants.WALL_IMAGE),
                Wall((constants.WALL_WIDTH, constants.WALL_HEIGHT), (400, 350),
                     constants.WALL_IMAGE),
            ],

        }
        self.pins = {
            constants.BACKGROUND_IMAGE: [
                Pin((constants.PIN_WIDTH, constants.PIN_HEIGHT), (constants.PIN_X, constants.PIN_Y),
                    constants.PIN_IMAGE),
            ],
            constants.BACKGROUND_SKY_IMAGE: [],
            constants.BACKGROUND_FINAL_IMAGE: [],
        }
        self.lavas = {
            constants.BACKGROUND_IMAGE: [
                lava((constants.LAVA_WIDTH, constants.LAVA_HEIGHT), (constants.LAVA_X, constants.LAVA_Y),
                     constants.LAVA_IMAGE),
            ],
            constants.BACKGROUND_SKY_IMAGE: [],
            constants.BACKGROUND_FINAL_IMAGE: [
                lava((constants.LAVA_WIDTH, constants.LAVA_HEIGHT), (150, 450),
                     constants.LAVA_IMAGE),
            ],
        }
        self.castles = {
            constants.BACKGROUND_IMAGE: [],
            constants.BACKGROUND_SKY_IMAGE: [],
            constants.BACKGROUND_FINAL_IMAGE: [
                castle((constants.CASTLE_WIDTH, constants.CASTLE_HEIGHT), (730, 305),
                       constants.CASTLE_IMAGE),
            ],
        }

    def next(self):
        self.screen_index += 1
        self.current_screen_image = self.screen_images[self.screen_index]

    def previous(self):
        self.screen_index -= 1
        self.current_screen_image = self.screen_images[self.screen_index]

    def set_index(self, index):
        self.screen_index = index
        self.current_screen_image = self.screen_images[self.screen_index]

    def get_objects(self):
        return self.walls[self.current_screen_image], \
            self.pins[self.current_screen_image], self.lavas[self.current_screen_image], self.castles[self.current_screen_image]

    def get_current_screen_image(self):
        return self.current_screen_image

    def get_current_index(self):
        return self.screen_index


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        self.clock = pygame.time.Clock()

        self.background = Background()

        self.mario = Mario((constants.MARIO_WIDTH, constants.MARIO_HEIGHT), (constants.START_X, constants.START_Y),
                           5, 3, constants.MARIO_IMAGE)


        self.current_background = self.background.get_current_screen_image()
        self.wall_list, self.pin_list, self.lava_list, self.castle_list = self.background.get_objects()

        pygame.display.set_caption('Mario')
        self.jump_counter = 0
        self.jump_timer = pygame.time.get_ticks()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.current_time = pygame.time.get_ticks()

                if self.current_time - self.jump_timer >= 240:
                    self.jump_counter = 0
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and self.jump_counter < 2:
                            self.mario.jump()
                            self.jump_counter += 1
                            self.jump_timer = self.current_time

            self.current_background = self.background.get_current_screen_image()
            self.wall_list, self.pin_list, self.lava_list, self.castle_list = self.background.get_objects()
            self.screen.blit(self.current_background, (0, 0))

            if self.mario.get_coordinates()[0] > 850 and self.background.get_current_index() < 2:
                self.background.next()
                self.mario.set_coordinates(60, self.mario.get_coordinates()[1])

            if self.mario.get_coordinates()[0] < 50 and self.background.get_current_index() > 0:
                self.background.previous()

            if self.mario.get_coordinates()[1] > 250 and self.background.get_current_index() == 1:
                self.background.previous()

                self.mario.set_coordinates(50, 50)

            if self.mario.rect_.collidelist([lava.rect_ for lava in self.lava_list]) != -1:
                self.mario.set_coordinates(100, 100)
            if self.mario.rect_.collidelist([Pin.rect_ for Pin in self.pin_list]) != -1:
                self.mario.set_coordinates(100, 100)


            if self.mario.rect_.collidelist([wall.rect_ for wall in self.wall_list]) == -1:
                self.mario.fall()

            self.mario.draw(self.screen)

            for wall in self.wall_list:
                wall.draw(self.screen)
            for pin in self.pin_list:
                pin.draw(self.screen)
            for l in self.lava_list:
                l.draw(self.screen)
            for castle in self.castle_list:
                castle.draw(self.screen)
            if self.mario.rect_.collidelist([castle.rect_ for castle in self.castle_list]) != -1:
                pygame.init()
                font = pygame.font.Font(None, 124)
                text = font.render('Victory', True, (255, 255, 255))
                text_rect = text.get_rect(center=(constants.WIDTH // 2, constants.HEIGHT // 2))
                self.screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                pygame.quit()
                sys.exit()

            self.mario.move(pygame.key.get_pressed())

            pygame.display.update()
            self.clock.tick(constants.FPS)
