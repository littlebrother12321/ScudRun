#!/usr/bin/python
#screen.py
#by Luke
#with help from Dad

import pygame;
import random;
import math;

#Setting Constants
BOX_TOP = 0;
BOX_BOTTOM = 768;
BOX_LEFT = 0;
BOX_RIGHT = 1024;
MAX_CHARACTER_SPEED = 1.10;
ROBOT_SPEED = 3;
CREEPBOT_SPEED = 3;
NUMBER_OF_LOCKBOTS = 10;
NUMBER_OF_WILDBOTS = 10;
NUMBER_OF_CREEPBOTS = 10;
NUMBER_OF_NURSEBOTS = 10;
NUMBER_OF_MEDKITS = 10;

#Initialization
 #Screen
screen = pygame.display.set_mode((BOX_RIGHT,BOX_BOTTOM	));
pygame.display.set_caption('Robots game');
 #Random Number Generator
clock = pygame.time.Clock();
random.seed();
 #get the joystick ready
pygame.joystick.init();
if(pygame.joystick.get_count()):
   joystick = pygame.joystick.Joystick(0);
   joystick.init();

#loads
#load robot pictures
creepbotimg = pygame.image.load('images/creepbot.png')
greenbotimg = pygame.image.load('images/greenbot.png');
playerimg = pygame.image.load('images/player.png');
junkimg = pygame.image.load('images/junk.png');
wildbotimg = pygame.image.load('images/wildbot.png');
nursebotimg = pygame.image.load('images/nursebot.png');
medkitimg = pygame.image.load('images/medkit.png');
#load sound effects
pygame.mixer.init();
pygame.mixer.set_num_channels(5)
collisionSound = pygame.mixer.Sound('sounds/collision.wav');
winSound = pygame.mixer.Sound('sounds/win.wav');
loseSound = pygame.mixer.Sound('sounds/lose.wav');
teleportSound = pygame.mixer.Sound('sounds/teleport.wav');
bounceSound = pygame.mixer.Sound('sounds/bounce.wav');
puaseSound = pygame.mixer.Sound('sounds/unpuase.wav');
unpuaseSound = pygame.mixer.Sound('sounds/puase.wav');
#load screen text
pygame.font.init();
scorefont = pygame.font.Font(None,30);
statusFont = pygame.font.Font(None,20)
screenText = "";
screen_text = "";
#game states
keepPlaying = True;
paused = False;




#define functions
   #define classes
class thing:
   def __init__(self):
      pass
   def render(self):
      pass
   def update(self):
      pass
   def collided(self,mob,dist):
      if self.broken and mob.broken:
         return False;
      if((abs(thing.pos_x - self.pos_x) <dist) and (abs(thing.pos_y - self.pos_y) <dist)):
         return True;
      else:
         return False;


class mob:
   def __init__(self):
      pass
   def render(self):
      pass
   def update(self):
      pass
   def collided(self,mob,dist):
      if self.broken and mob.broken:
         return False;
      if((abs(mob.pos_x - self.pos_x) <dist) and (abs(mob.pos_y - self.pos_y) <dist)):
         return True;
      else:
         return False;

class Character(mob):
   def __init__(self):
      self.pos_x = 512;
      self.pos_y = 384;
      self.broken = False;
   def render(self):
      #pygame.draw.circle(screen, (192,192,192),(self.pos_x,self.pos_y),5, 0);
      #screen.blit(playerimg, [self.pos_x-5, self.pos_y-5]);
      if self.broken == True:
         screen.blit(pygame.transform.rotate(playerimg, -90),[self.pos_x-5, self.pos_y-5]);
         #screen.blit(junkimg, [self.pos_x-5, self.pos_y-5]);
      else:
         #self.broken == False;
         screen.blit(playerimg, [self.pos_x-5, self.pos_y-5]);
   def update(self):
      axis0 = joystick.get_axis( 0 );
      axis1 = joystick.get_axis( 1 );
      #interpret the joystick axes
      x_speed =float(axis0*MAX_CHARACTER_SPEED);
      y_speed =float(axis1*MAX_CHARACTER_SPEED);
      self.pos_x += x_speed;
      self.pos_y += y_speed;
      #self.speed = abs(x_speed) + abs(y_speed);
      self.speed = math.sqrt(x_speed*x_speed+y_speed*y_speed);
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
      teleportSound.play();
      #pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/teleportSound'));

class Lockbot(mob):
   def __init__(self):
      self.pos_x = random.randint(BOX_LEFT,BOX_RIGHT);
      self.pos_y = random.randint(BOX_TOP,BOX_BOTTOM);
      self.broken = False;
   def render(self):
      # .. draw a robot
      if self.broken:
         #pygame.draw.rect(screen, (0,0,0),(self.pos_x-5,self.pos_y-5,10,10), 0);
         screen.blit(junkimg, [self.pos_x-5, self.pos_y-5]);
      else:
         #pygame.draw.rect(screen, (255,0,0),(self.pos_x-5,self.pos_y-5,10,10), 0);
         screen.blit(greenbotimg, [self.pos_x-5, self.pos_y-5]);
   def update(self,mob):
      #these robots follow you around
      if(not self.broken):
         if mob.pos_x > self.pos_x:
            self.pos_x += 1; 
         if mob.pos_x < self.pos_x:
            self.pos_x -= 1;
         if mob.pos_y > self.pos_y:
            self.pos_y += 1; 
         if mob.pos_y < self.pos_y:
            self.pos_y -= 1;
#   def collided(self,x,y,dist):
#      if self.broken:
#         return False:
#      if((abs(x - self.pos_x) <dist) and (abs(y - self.pos_y) <dist)):
#         return True;
#      else:
#         return False;

class Wildbot(mob):
   def __init__(self):
      self.pos_x = random.randint(BOX_LEFT,BOX_RIGHT);
      self.pos_y = random.randint(BOX_TOP,BOX_BOTTOM);
      self.velocity = [random.randint(-ROBOT_SPEED,
                                       ROBOT_SPEED),
                       random.randint(-ROBOT_SPEED,
                                       ROBOT_SPEED)];
      #self.velocity = [1, 1];
      self.broken = False;
   def render(self):
      # .. draw a robot
      if self.broken:
         #pygame.draw.rect(screen, (0,0,0),(self.pos_x-5,self.pos_y-5,10,10), 0);
         screen.blit(junkimg, [self.pos_x-5, self.pos_y-5]);
      else:
         #pygame.draw.rect(screen, (128,0,0),(self.pos_x-5,self.pos_y-5,10,10), 0);
         screen.blit(wildbotimg, [self.pos_x-5, self.pos_y-5]);
   def update(self,mob):
      # these robots bounce around and off the walls
      if(not self.broken):
         self.pos_x += self.velocity[0];
         self.pos_y += self.velocity[1];
         if self.pos_x < BOX_LEFT or self.pos_x > BOX_RIGHT:
            self.velocity[0] *= -1;
            self.velocity[1] = random.randint(-ROBOT_SPEED,
                                       ROBOT_SPEED);
            bounceSound.play();
            #pygame.mixer.Channel(1).play(pygame.mixer.Sound('sounds/bounceSound'));
         if self.pos_y < BOX_TOP or self.pos_y > BOX_BOTTOM:
            self.velocity[1] *= -1;
            self.velocity[0] = random.randint(-ROBOT_SPEED,
                                       ROBOT_SPEED);
            bounceSound.play();
            #pygame.mixer.Channel(1).play(pygame.mixer.Sound('sounds/bounceSound'));
#   def collided(self,x,y,dist):
#      if((abs(x - self.pos_x) <dist) and (abs(y - self.pos_y) <dist)):
#         return True;
#      else:
#         return False;

class Creepbot(mob):
   def __init__(self):
      self.pos_x = random.randint(BOX_LEFT,BOX_RIGHT);
      self.pos_y = random.randint(BOX_TOP,BOX_BOTTOM);
      self.broken = False;
   def render(self):
      # .. draw a robot
      if self.broken:
         #pygame.draw.rect(screen, (0,0,0),(self.pos_x-5,self.pos_y-5,10,10), 0);
         screen.blit(junkimg, [self.pos_x-5, self.pos_y-5]);
      else:
         #pygame.draw.rect(screen, (255,0,0),(self.pos_x-5,self.pos_y-5,10,10), 0);
         screen.blit(creepbotimg, [self.pos_x-5, self.pos_y-5]);
   def update(self,mob):
      #these robots follow you around
      if(not self.broken):

         if mob.pos_x > self.pos_x:
            self.pos_x += mob.speed; 
         if mob.pos_x < self.pos_x:
            self.pos_x -= mob.speed;
         if mob.pos_y > self.pos_y:
            self.pos_y += mob.speed; 
         if mob.pos_y < self.pos_y:
            self.pos_y -= mob.speed;
#   def collided(self,x,y,dist):
#      if((abs(x - self.pos_x) <dist) and (abs(y - self.pos_y) <dist)):
#         return True;
#      else:
#         return False;

class Nursebot(mob):
   def __init__(self):
      self.pos_x = random.randint(BOX_LEFT,BOX_RIGHT);
      self.pos_y = random.randint(BOX_TOP,BOX_BOTTOM);
      self.broken = False;
   def render(self):
      # .. draw a robot
      if self.broken:
        #pygame.draw.rect(screen, (0,0,0),(self.pos_x-5,self.pos_y-5,10,10), 0);
         screen.blit(junkimg, [self.pos_x-5, self.pos_y-5]);
      else:
         #pygame.draw.rect(screen, (255,0,0),(self.pos_x-5,self.pos_y-5,10,10), 0);
         screen.blit(nursebotimg, [self.pos_x-5, self.pos_y-5]);
   def update(self,mob):
      #these robots follow you around
      if(not self.broken):
         pass
         if mob.pos_x > self.pos_x:
            self.pos_x += mob.speed; 
         if mob.pos_x < self.pos_x:
            self.pos_x -= mob.speed;
         if mob.pos_y > self.pos_y:
            self.pos_y += mob.speed; 
         if mob.pos_y < self.pos_y:
            self.pos_y -= mob.speed;

class Medkit(thing):
   def __init__(self):
      self.pos_x = random.randint(BOX_LEFT,BOX_RIGHT);
      self.pos_y = random.randint(BOX_TOP,BOX_BOTTOM);
      self.broken = False;
   def render(self):
      # .. draw a medkit
      if self.broken:
         #pygame.draw.rect(screen, (0,0,0),(self.pos_x-5,self.pos_y-5,10,10), 0);
         screen.blit(junkimg, [self.pos_x-5, self.pos_y-5]);
      else:
         #pygame.draw.rect(screen, (255,0,0),(self.pos_x-5,self.pos_y-5,10,10), 0);
         screen.blit(medkitimg, [self.pos_x-5, self.pos_y-5]);
   def update(self):
      pass

#setting up the game
def reset_game():
   global keepPlaying;
   global player
   global moblist;
   global thinglist;
   player = Character();
   moblist = [];
   moblist = [Lockbot() for count in range(NUMBER_OF_LOCKBOTS)];
   moblist += [Wildbot() for count in range(NUMBER_OF_WILDBOTS)];
   moblist += [Creepbot() for count in range(NUMBER_OF_CREEPBOTS)];
   moblist += [Nursebot() for count in range(NUMBER_OF_NURSEBOTS)];

   thinglist = [];
   thinglist += [Medkit() for count in range(NUMBER_OF_MEDKITS)];
   keepPlaying = True;
 
#pause function
def toggle_pause():
   global paused;
   if paused == True:
      paused = False;
      unpuaseSound.play();
      screen_text = ""
   else:
      paused = True;
      puaseSound.play();
      screen_text = "PAUSED";
   print "paused is toggled";

def play_level():
   global keepPlaying;
   global player
   global moblist;
   global thinglist;
   global screen_text;
   while keepPlaying:
      clock.tick(1000);
      #Handle Events (key press)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            keepPlaying = False;
            screenText = "GAME OVER:  Quitter";
         if event.type == pygame.JOYBUTTONDOWN:
            if not paused:
               if(joystick.get_button( 10 )):
                  player.tp_player_safe();
            if(joystick.get_button( 8 )):
               reset_game();
            if(joystick.get_button( 0 )):
               toggle_pause();
               if paused == True:
                  screen_text = "PAUSED";
               if paused == False:
                  screen_text = "";
         if not hasattr(event, 'key'):
            continue;
         if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            keepPlaying = False;
            screenText = "GAME OVER:  Quitter";
         if event.key == pygame.K_p:
            toggle_pause;

      #Read the Joystick
#      axis0 = joystick.get_axis( 0 );
#      axis1 = joystick.get_axis( 1 );
#      axis2 = joystick.get_axis( 2 );
#      axis3 = joystick.get_axis( 3 );
      if(joystick.get_button( 9 )):
         keepPlaying = False;
         screenText = "GAME OVER:  Quitter";

      #Game Logic
      aliveBots = 0;
      if not paused:
         player.update();
         #move class robots and check for collisions
      for i in range(len(moblist)):
         if not paused:
            moblist[i].update(player);
             #Check for collistion with Player
         if(moblist[i].collided(player,10)):
            player.broken = True;
            keepPlaying = False;
            loseSound.play();
            #pygame.mixer.Channel(2).play(pygame.mixer.Sound('sounds/loseSound'));
            print "you died";
            screenText = "You died   GAME OVER";
         #Check for collisions with other Bots
         for j in range(i+1,len(moblist)):
            if(moblist[i].collided(moblist[j],10)):
               moblist[i].broken=True;
               moblist[j].broken=True;
               collisionSound.play();
               #pygame.mixer.Channel(3).play(pygame.mixer.Sound('sounds/collisionSound'));
         if moblist[i].broken == False:
            aliveBots = aliveBots + 1;
      if aliveBots == 0:
          keepPlaying = False;
          screenText = "You Win!"
      
               

      #Draw the screen
      screen.fill((12,0,128));
      player.render();
      for robot in moblist:
         robot.render();
      for thing in thinglist:
         robot.render();
         thing.render();
      if keepPlaying == False:
         gameOverText = scorefont.render(screenText, 1, (255,255,255));
         screen.blit(gameOverText, [412,390]);
#         game_over_text = scorefont.render(, 1, (255,255,255));
#         screen.blit(game_over_text, [512,394]);
      if keepPlaying == True:
         KeepPlayingText = scorefont.render(screen_text, 1, (255,255,255));
         screen.blit(KeepPlayingText, [412,390]);
      botCountText = statusFont.render("Bots: "+str(aliveBots),1,(255,255,255));
      screen.blit(botCountText, [40,30]);
      pygame.display.flip();
      print "AliveBots: " + str(aliveBots);
   pygame.time.wait(1000);
   #render (str"game over", 1, (0,0,0));
   print "Game over"

def quit_menu():
   global screen_text;
   KeepPlayingText = scorefont.render("Do you want to play again?", 1, (255,255,255));
   screen.blit(KeepPlayingText, [400,415]);
   pygame.display.flip();
   pygame.time.wait(1000)
   KeepPlayingText = scorefont.render("(if yes press y if no press n)", 1, (255,255,255));
   screen.blit(KeepPlayingText, [400,435]);
#   screen_text = "do you want to play again?";
   pygame.display.flip();
   pygame.time.wait(1000);
   waiting_for_user = True;
   while waiting_for_user:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            keepPlaying = False;
            screenText = "GAME OVER:  Quitter";
         if not hasattr(event, 'key'):
            continue;
         if event.key == pygame.K_y:
            waiting_for_user = False;
            return True;
         if event.key == pygame.K_n:
            waiting_for_user = False;
            return False;



#Start the game
playing = True;
while playing:
   reset_game();
   play_level();
   playing = quit_menu();
