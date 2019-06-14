import pygame
import os
import sys
import math
from random import *
from boids import boid

(width, height) = (640, 480)
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flock Sim")
screen.fill(WHITE)

pygame.display.flip()

#boid1 = boid((width/2), (height/2), 1, 1, os.urandom(1), os.urandom(1))

running = True
while running:

    screen.fill(WHITE)
    #print(os.urandom(1))
    print(int.from_bytes(os.urandom(1), byteorder='big')
    #boid.draw(boid1)
    #boid.update(boid1)

    pygame.display.update()
    clock.tick(60)

    # Break statement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
