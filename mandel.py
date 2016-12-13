import pygame
import os
from time import sleep




os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((320, 240))
lcd.fill((0, 0, 0))
pygame.display.update()

# Colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

lcd.set_at((0, 10), WHITE)
lcd.set_at((10, 10), WHITE)
lcd.set_at((30, 240), WHITE)
lcd.set_at((40, 239), BLUE)
pygame.display.update()

sleep(5)
