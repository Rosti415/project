import pygame

from Source.sprite import Sprite


class Tiles(Sprite):
    def __init__(self, size, start_coordinates, image):
        super().__init__(size, start_coordinates, image=image)

