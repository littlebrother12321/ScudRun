#!/usr/bin/python
#screen.py
#by luke
#make a screen appear and disappear by pressing "Q"and "esc"

import pygame;
import random;

#get the screen ready
BOX_TOP = 0;
BOX_BOTTOM = 768;
BOX_LEFT = 0;
BOX_RIGHT = 1024;
CHARACTER_SPEED = 10;
ROBOT_SPEED = 20;
screen = pygame.display.set_mode((1024,768));
pygame.display.set_caption('Lukes game window');
clock = pygame.time.Clock();
random.seed();

#get the game ready
pygame.joystick.init()
if(pygame.joystick.get_count()):
   joystick = pygame.joystick.Joystick(0);
   joystick.init();


keepPlaying = True;
character_x =512; character_y =384;
robot_x = random.randint(BOX_LEFT,BOX_RIGHT);
robot_y =random.randint(BOX_TOP,BOX_BOTTOM);

while keepPlaying:
   clock.tick(30);
   #Handle Events (key press)
   for event in pygame.event.get():
      if not hasattr(event, 'key'):
         continue;
      if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
         keepPlaying = False;
      if event.key == pygame.K_w:
         character_y-= 3;
      if event.key == pygame.K_s:
         character_y+= 3;
      if event.key == pygame.K_a:
         character_x-= 3;
      if event.key == pygame.K_d:
         character_x+= 3;
   #Read the Joystick
   axis0 = joystick.get_axis( 0 );
   axis1 = joystick.get_axis( 1 );
   #Game Logic
   character_x += (int)(axis0*CHARACTER_SPEED);
   character_y += (int)(axis1*CHARACTER_SPEED);
   if(character_x > BOX_RIGHT):
      character_x = BOX_LEFT;
   if(character_x < BOX_LEFT):
      character_x = BOX_RIGHT;
   if(character_y < BOX_TOP):
      character_y = BOX_BOTTOM;
   if(character_y > BOX_BOTTOM):
      character_y = BOX_TOP;
   #Draw the screen
   screen.fill((128,128,128));
   pygame.draw.rect(screen, (255,0,0), (robot_x,robot_y,10,10), 0);
   pygame.draw.circle(screen, (192,192,192), (character_x,character_y),5, 0);
   pygame.display.flip();
    
print "Game over"

