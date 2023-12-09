# Tic Tac Toe RL angent

Tic Tac Toe is a fun and simple game involving two players taking turns placing Xs or Os on a 3x3 grid
The first to get three of thier symbol in a row wins. If no one gets three in a row the game is a draw.

Many kids learn the simple rules of Tic Tac Toe and begin to play with their friends. Over time they
observe patterns and devise stratagies to improve their chance of winning. Given enough time however
the children will eventually learn that it is always possible to force a draw to avoid losing. 
Consequentially two knowlegable Tic Tac Toe players will always end in a draw and the joy of the game
will be lost. 

The fact that Tic Tac Toe is a simple but not trivial game where the change in game outcomes as a function
of learned skill is know makes it a good game to use for a basic RL agent experiment. 

rand_opp:
   selects a free space to place it's symbol uniformly randomly.
   useful for comparison and inital testing

edu_opp1: 
   learn values of each of the < 3^9 valid boards by back propegating values through winning, losing and draw sequences
   no extra structure imposed on the agent. just board realizations and values

edu_opp2:
   create or learn a function to equate board realizations that are transpositions or rotations of eachother to reduce
   the number of games needed to play effectivly.

expectations:
   rand_opp vs rand_opp
      wins should be roughly 50-50
      wins can come early in the tree and should be more likely that draws

   rand_opp vs untrained edu_opp
      should exibit similar behavior as rand_opp vs rand_opp

   rand_opp vs traind edu_opp
      edu_opp should win the majority of the time since it can reach winning states faster
      loses should approach zero since edu_opp should have learned to block loses states
      some draws should still be present since the rand_opp could get lucky and block a edu_opp win

   edu_opp vs edu_opp
      should approach 100% draws



