from random import random 
from rand_opp import rand_opp
from edu_opp import edu_opp
from game import game_board, game

if __name__ == '__main__':
   gb = game_board()
   p1 = edu_opp(gb,'X') #, 'new_value_table.txt')
   p2 = edu_opp(gb,'O')
   g = game(gb, p1, p2)
   
   for i in range(10):
      g.play_n_games(10000)
      g.print_score()
      g.clear_score()

#   p1.save()

   print()
   for i in range(9):
      s = i*'e' + 's' + (8-i)*'e'
      print(s,p1.value_table[s])
