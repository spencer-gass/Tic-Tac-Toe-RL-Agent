from random import random 

class game_board():
   def __init__(self):
      self.board = [[None]*3,[None]*3,[None]*3]
      self.draw_sym = 'draw'

   def clear_board(self):
      self.board = [[None]*3,[None]*3,[None]*3]

   def is_empty(self, row, col):
      if self.board[row][col] == None:
         return True
      else: 
         return False

   def get_board(self):
      return self.board

   def get_draw_sym(self):
      return self.draw_sym

   def get_winner(self):
      # check cols and rows
      for i in range(3):
         if self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2] and self.board[i][0] != None:
            return self.board[i][0]
         if self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i] and self.board[0][i] != None:
            return self.board[0][i]

      # check diags
      if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[0][0] != None:
         return self.board[0][0]
      if self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0] and self.board[0][2] != None:
         return self.board[0][2]

      for i in range(3):
         if None in self.board[i]:
            return None

      return self.draw_sym

   def place_sym(self, row, col, sym):
      self.board[row][col] = sym

   def __str__(self):
      b_str = "---\n"
      for r in range(3):
         row = ""
         for c in range(3):
            if self.board[r][c] == None:
               row += ' '
            else:
               row += self.board[r][c]
         b_str += row + '\n'
      return b_str + '---\n'

class game():
   def __init__(self, gb, p1, p2):
      self.gb = gb
      self.players = [p1,p2]
      self.clear_score()

   def get_score(self):
      return (self.wins[0], self.wins[1], self.draws)

   def print_score(self):
      print('---------------')
      print('p1 wins', self.wins[0])
      print('p2 wins', self.wins[1])
      print('draws  ', self.draws)
      print()

   def clear_score(self):
      self.wins = [0, 0]
      self.draws = 0

   def play_one_game(self, en_print=False):
      if random() < 0.5:
         turn_ptr = 0
      else: 
         turn_ptr = 1

      while self.gb.get_winner() == None:
         turn_ptr ^= 1
         self.players[turn_ptr].take_turn()
         if en_print: print(self.gb)

      if self.gb.get_winner() == self.gb.get_draw_sym():
         self.draws += 1
         self.players[turn_ptr].accept_draw()
         self.players[turn_ptr^1].accept_draw()
      else:
         self.wins[turn_ptr] += 1
         self.players[turn_ptr].accept_win()
         self.players[turn_ptr^1].accept_loss()
         
      if en_print:
         print(self.gb)
         print('Winner: ', self.gb.get_winner())

   def play_n_games(self, n):
      for g in range(n):
         self.play_one_game()
         self.gb.clear_board()

