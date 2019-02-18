#!/usr/bin/python
#screen.py
#by luke
#make a screen appear and disappear by pressing "Q"

import pygame;

#get the screen ready
screen = pygame.display.set_mode((1024,768));
pygame.display.set_caption('Lukes game window');
clock = pygame.time.Clock();

#get the game ready
keepPlaying = True;
character_x =512; character_y =384;

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
   #Game Logic(empty for now)   
   #Draw the screen
   screen.fill((128,128,128));
   pygame.draw.circle(screen, (192,192,192), (character_x,character_y),5, 0);
   pygame.display.flip();
    
print "Game over"

