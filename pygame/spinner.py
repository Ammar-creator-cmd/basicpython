import pygame
import sys
import math
from pygame.locals import QUIT, MOUSEBUTTONDOWN

pygame.init()

window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Spinner")

#colour
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
Yellow = (255, 255, 0)

background_image = pygame.image.load("background.png").convert()
background_image = pygame.transform.scale(background_image, (window_width, window_height))