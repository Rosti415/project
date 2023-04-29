import pygame

from Source.sprite import Sprite


class Tiles(Sprite):
    def __init__(self, size: tuple[int, int], start_coordinates: tuple[int, int], image: pygame.Surface | None):
        super().__init__(size, start_coordinates, image=image)

