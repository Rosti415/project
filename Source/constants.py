import pygame

WIDTH, HEIGHT = 900, 500
MARIO_WIDTH, MARIO_HEIGHT = 37, 60
FPS = 60
START_X, START_Y = 20, 400
WALL_X,WALL_Y = 100,50
WALL_WIDTH,WALL_HEIGHT = 100,50
PIN_X,PIN_Y = 75,100
PIN_WIDTH,PIN_HEIGHT= 100,75

BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load(r'C:\Users\User\Documents\GitHub\project\Assets\sky_mario.jpeg.'), (WIDTH, HEIGHT))
WALL_IMAGE = pygame.transform.scale(
    pygame.image.load(r"C:\Users\User\Documents\GitHub\project\Assets\wall.png"),(WALL_WIDTH,WALL_HEIGHT))
MARIO_IMAGE = pygame.transform.scale(
    pygame.image.load(r"C:\Users\User\Documents\GitHub\project\Assets\mario.png"), (MARIO_WIDTH, MARIO_HEIGHT))
PIN_IMAGE = pygame.transform.scale(
    pygame.image.load(r"C:\Users\User\Documents\GitHub\project\Assets\pin.png"), (PIN_WIDTH, PIN_HEIGHT))
