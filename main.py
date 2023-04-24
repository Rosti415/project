import sys

import pygame
from pygame.locals import*

WIDTH,HEIGHT = 900,500
MARIO_WIDTH,MARIO_HEIGHT = 37,60
FPS = 60
START_X,START_Y = 35,200

BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load('bg.jpg'),(WIDTH,HEIGHT))
MARIO_IMAGE = pygame.transform.scale(pygame.image.load('mario_1-removebg-preview.png'),(MARIO_WIDTH,MARIO_HEIGHT))


class Mario:
    def __init__(self):
        self.rect = pygame.rect.Rect(START_X,START_Y,MARIO_WIDTH,MARIO_HEIGHT)
        self.image =MARIO_IMAGE



class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Mario')
        self.clock = pygame.time.Clock()
        self.mario = Mario()
    def run(self):
        while True:
            self.screen.blit(BACKGROUND_IMAGE,(0,0))
            self.screen.blit(MARIO_IMAGE,(20,350))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()






            pygame.display.update()
            self.clock.tick(FPS)

def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()