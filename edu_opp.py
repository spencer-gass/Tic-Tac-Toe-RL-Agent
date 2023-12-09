from opp import opp
from random import random 
from copy import deepcopy
import json

class edu_opp(opp):
   def __init__(self, game_board, sym, fname=None):
      opp.__init__(self, game_board, sym)
      self.fname = fname
      self._restore_state()
      self.opts = list()
      self.turn_stack = list()
      self.wonder = 1.0
      self.learning_rate = 1.0
      self.win_val = 1.0
      self.loss_val = -1.0
      self.draw_val = 0.0
      self.game_cnt = 0
      self.fname = fname
      
   def take_turn(self):
      self.opts = list()
      self._enum_options()
      self._eval_options()
      if random() < self.wonder:
         opt = self._rand_option()
      else:
         opt = self._sel_option()
      self._commit_opt(opt)

   def _enum_options(self):
      for r in range(3):
         for c in range(3):
            if self.game_board.is_empty(r,c):
               opt = turn_option()
               opt.set_row(r)
               opt.set_col(c)
               self._make_gb_str(opt)
               self.opts.append(opt)

   def _make_gb_str(self, opt):
      gb = deepcopy(self.game_board)
      gb.place_sym(opt.get_row(), opt.get_col(), self.sym)
      gb_str = self._format_gb_str(gb)
      opt.set_gb_str(gb_str)

   def _format_gb_str(self, gb):
      b = gb.get_board()
      gb_str = str()
      for r in range(3):
         for c in range(3):
            if b[r][c] == None:
               gb_str += 'e' # empty
            elif b[r][c] == self.sym:
               gb_str += 's' # self
            else:
               gb_str += 'o' # opponent
      return gb_str

   def _eval_options(self):
      for o in self.opts:
         val = self._get_value(o.get_gb_str())
         o.set_val(val)

   def _sel_option(self):
      self.opts.sort(reverse=True)
      best = list()
      mv = self.opts[0].get_val()
      for o in self.opts:
         if o.get_val() == mv:
            best.append(o)
      i = int(len(best) * random())
      return best[i]

   def _rand_option(self):
      i = int(random() * len(self.opts))
      return self.opts[i]

   def _commit_opt(self, opt):
      self.game_board.place_sym(opt.get_row(), opt.get_col(), self.sym)
      self.turn_stack.append(opt.get_gb_str())

   def accept_win(self):
      self._game_ended()
      self._back_prop_value(self.win_val)
      self.turn_stack = list()

   def accept_loss(self):
      self._game_ended()
      self._back_prop_value(self.loss_val)
      self.turn_stack = list()

   def accept_draw(self):
      self._game_ended()
      self._back_prop_value(self.draw_val)
      self.turn_stack = list()

   def _game_ended(self):
      self.game_cnt += 1
      if self.game_cnt < 100000:
         self.wonder = 1.0 - (float(self.game_cnt)/100000.0)
         self.learning_rate = 1.0 - (float(self.game_cnt)/100000.0) 

   def _back_prop_value(self,val):
      self.game_cnt += 1
      self.turn_stack.reverse()
      for t in self.turn_stack:
         self._update_value(t,val)
         val = val/2.0

   def _restore_state(self):
      try: 
         f = open(self.fname)
         d = f.read()
         self.value_table = json.loads(d)
      except Exception:
         print('edu opp: creating new value table')
         self.value_table = dict()

      if 'game_cnt' in self.value_table:
         self.game_cnt = self.value_table['game_cnt']
      else:
         self.game_cnt = 0
   
   def save(self):
      if self.fname:
         self.value_table['game_cnt'] = self.game_cnt
         d = json.dumps(self.value_table)
         try: 
            f = open(self.fname, 'w')
            f.write(d)
            f.close()
         except Exception:
            print('edu opp: unable to save value table')
            return
      else:
         print('edu_opp: No file name. Not saving.')

   def _get_value(self, gb_str):
      if not gb_str in self.value_table:
         self.value_table[gb_str] = 0.0
      return self.value_table[gb_str]

   def _update_value(self, gb_str, update):
      self.value_table[gb_str] = self.learning_rate * update + (1-self.learning_rate) * self.value_table[gb_str]
        
class turn_option():
   def __init__(self):
      self.val = None
      self.row = None
      self.col = None
      self.gb_str = None

   def get_val(self):
      return self.val

   def get_row(self):
      return self.row

   def get_col(self):
      return self.col

   def get_gb_str(self):
      return self.gb_str

   def set_val(self, v):
      self.val = v

   def set_row(self, r):
      self.row = r

   def set_col(self, c):
      self.col = c

   def set_gb_str(self, s):
      self.gb_str = s

   def __lt__(self, other):
      if self.val < other.get_val():
         return True
      else:
         return False
