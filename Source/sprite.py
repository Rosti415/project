import pygame
import Source.constants as constants


class Sprite:
    def __init__(self, size=(0, 0), start_coordinates=(0, 0),
                 speed: int = 0, health: int = 0, image=None):
        self.rect_ = pygame.rect.Rect(*start_coordinates, *size)
        self._speed_ = speed
        self._health_ = health
        self._image_ = image
        self.jump_sound = pygame.mixer.Sound(constants.MARIO_JUMP_SOUND)

    def get_coordinates(self):
        return self.rect_.x, self.rect_.y

    def get_image(self) -> pygame.Surface:
        return self._image_

    def get_health(self) -> int:
        return self._health_

    def get_speed(self) -> int:
        return self._speed_

    def set_coordinates(self, x: int, y: int) -> None:
        self.rect_.x = x
        self.rect_.y = y

    def fall(self):
        if self.get_coordinates()[1] < 400:
            self.change_coordinates(y=5)
    def jump(self):
        self.change_coordinates(1,-185)
        self.jump_sound.play()
    def change_coordinates(self, x=0, y=0) -> None:
        self.rect_.x += x
        self.rect_.y += y

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self._image_, self.get_coordinates())

