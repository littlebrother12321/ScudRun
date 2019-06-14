import pygame

(width, height) = (1280, 720)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

class boid:
    def __init__(self, posX, posY, velX, velY, accX, accY):
        self.posX = posX
        self.posY = posY
        self.velX = velX
        self.velY = velY
        self.accX = accX / 10
        self.accY = accY / 10

    tmpAccX = self.accX / 10
    tmpAccY = self.accY / 10
    tmpVelX = self.velX
    tmpVelY = self.velY

    def draw(self):
        pygame.draw.circle(screen, BLACK, (int(self.posX), int(self.posY)), 5)

    def update(self):
        if self.posX >= width or self.posX <= 0:
            #self.posX = width/2
            self.velX = tmpVelX * -1
            self.accX = tmpAccX

        if self.posY >= height or self.posY <= 0:
            #self.posY = height/2
            self.velY = tmpVelY * -1
            self.accY = tmpAccY

        self.velX += self.accX
        self.velY += self.accY

        self.posX += self.velX
        self.posY += self.velY

boids = []
