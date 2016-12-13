import pygame
import os
from time import sleep


# Colours
WHITE = (255, 255, 255)

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((320, 240))
lcd.fill((0, 0, 0))
pygame.display.update()


lcd.set_at((10, 10), WHITE)
lcd.set_at((20, 10), WHITE)
lcd.set_at((30, 10), WHITE)
lcd.set_at((40, 100), WHITE)
pygame.display.update()