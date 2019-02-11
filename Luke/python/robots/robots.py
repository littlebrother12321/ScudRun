#!/usr/bin/python
#screen.py
#by luke
#make a screen appear and disappear by pressing "Q"and "esc"

import pygame;
import random;
import math;

#get the screen ready
BOX_TOP = 0;
BOX_BOTTOM = 768;
BOX_LEFT = 0;
BOX_RIGHT = 1024;
CHARACTER_SPEED = 4;
ROBOT_SPEED = 4;
ROBOT2_SPEED = 4;
screen = pygame.display.set_mode((BOX_RIGHT,BOX_BOTTOM	));
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
robot_y = random.randint(BOX_TOP,BOX_BOTTOM);
robot2_x =random.randint(BOX_LEFT,BOX_RIGHT);
robot2_y =random.randint(BOX_TOP,BOX_BOTTOM);

def tp_player_safe():
   global character_x;
   global character_y; 
   character_x = random.randint(BOX_LEFT,BOX_RIGHT); 
   character_y = random.randint(BOX_TOP,BOX_BOTTOM);
   print "teleporting..."

while keepPlaying:
   clock.tick(4000);
   #Handle Events (key press)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         keepPlaying = False;
      if event.type == pygame.JOYBUTTONDOWN:
         if(joystick.get_button( 10 )):
            tp_player_safe();
      if not hasattr(event, 'key'):
         continue;
      if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
         keepPlaying = False;
      if event.key == pygame.K_w:
         robot2_y-= 3;
      if event.key == pygame.K_s:
         robot2_y+= 3;
      if event.key == pygame.K_a:
         robot2_x-= 3;
      if event.key == pygame.K_d:
         robot2_x+= 3;
   #Read the Joystick
   axis0 = joystick.get_axis( 0 );
   axis1 = joystick.get_axis( 1 );
   axis2 = joystick.get_axis( 2 );
   axis3 = joystick.get_axis( 3 );
   if(joystick.get_button( 9 )):
      keepPlaying = False;
   if(joystick.get_button( 11 )):
      robot_x = random.randint(BOX_LEFT,BOX_RIGHT);
      robot_y = random.randint(BOX_TOP,BOX_BOTTOM);

   #Game Logic
      #interpret the joystick axes
   character_x += int(axis0*CHARACTER_SPEED);
   character_y += int(axis1*CHARACTER_SPEED);
   robot_x += int(axis2*ROBOT_SPEED);
   robot_y += int(axis3*ROBOT_SPEED);
   
   #limit the character to the game window
   if(character_x > BOX_RIGHT):
      character_x = BOX_RIGHT;
   if(character_x < BOX_LEFT):
      character_x = BOX_LEFT;
   if(character_y < BOX_TOP):
      character_y = BOX_TOP;
   if(character_y > BOX_BOTTOM):
      character_y = BOX_BOTTOM;

   #allowing the robot to wrap
   if(robot_x > BOX_RIGHT):
      robot_x = BOX_LEFT;
   if(robot_x < BOX_LEFT):
      robot_x = BOX_RIGHT;
   if(robot_y < BOX_TOP):
      robot_y = BOX_BOTTOM;
   if(robot_y > BOX_BOTTOM):
      robot_y = BOX_TOP;

   #allowing the robot2 to wrap
   if(robot2_x > BOX_RIGHT):
      robot2_x = BOX_LEFT;
   if(robot2_x < BOX_LEFT):
      robot2_x = BOX_RIGHT;
   if(robot2_x < BOX_LEFT):
      robot2_x = BOX_RIGHT;
   if(robot2_y < BOX_TOP):
      robot2_y = BOX_BOTTOM;
   if(robot2_y > BOX_BOTTOM):
      robot2_y = BOX_TOP;

   #Draw the screen
   screen.fill((12,0,128));

   pygame.draw.rect(screen, (255,0,0), 
(robot_x,robot_y,10,10), 0);
   pygame.draw.circle(screen, (192,192,192),
(character_x,character_y),5, 0);
   pygame.draw.rect(screen,(255,0,0), 
(robot2_x,robot2_y,10,10), 0);
   pygame.display.flip();

    
print "Game over"
print "robot " + str(robot_x) + "," + str(robot_y)
print "robot2 " + str(robot2_x) + "," + str(robot2_y)
