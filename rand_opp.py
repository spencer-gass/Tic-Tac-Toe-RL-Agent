
from random import random 
from opp import opp

class rand_opp(opp):
   def __init__(self, game_board, sym):
      opp.__init__(self, game_board, sym)

   def take_turn(self):
      if self.game_board.get_winner() == None:
         r = int(3.0 * random())
         c = int(3.0 * random())
         while not self.game_board.is_empty(r,c):
            r = int(3.0 * random())
            c = int(3.0 * random())
         
         self.game_board.place_sym(r,c,self.sym)


