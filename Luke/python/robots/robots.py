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
ROBOT2_SPEED = 4;
NUMBER_OF_LOCKBOTS = 10;
NUMBER_OF_WILDBOTS = 10;

#Initialization
 #Screen
screen = pygame.display.set_mode((BOX_RIGHT,BOX_BOTTOM	));
pygame.display.set_caption('Lukes game window');
 #Random Number Generator
clock = pygame.time.Clock();
random.seed();
 #get the joystick ready
pygame.joystick.init();
if(pygame.joystick.get_count()):
   joystick = pygame.joystick.Joystick(0);
   joystick.init();
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
         pygame.draw.rect(screen, (255,0,0),(self.pos_x-5,self.pos_y-5,10,10), 0);
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
   global robot_x;
   global robot_y;
   global robot2_x;
   global robot2_y;
   global player
   global moblist;
   player = Character();
   moblist = [];
   moblist = [Lockbot() for count in range(NUMBER_OF_LOCKBOTS)];
   moblist += [Wildbot() for count in range(NUMBER_OF_WILDBOTS)];
   keepPlaying = True;
   robot_x = random.randint(BOX_LEFT,BOX_RIGHT);
   robot_y = random.randint(BOX_TOP,BOX_BOTTOM);
   robot2_x =random.randint(BOX_LEFT,BOX_RIGHT);
   robot2_y =random.randint(BOX_TOP,BOX_BOTTOM);


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
   robot_x += int(axis2*ROBOT_SPEED);
   robot_y += int(axis3*ROBOT_SPEED);
   
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
   player.render();
   for robot in moblist:
      robot.render();
   pygame.draw.rect(screen, (0,255,0), 
(robot_x,robot_y,10,10), 0);
   pygame.draw.rect(screen,(0,255,0), 
(robot2_x,robot2_y,10,10), 0);
   pygame.display.flip();

    
print "Game over"
print "robot " + str(robot_x) + "," + str(robot_y)
print "robot2 " + str(robot2_x) + "," + str(robot2_y)

