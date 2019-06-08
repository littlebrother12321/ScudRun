#!/usr/bin/python

import random
import os
import curses

def intro(win):
    #Game Message
    win.addstr("\nYou have 20 turns to guess the position of a 1 x 1 battleship\n");
    win.addstr("Move the cursor with the arrows. SPACE to fire\n");

class Space:
    def __init__(self):
        self.isBoat = False;
        self.cleared = False;

class Board:
    def __init__(self,rows,cols):
         self.rows = rows
         self.cols = cols
         self.spaces = []
         self.disp = []
         for x in range(rows):
             self.spaces.append([Space() for count in range(cols)])
             self.disp.append(['O'] * cols)

class Boat:
    def __init__(self, size, name):
        self.size = size
        placed = False
    def checkPlacement(self,board):
        #TODO: See if the boad is contained within the board
        pass
    def checkPlacement(self,boat):
        #TODO: See if the boat conflicts with other boats
        pass
    def autoPlace(self,boats,board):
        self.row = random.randint(0,board.rows -1)
        self.col = random.randint(0,board.cols -1)
        #Check for fit on board
        self.checkPlacement(board)
        #check for conflict with other boats
        for boat in boats:
            self.checkPlacement(boat)
        #Indicate occupation of spaces on the board
        board.spaces[self.row][self.col].isBoat = True;

class Game:
    #def rand_col(self):
    #    return random.randint(0, self.board.cols - 1)
    #def rand_row(self):
    #    return random.randint(0, self.board.rows - 1)
    def shot(self,row,col):
        #if row == self.shipRow and col == self.shipCol:
        if self.board.spaces[row][col].isBoat:
           self.board.disp[row][col] = '#'
           return True
        else:
           self.board.disp[row][col] = chr(46)
           return False
    def createBoats(self):
        self.allBoats = []
        self.allBoats.append(Boat(5,"Carrier"))
        self.allBoats.append(Boat(4,"Battleship"))
        self.allBoats.append(Boat(3,"Cruiser"))
        self.allBoats.append(Boat(3,"Submarine"))
        self.allBoats.append(Boat(2,"PT Boat"))
    def placeBoatsAuto(self):
        #place boats on board
        self.activeBoats = [];
        for boat in self.allBoats:
            boat.autoPlace(self.activeBoats,self.board)
            self.activeBoats.append(boat)
    def placeBoats(self):
        self.placeBoatsAuto()
        #TODO: branch for manual boat placement
        #Might require the interface to place them, or check
    def __init__(self):
        self.board = Board(10,10)
        self.createBoats()
        self.placeBoats()


class GameInterface:
    def __init__(self,theGame):
        self.cursor = [4,4];
        self.height = theGame.board.rows
        self.width = theGame.board.cols
    def cursorHorz(self,right):
        if(right and self.cursor[1] < self.width -1):
           self.cursor[1] = self.cursor[1] + 1;
        if(not right and self.cursor[1] > 0):
           self.cursor[1] = self.cursor[1] - 1;
        print self.cursor;
    def cursorVert(self,up):
        if(up and self.cursor[0] > 0):
           self.cursor[0] = self.cursor[0] - 1;
        if(not up and self.cursor[0] < self.height -1):
           self.cursor[0] = self.cursor[0] + 1;
        print self.cursor;
    def printBoard(self,win):
        win.clear();
        for row in range(theGame.board.rows):
            if(row == self.cursor[0]):
                if(0 == self.cursor[1]):
                    win.addstr(" ".join(theGame.board.disp[row][0:self.cursor[1]]) + "[" + theGame.board.disp[row][self.cursor[1]] + "]" + " ".join(theGame.board.disp[row][self.cursor[1]+1:len(theGame.board.disp[row])]) + "\n")
                else:
                    win.addstr(" " + " ".join(theGame.board.disp[row][0:self.cursor[1]]) + "[" + theGame.board.disp[row][self.cursor[1]] + "]" + " ".join(theGame.board.disp[row][self.cursor[1]+1:len(theGame.board.disp[row])]) + "\n")
            else:
                win.addstr(" " + " ".join(theGame.board.disp[row]) + "\n");
        win.addstr(str(self.cursor[0]) + " "+ str(self.cursor[1]) + "\n")
        #print row;
        #print cur;
        #print cur[0];
        #print cur[1];

#get input from the user
def getInput(rowOrCol):
   val = -1;
   while(val < 0 or val > 10):
      val = input(rowOrCol);
   return val - 1;
#Get user Column



#Display Board

#for turn in range(20):
#   print "Turn: " + str(turn + 1);
#   guessRow = getInput("row: ");
#   guessCol = getInput("col: ");
#   board[guessRow][guessCol] = 'x';
#   printBoard(board,cursor);

theGame = Game();
iface = GameInterface(theGame);


def main(win):
    win.nodelay(True)
    key=""
    win.clear()
    iface.printBoard(win)
    intro(win)
    #win.addstr("Detected key:")
    while 1:
        try:
            key = win.getkey()
            if key == os.linesep or key == 'q':
                break;
            if key == "KEY_RIGHT":
                 #pass
                 try:
                     iface.cursorHorz(True)
                 except Exception as e:
                     win.addstr(str(e))
                 iface.printBoard(win)
            if key == "KEY_LEFT":
                 iface.cursorHorz(False)
                 iface.printBoard(win)
            if key == "KEY_UP":
                 try:
                     iface.cursorVert(True)
                 except Exception as e:
                     win.addstr(str(e))
                 iface.printBoard(win)
            if key == "KEY_DOWN":
                 iface.cursorVert(False)
                 iface.printBoard(win)
            if key == " ":
                 shotstr = "FIRE!\n"
                 if(theGame.shot(iface.cursor[0],iface.cursor[1])):
                     shotstr = "****Hit!*****\n"
                 else:
                     shotstr =  "----Miss!---\n"
                 iface.printBoard(win)
                 win.addstr(shotstr)
            #win.addstr(key + "\n")
            #win.addstr("0 "+ str(iface.cursor[0]) + "\n")
            #win.addstr("1 "+ str(iface.cursor[1]) + "\n")
            #else:
            #    win.clear()
            #    win.addstr("Detected key: ")
            #    win.addstr(str(key))
        except Exception as e:
            pass

curses.wrapper(main)
