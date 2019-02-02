#! /usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#
# $Id:: 01_singleParticle.py 72 2015-05-16 20:08:55Z andrew.eldredge+locker@gm#$
# $Rev:: 72                                                                    $
# $Author:: andrew.eldredge+locker@gmail.com                                   $
# $Date:: 2015-05-16 14:08:55 -0600 (Sat, 16 May 2015)                         $
#
# Description: A single particle bouncing around a box
#
################################################################################

# MODULES
import pygame, math, sys;
from pygame.locals import *;
from pygame import draw;
import random;
#import pygame;

#CONSTANTS
TURN_SPEED = 5;
ACCELERATION = 2;
MAX_FORWARD_SPEED = 10;
MAX_REVERSE_SPEED = -5;

BLACK = (32,32,32);
BLUE_BG = (4,4,64);
WHITE = (192,192,192);
BOX_TOP = 0;
BOX_BOTTOM = 768;
BOX_LEFT = 0;
BOX_RIGHT = 1024;
MAX_PARTICLE_AXIS_SPEED = 10;
keepPlaying = True;

# INITIALIZATION
random.seed(); #defaults to system time (on import also)
screen = pygame.display.set_mode((1024,768));
car = pygame.image.load('car.png');
clock = pygame.time.Clock();
k_up = k_down = k_left = k_right = 0;
speed = direction = 0;
position = (random.randint(BOX_LEFT,BOX_RIGHT),
            random.randint(BOX_TOP,BOX_BOTTOM));
particle_position = [random.randint(BOX_LEFT,BOX_RIGHT),
                     random.randint(BOX_TOP,BOX_BOTTOM)];
particle_velocity = [random.randint(-MAX_PARTICLE_AXIS_SPEED,
                                     MAX_PARTICLE_AXIS_SPEED),
                     random.randint(-MAX_PARTICLE_AXIS_SPEED,
                                     MAX_PARTICLE_AXIS_SPEED)];

#initalizing the joystick
pygame.joystick.init()
if(pygame.joystick.get_count()):
   joystick = pygame.joystick.Joystick(0);
   joystick.init();

while keepPlaying:
    # USER INPUT
   clock.tick(30);
   for event in pygame.event.get():
       if not hasattr(event, 'key'): continue;
       down = event.type == KEYDOWN #Key down or up?
       if event.key == K_RIGHT: k_right = down * -5;
       elif event.key == K_LEFT: k_left = down * 5;
       elif event.key == K_UP: k_up = down * 2;
       elif event.key == K_DOWN: k_down = down * -2;
       elif event.key == K_ESCAPE: keepPlaying = False; #quit the game
       elif event.key == K_q: keepPlaying = False; #quit the game
   screen.fill(BLUE_BG);
   #read the joystick
   axis0 = joystick.get_axis( 0 );
   axis1 = joystick.get_axis( 1 );
   if(joystick.get_button( 8 )):
      speed = 0;
   if(joystick.get_button( 9 )):
      keepPlaying = False;
   if(joystick.get_button( 4 )):
      car_y = random.randint(BOX_TOP,BOX_BOTTOM);
      car_x = random.randint(BOX_LEFT,BOX_RIGHT);
   # SIMULATION
   # .. new speed and direction based on acceleration and turn
   speed += (k_up + k_down);
   if speed > MAX_FORWARD_SPEED: speed = MAX_FORWARD_SPEED;
   if speed < MAX_REVERSE_SPEED: speed = MAX_REVERSE_SPEED;
   direction += (k_right + k_left)
   # .. new position based on current position, speed and direction
   direction -= (int)(axis0*TURN_SPEED);
   speed -= (int)(axis1*MAX_FORWARD_SPEED);
   x, y = position;
   rad = direction * math.pi / 180;
   x += -speed*math.sin(rad);
   y += -speed*math.cos(rad);
   if x < BOX_LEFT:
      x = BOX_RIGHT;
   if x > BOX_RIGHT:
      x = BOX_LEFT;
   if y < BOX_TOP:
      y = BOX_BOTTOM;
   if y > BOX_BOTTOM:
      y = BOX_TOP;

   position = (x,y);
   #PARTICLE SIMULATION
   particle_position[0] += particle_velocity[0];
   particle_position[1] += particle_velocity[1];
   if particle_position[0] < BOX_LEFT:
      particle_velocity[0] *= -1;
   if particle_position[0] > BOX_RIGHT:
      particle_velocity[0] *= -1;
   if particle_position[1] < BOX_TOP:
      particle_velocity[1] *= -1;
   if particle_position[1] > BOX_BOTTOM:
      particle_velocity[1] *= -1;

   # RENDERING
   # .. rotate the car image for direction
   rotated_car = pygame.transform.rotate(car, direction);
   # .. position the car on the screen
   rect = rotated_car.get_rect();
   rect.center = position;
   # .. render the car to the screen
   screen.blit(rotated_car, rect);
   # .. draw a dot
   draw.circle(screen, WHITE, particle_position, 5, 0);
   pygame.display.flip();


#let this one alone until I know how to stop it.
#screen = pygame.display.setmode((1024,768),FULLSCREEN);
#other flags:
 #DOUBLEBUF
 #OPENGL - most pygame drawing stuff won't work.

#load up a car for display
#screen.blit(car, (50, 100));
#pygame.display.flip();

#import math;
#transform.rotate seems to prefer degrees
#rotated = pygame.transform.rotate(car, 45 * math.pi / 180);
#rotated = pygame.transform.rotate(car, 45);
#screen.blit(rotated, (50,100));
#pygame.display.flip();

#animate the car
#for i in range(100):
#    screen.fill((64,64,64));
#    screen.blit(car, (i,0));
#    pygame.display.flip();
print "game over"
