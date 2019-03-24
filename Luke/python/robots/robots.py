#!/usr/bin/python
#screen.py
#by Luke
#with help from Dad

import pygame;
import random;

#Setting Constants
BOX_TOP = 0;
BOX_BOTTOM = 768;
BOX_LEFT = 0;
BOX_RIGHT = 1024;
MAX_CHARACTER_SPEED = 4;
ROBOT_SPEED = 4;
NUMBER_OF_LOCKBOTS = 10;
NUMBER_OF_WILDBOTS = 10;

#Initialization
 #Screen
screen = pygame.display.set_mode((BOX_RIGHT,BOX_BOTTOM	));
pygame.display.set_caption('Robots');
 #Random Number Generator
clock = pygame.time.Clock();
random.seed();
 #get the joystick ready
pygame.joystick.init();
if(pygame.joystick.get_count()):
   joystick = pygame.joystick.Joystick(0);
   joystick.init();
#load robot pictures
greenbot = pygame.image.load('greenbot.png');
 #game states
keepPlaying = True;



#define functions
   #define classes
class mob:
   def __init__(self):
      pass
   def render(self):
      pass
   def update(self):
      pass

class Character(mob):
   def __init__(self):
      self.pos_x = 512;
      self.pos_y = 384;
   def render(self):
      pygame.draw.circle(screen, (192,192,192),(self.pos_x,self.pos_y),5, 0);
   def update(self):
      #interpret the joystick axes
      self.pos_x += int(axis0*MAX_CHARACTER_SPEED);
      self.pos_y += int(axis1*MAX_CHARACTER_SPEED);
      #limit the character to the game window
      if(self.pos_x > BOX_RIGHT):
         self.pos_x = BOX_RIGHT;
      if(self.pos_x < BOX_LEFT):
          self.pos_x = BOX_LEFT;
      if(self.pos_y < BOX_TOP):
         self.pos_y = BOX_TOP;
      if(self.pos_y > BOX_BOTTOM):
         self.pos_y = BOX_BOTTOM;
   def tp_player_safe(self): 
      self.pos_x = random.randint(BOX_LEFT,BOX_RIGHT); 
      self.pos_y = random.randint(BOX_TOP,BOX_BOTTOM);
      print "teleporting..."

class Lockbot(mob):
   def __init__(self):
      self.pos_x = random.randint(BOX_LEFT,BOX_RIGHT);
      self.pos_y = random.randint(BOX_TOP,BOX_BOTTOM);
      self.broken = False;
   def render(self):
      # .. draw a robot
      if self.broken:
         pygame.draw.rect(screen, (0,0,0),(self.pos_x-5,self.pos_y-5,10,10), 0);
      else:
         #pygame.draw.rect(screen, (255,0,0),(self.pos_x-5,self.pos_y-5,10,10), 0);
         screen.blit(greenbot, [self.pos_x-5, self.pos_y-5]);
   def update(self,x,y):
      #these robots follow you around
      if(not self.broken):
         if x > self.pos_x:
            self.pos_x += 1; 
         if x < self.pos_x:
            self.pos_x -= 1;
         if y > self.pos_y:
            self.pos_y += 1; 
         if y < self.pos_y:
            self.pos_y -= 1;
   def collided(self,x,y,dist):
      if((abs(x - self.pos_x) <dist) and (abs(y - self.pos_y) <dist)):
         return True;
      else:
         return False;

class Wildbot(mob):
   def __init__(self):
      self.pos_x = random.randint(BOX_LEFT,BOX_RIGHT);
      self.pos_y = random.randint(BOX_TOP,BOX_BOTTOM);
      self.velocity = [random.randint(-ROBOT_SPEED,
                                       ROBOT_SPEED),
                       random.randint(-ROBOT_SPEED,
                                       ROBOT_SPEED)];
      self.velocity = [1, 1];
      self.broken = False;
   def render(self):
      # .. draw a robot
      if self.broken:
         pygame.draw.rect(screen, (0,0,0),(self.pos_x-5,self.pos_y-5,10,10), 0);
      else:
         pygame.draw.rect(screen, (128,0,0),(self.pos_x-5,self.pos_y-5,10,10), 0);
   def update(self,x,y):
      # these robots bounce around and off the walls
      if(not self.broken):
         self.pos_x += self.velocity[0];
         self.pos_y += self.velocity[1];
         if self.pos_x < BOX_LEFT:
            self.velocity[0] *= -1;
         if self.pos_x > BOX_RIGHT:
            self.velocity[0] *= -1;
         if self.pos_y < BOX_TOP:
            self.velocity[1] *= -1;
         if self.pos_y > BOX_BOTTOM:
            self.velocity[1] *= -1;
   def collided(self,x,y,dist):
      if((abs(x - self.pos_x) <dist) and (abs(y - self.pos_y) <dist)):
         return True;
      else:
         return False;




#setting up the game
def reset_game():
   global keePlaying;
   global player
   global moblist;
   player = Character();
   moblist = [];
   moblist = [Lockbot() for count in range(NUMBER_OF_LOCKBOTS)];
   moblist += [Wildbot() for count in range(NUMBER_OF_WILDBOTS)];
   keepPlaying = True;
 

#Start the game
reset_game();
while keepPlaying:
   clock.tick(60);
   #Handle Events (key press)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         keepPlaying = False;
      if event.type == pygame.JOYBUTTONDOWN:
         if(joystick.get_button( 10 )):
            player.tp_player_safe();
         if(joystick.get_button( 8 )):
            reset_game();
      if not hasattr(event, 'key'):
         continue;
      if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
         keepPlaying = False;

   #Read the Joystick
   axis0 = joystick.get_axis( 0 );
   axis1 = joystick.get_axis( 1 );
   axis2 = joystick.get_axis( 2 );
   axis3 = joystick.get_axis( 3 );
   if(joystick.get_button( 9 )):
      keepPlaying = False;


   #Game Logic

   
   player.update();
   #move class robots and check for collisions
   for i in range(len(moblist)):
      moblist[i].update(player.pos_x,player.pos_y);
      if(moblist[i].collided(player.pos_x,player.pos_y,3)):
         keepPlaying = False;
         print "you died";
      for j in range(i+1,len(moblist)):
         if(moblist[i].collided(moblist[j].pos_x,moblist[j].pos_y,5)):
            moblist[i].broken=True;
            moblist[j].broken=True;





   #Draw the screen
   screen.fill((12,0,128));
   player.render();
   for robot in moblist:
      robot.render();
   pygame.display.flip();

    
print "Game over"


