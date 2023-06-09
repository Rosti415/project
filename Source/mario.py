import pygame

import Source.constants as constants

from Source.sprite import Sprite


class Mario(Sprite):
    def __init__(self, size, start_coordinates, speed: int, health: int,
                 image):
        super().__init__(size, start_coordinates, speed, health, image)





    def move(self, key_pressed: pygame.key.ScancodeWrapper) -> None:
        if self.get_coordinates()[0] > 0 and key_pressed[pygame.K_a]:
            self.change_coordinates(x=-self._speed_)
        if self.get_coordinates()[1] < constants.WIDTH - self.rect_.width and key_pressed[pygame.K_d]:
            self.change_coordinates(x=self._speed_)

