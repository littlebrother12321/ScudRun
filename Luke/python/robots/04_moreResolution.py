#! /usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#
# $Id:: 04_moreResolution.py 94 2015-05-20 04:00:34Z andrew.eldredge+locker@gm#$
# $Rev:: 94                                                                    $
# $Author:: andrew.eldredge+locker@gmail.com                                   $
# $Date:: 2015-05-19 22:00:34 -0600 (Tue, 19 May 2015)                         $
#
# Description: Increased resolution so it will take longer to repeat
#
################################################################################

# MODULES
import pygame, math, sys;
from pygame.locals import *;
from pygame import draw;
import random;
#DEFINING THE JOYSTICK
pygame.joystick.init()
if(pygame.joystick.get_count()):
   joystick = pygame.joystick.Joystick(0);
   joystick.init();
CAR_SPEED = 10;
CAR_X = (CAR_SPEED);
CAR_Y = (CAR_SPEED);
#import pygame;


###CONSTANTS###
#SCREEN CONSTANTS
SCREEN_WIDTH = 1024;
SCREEN_CENTER_X = SCREEN_WIDTH>>1;
SCREEN_HEIGHT = 768;
#resolution power
PRT_RES = 8;


#CAR CONSTANTS
TURN_SPEED = 5;
ACCELERATION = 2;
MAX_FORWARD_SPEED = 10;
MAX_REVERSE_SPEED = -5;

#PARTICLE CONSTANTS
NUMBER_OF_PARTICLES = 1000;
BLACK = (32,32,32);
BLUE_BG = (4,4,64);
WHITE = (192,192,192);
RED = (192,32,32);
YELLOW = (192,192,32);
BRIGHT_WHITE = (255,255,255);
BOX_TOP = 0;
BOX_BOTTOM = SCREEN_HEIGHT<<PRT_RES;
BOX_LEFT = 0;
BOX_RIGHT = SCREEN_WIDTH<<PRT_RES;
MAX_PARTICLE_AXIS_SPEED = 17<<PRT_RES;
MAX_PARTICLE_SIZE = 7;
MIN_PARTICLE_SIZE = 1;
BOX_CENTER_X = (BOX_RIGHT - BOX_LEFT)>>1;
#Full Frame
#PARTICLE_START_LEFT = BOX_LEFT;
#PARTICLE_START_RIGHT = BOX_RIGHT;
#PARTICLE_START_TOP = BOX_TOP;
#PARTICLE_START_BOTTOM = BOX_BOTTOM;
#Right Side
PARTICLE_START_LEFT = BOX_RIGHT/2;
PARTICLE_START_RIGHT = BOX_RIGHT;
PARTICLE_START_TOP = BOX_TOP;
PARTICLE_START_BOTTOM = BOX_BOTTOM;
#Center Quarter
#PARTICLE_START_LEFT = BOX_RIGHT/4
#PARTICLE_START_RIGHT = 3*BOX_RIGHT/4;
#PARTICLE_START_TOP = BOX_BOTTOM/4;
#PARTICLE_START_BOTTOM = 3*BOX_BOTTOM/4;
#Center (over-ordered)
#PARTICLE_START_LEFT = BOX_RIGHT/2
#PARTICLE_START_RIGHT = BOX_RIGHT/2;
#PARTICLE_START_TOP = BOX_BOTTOM/2;
#PARTICLE_START_BOTTOM = BOX_BOTTOM/2;
#SCOREBOARD CONSTANTS
pygame.font.init();
scorefont = pygame.font.Font(None,30);
score_pos_left = SCREEN_WIDTH>>2;
score_pos_right = 3*SCREEN_WIDTH>>2;
score_pos_y = 50;
BAR_LEFT = (SCREEN_WIDTH-NUMBER_OF_PARTICLES)>>1;
#BAR_RIGHT = SCREEN_WIDTH - 100;
BAR_WIDTH = 20;
BAR_Y = score_pos_y + 30;


class TwoDof:
   def update(self):
      pass;
   def draw(self):
      pass;

class Particle(TwoDof):
   def __init__(self):
      self.position = [random.randint(PARTICLE_START_LEFT,PARTICLE_START_RIGHT),
                       random.randint(PARTICLE_START_TOP,PARTICLE_START_BOTTOM)];
      self.screenPos = [self.position[0]>>PRT_RES, self.position[1]>>PRT_RES];
      self.velocity = [random.randint(-MAX_PARTICLE_AXIS_SPEED,
                                       MAX_PARTICLE_AXIS_SPEED),
                       random.randint(-MAX_PARTICLE_AXIS_SPEED,
                                       MAX_PARTICLE_AXIS_SPEED)];
      self.size = random.randint(MIN_PARTICLE_SIZE,MAX_PARTICLE_SIZE);

   def update(self):
      self.position[0] += self.velocity[0];
      self.position[1] += self.velocity[1];
      if self.position[0] < BOX_LEFT:
         self.velocity[0] *= -1;
      if self.position[0] > BOX_RIGHT:
         self.velocity[0] *= -1;
      if self.position[1] < BOX_TOP:
         self.velocity[1] *= -1;
      if self.position[1] > BOX_BOTTOM:
         self.velocity[1] *= -1;

   def render(self):
      # .. draw a dot
      self.screenPos[0] = self.position[0]>>PRT_RES;
      self.screenPos[1] = self.position[1]>>PRT_RES;
      draw.circle(screen, WHITE, self.screenPos, self.size, 0);

# INITIALIZATION
random.seed(); #defaults to system time (on import also)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT));

#Car init
car = pygame.image.load('car.png');
clock = pygame.time.Clock();
k_up = k_down = k_left = k_right = 0;
speed = direction = 0;
position = (random.randint(0,SCREEN_WIDTH),
            random.randint(0,SCREEN_HEIGHT));

#particle init
particlelist = [Particle() for count in range(NUMBER_OF_PARTICLES)];

#scoreboard_init
centerMark = [[SCREEN_CENTER_X, BAR_Y-1],[SCREEN_CENTER_X-2, BAR_Y-6],[SCREEN_CENTER_X+2, BAR_Y-6]];

while 1:
    # USER INPUT
   clock.tick(30);
   for event in pygame.event.get():
       if not hasattr(event, 'key'): continue;
       down = event.type == KEYDOWN #Key down or up?
       if event.key == K_RIGHT: k_right = down * -5;
       elif event.key == K_LEFT: k_left = down * 5;
       elif event.key == K_UP: k_up = down * 2;
       elif event.key == K_DOWN: k_down = down * -2;
       elif event.key == K_ESCAPE: sys.exit(0) #quit the game
       elif event.key == K_q: sys.exit(0) #quit the game
   screen.fill(BLUE_BG);

   # SIMULATION
   # .. new speed and direction based on acceleration and turn
   speed += (k_up + k_down);
   if speed > MAX_FORWARD_SPEED: speed = MAX_FORWARD_SPEED;
   if speed < MAX_REVERSE_SPEED: speed = MAX_REVERSE_SPEED;
   direction += (k_right + k_left)
   # .. new position based on current position, speed and direction
   x, y = position;
   rad = direction * math.pi / 180;
   x += -speed*math.sin(rad);
   y += -speed*math.cos(rad);
   if x < 0:
      x = SCREEN_WIDTH;
   if x > SCREEN_WIDTH:
      x = 0;
   if y < 0:
      y = SCREEN_HEIGHT;
   if y > SCREEN_HEIGHT:
      y = 0;
   position = (x,y);

   for particle in particlelist:
       particle.update();
   #READ THE JOYSTICK
   axis0 = joystick.get_axis( 0 );
   axis1 = joystick.get_axis( 1 );
   if(joystick.get_button( 8 )):
      speed = 0;
   if(joystick.get_button( 9 )):
      keepPlaying = False;
   if(joystick.get_button( 4 )):
      car_y = random.randint(BOX_TOP,BOX_BOTTOM);
      car_x = random.randint(BOX_LEFT,BOX_RIGHT);
   direction -= (int)(axis0*TURN_SPEED);
   speed -= (int)(axis1*MAX_FORWARD_SPEED);
   # RENDERING
   # .. rotate the car image for direction
   rotated_car = pygame.transform.rotate(car, direction);
   # .. position the car on the screen
   rect = rotated_car.get_rect();
   rect.center = position;
   # .. render the car to the screen
   screen.blit(rotated_car, rect);

   # .. draw the particles and calulate score
   rightscore = 0;
   leftscore = 0;
   for particle in particlelist:
      if particle.position[0] > BOX_CENTER_X:
         rightscore += 1;
      else:
         leftscore += 1;
      particle.render();

   leftscoretext = scorefont.render(str(leftscore), 1, BRIGHT_WHITE);
   rightscoretext = scorefont.render(str(rightscore), 1, BRIGHT_WHITE);
   screen.blit(leftscoretext, [score_pos_left,score_pos_y]);
   screen.blit(rightscoretext, [score_pos_right,score_pos_y]);

   
   #not used yet
   #leftpercent = 100 * leftscore / (leftscore+rightscore);
   draw.rect(screen, RED, (BAR_LEFT,BAR_Y, leftscore, BAR_WIDTH));
   draw.rect(screen, YELLOW, (leftscore+BAR_LEFT,BAR_Y, rightscore, BAR_WIDTH));
   draw.polygon(screen, WHITE, centerMark);

   pygame.display.flip();
