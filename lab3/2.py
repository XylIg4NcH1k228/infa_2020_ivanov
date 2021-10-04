import math
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

def lines(

def background(x, y, a, b, c):
    '''
    x, y - dimensions of the screen
    a:b:c - the ratio between the size of the sky, sea and land
    '''
    rect(screen, (0, 255, 255), (0, 0, x, y * a / (a + b + c)))
    rect(screen, (0, 0, 255), (0, y * a / (a + b + c), x, y * (a + b) / (a + b + c)))
    rect(screen, (255, 204, 0), (0, y * (a + b) / (a + b + c), x, y))
    
def sun(x, y, r):
    '''
    x, y - coordinates of the centre of the sun
    r - radius of the sun
    '''
    circle(screen, (255, 255, 0), (x, y), r)

def umbrella(x, y, h, w, H):
    '''
    x, y - coordinates of the umbrella's stand on the beach
    h - height of umbrella's stand
    w - width of umbrella's cover
    H - height of umbrella
    '''
    line(screen, (153, 51, 0), (x, y), (x, y - h), 10)
    polygon(screen, (153, 51, 102), [(x - w / 2, y - h), (x + w / 2, y - h), (x, y - H), (x - w / 2, y - h)])
    def lines()

background(400, 400, 3, 1, 1)
sun(300, 60, 100)
umbrella(100, 370, 100, 140, 140)

x1 = 30
x2 = 170
N = 6
color = (0, 0, 0)
h = (x2 - x1) // (N + 1)
x = x1 + h
for i in range(N):
    line(screen, color, (100, 230), (x, 270))
    x += h

rect(screen, (153, 51, 0), (250, 220, 80, 30))
polygon(screen, (153, 51, 0), [(330, 220), (390, 220), (330, 250), (330, 220)])
circle(screen, (153, 51, 0), (250, 220), 30)
rect(screen, (0, 0, 255), (0, 200, 400, 20))
rect(screen, (0, 255, 255), (0, 150, 400, 50))
circle(screen, (255, 255, 255), (347, 230), 7)
circle(screen, (0, 0, 0), (347, 230), 7, 2)
line(screen, (0, 0, 0), (270, 220), (270, 120), 6)
polygon(screen, (255, 255, 255), [(273, 120), (320, 170), (290, 170), (273, 120)])
polygon(screen, (0, 0, 0), [(273, 120), (320, 170), (290, 170), (273, 120)], 1)
polygon(screen, (255, 255, 255), [(273, 220), (320, 170), (290, 170), (273, 220)])
polygon(screen, (0, 0, 0), [(273, 220), (320, 170), (290, 170), (273, 220)], 1)
circle(screen, (255, 255, 255), (100, 40), 20)
circle(screen, (51, 51, 51), (100, 40), 20, 1)
circle(screen, (255, 255, 255), (80, 40), 20)
circle(screen, (51, 51, 51), (80, 40), 20, 1)
circle(screen, (255, 255, 255), (60, 40), 20)
circle(screen, (51, 51, 51), (60, 40), 20, 1)
circle(screen, (255, 255, 255), (50, 60), 20)
circle(screen, (51, 51, 51), (50, 60), 20, 1)
circle(screen, (255, 255, 255), (70, 60), 20)
circle(screen, (51, 51, 51), (70, 60), 20, 1)
circle(screen, (255, 255, 255), (90, 60), 20)
circle(screen, (51, 51, 51), (90, 60), 20, 1)
circle(screen, (255, 255, 255), (110, 60), 20)
circle(screen, (51, 51, 51), (110, 60), 20, 1)
circle(screen, (255, 255, 255), (120, 50), 20)
circle(screen, (51, 51, 51), (120, 50), 20, 1)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
