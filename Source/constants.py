import pygame

WIDTH, HEIGHT = 900, 500
MARIO_WIDTH, MARIO_HEIGHT = 37, 60
FPS = 60
START_X, START_Y = 20, 350

BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load(r"C:\GitRepos\Mario\Assets\background.jpg"), (WIDTH, HEIGHT))
MARIO_IMAGE = pygame.transform.scale(
    pygame.image.load(r"C:\GitRepos\Mario\Assets\mario.png"), (MARIO_WIDTH, MARIO_HEIGHT))
