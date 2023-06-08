import pygame

WIDTH, HEIGHT = 900, 500
MARIO_WIDTH, MARIO_HEIGHT = 37, 60
FPS = 60
START_X, START_Y = 20, 400
WALL_X, WALL_Y = 200, 320
WALL_WIDTH, WALL_HEIGHT = 100, 50
PIN_X, PIN_Y = 315, 365
PIN_WIDTH, PIN_HEIGHT = 75, 85
LAVA_WIDTH, LAVA_HEIGHT = 400, 125
LAVA_X, LAVA_Y = 500, 450



BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load(r'C:\Users\akubo\OneDrive\Документи\GitHub\project\project\Assets\sky_mario.jpeg'), (WIDTH, HEIGHT))
BACKGROUND_SKY_IMAGE = pygame.transform.scale(
    pygame.image.load(r'C:\Users\akubo\OneDrive\Документи\GitHub\project\project\Assets\sky.jpeg'), (WIDTH, HEIGHT))
WALL_IMAGE = pygame.transform.scale(
    pygame.image.load(r"C:\Users\akubo\OneDrive\Документи\GitHub\project\project\Assets\wall-removebg-preview.png"), (WALL_WIDTH, WALL_HEIGHT))
MARIO_IMAGE = pygame.transform.scale(
    pygame.image.load(r"C:\Users\akubo\OneDrive\Документи\GitHub\project\project\Assets\mario.png"), (MARIO_WIDTH, MARIO_HEIGHT))
PIN_IMAGE = pygame.transform.scale(
    pygame.image.load(r"C:\Users\akubo\OneDrive\Документи\GitHub\project\project\Assets\pin.png"), (PIN_WIDTH, PIN_HEIGHT))
LAVA_IMAGE = pygame.transform.scale(
    pygame.image.load(r'C:\Users\akubo\OneDrive\Документи\GitHub\project\project\Assets\lava_2.png'), (LAVA_WIDTH, LAVA_HEIGHT))
