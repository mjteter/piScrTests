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
MaxIteration = 255

for xpix in range(320):
    for ypix in range(240):
        x = -2 + (3 * (float(xpix) / 320.0))
        y = -1 + (2 * (float(ypix) / 240.0))
        z = complex(x, y)
        c = z

        for iteration in xrange(MaxIteration):
            z = (z * z) + c
            if abs(z) > 2.236:
                break
            else:
                if iteration == MaxIteration - 1:
                    Colour = (0, 0, 0)
                else:
                    Colour = WHITE

        lcd.set_at((xpix, ypix), Colour)

        pygame.display.update()
    print "row " + xpix + "done"
# lcd.set_at((0, 10), WHITE)
# lcd.set_at((10, 10), WHITE)
# lcd.set_at((30, 240), WHITE)
# lcd.set_at((40, 239), BLUE)
# pygame.display.update()

sleep(5)
