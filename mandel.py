import pygame
from pygame.locals import *
import os
from time import sleep




os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((320, 240))
lcd.fill((0, 0, 0))
pygame.display.update()

# Colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
MaxIteration = 255

ctrX = -1.5
ctrY = 0
lenX = .5
lenY = 2.0 / 2.666 * lenX
startX = ctrX - lenX / 2.0
startY = ctrY - lenY / 2.0


for xpix in range(320):
    for ypix in range(240):
        x = startX + (lenX * (float(xpix) / 320.0))
        y = startY + (lenY * (float(ypix) / 240.0))
        z = complex(x, y)
        c = z
        Colour = (0, 0, 0)
        for iteration in xrange(MaxIteration):
            z = (z * z) + c
            if abs(z) > 2.0:  # was 2.236, why?
                break
            else:
                if iteration == MaxIteration - 1:
                    Colour = (0, 0, 0)
                else:
                    Colour = (0, iteration, iteration)

        
        lcd.set_at((xpix, ypix), Colour)
    if xpix % 5 == 0:
        pygame.display.update()
pygame.display.update()
print "done!"

while True:
    # Scan touchscreen events
    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            print "buttondown " + str(pos[0]) + ", " + str(pos[1])
        elif(event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            print "buttonup " + str(pos[0]) + ", " + str(pos[1])
            #Find which quarter of the screen we're in
            ctrXpix, ctrYpix = pos
            
            if ctrXpix < 20 and ctrYpix < 20:
                lenX *= 2.0
                lenY *= 2.0
            else:
                ctrX = startX + (lenX * (float(ctrXpix) / 320.0))
                ctrY = startY + (lenY * (float(ctrYpix) / 240.0))
                lenX *= .5
                lenY *= .5
            startX = ctrX - lenX / 2.0
            startY = ctrY - lenY / 2.0
            print str(ctrX) + ", " + str(ctrY)

            for xpix in range(320):
                for ypix in range(240):
                    x = startX + (lenX * (float(xpix) / 320.0))
                    y = startY + (lenY * (float(ypix) / 240.0))
                    z = complex(x, y)
                    c = z
                    Colour = (0, 0, 0)
                    for iteration in xrange(MaxIteration):
                        z = (z * z) + c
                        if abs(z) > 2.0:  # was 2.236, why?
                            break
                        else:
                            if iteration == MaxIteration - 1:
                                Colour = (0, 0, 0)
                            else:
                                Colour = (0, iteration, iteration)

        
                    lcd.set_at((xpix, ypix), Colour)
                if xpix % 5 == 0:
                    pygame.display.update()
            pygame.display.update()

    sleep(0.1)


pygame.display.update()
# lcd.set_at((0, 10), WHITE)
# lcd.set_at((10, 10), WHITE)
# lcd.set_at((30, 240), WHITE)
# lcd.set_at((40, 239), BLUE)
# pygame.display.update()

#sleep(5)
while (True):
    pass
