import pygame, sys
import simpy

pygame.init()

(width, height) = (640, 480)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bird Simulation")
screen.init()
pygame.display.flip()


print("Hello World")

while True:
    for event in pygame.event.get():
        if event.type == pyagame.QUIT:
            sys.exit(0)
        else:
            print(event)
