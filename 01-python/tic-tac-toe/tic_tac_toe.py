import re
import random

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    # return self.board.count(None) == 0
    options=[self.board.count(None) == 0,
    self.board[0:3].count(self.board[0])==3 and self.board[0] is not None,
    self.board[3:6].count(self.board[3])==3 and self.board[3] is not None,
    self.board[6:].count(self.board[6])==3 and self.board[6] is not None,
    self.board[0::3].count(self.board[0])==3 and self.board[0] is not None,
    self.board[1::3].count(self.board[1])==3 and self.board[1] is not None,
    self.board[2::3].count(self.board[2])==3 and self.board[2] is not None,
    self.board[0::4].count(self.board[0])==3 and self.board[0] is not None,
    self.board[2::2].count(self.board[2])==3 and self.board[2] is not None]
    finished=any(options)
    try:
      index=options[1:].index(True)
      if index in [0,3,6]:
        self.winner=self.board[0]
      elif  index in [1]:
        self.winner=self.board[3]
      elif index in [2]:
        self.winner=self.board[6]
      elif index in [4]:
        self.winner=self.board[1];
      else:
        self.winner=self.board[2]
      return finished
    except Exception as e:
      return finished
    
    return any(options)
    
  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self): # TODO: Finish this function by making the machine choose a random cell (use random module)
    # for i, cell in enumerate(self.board):
    #   if cell is None:
    #     self.board[i] = _MACHINE_SYMBOL
    #     break
    options=[idx for (idx,x) in enumerate(self.board) if x is None]
    self.board[random.choice(options)]=_MACHINE_SYMBOL
    

  def format_board(self):
    row0 = "|".join(list(map(lambda c: " " if c is None else c, self.board[0:3])))
    row1 = "|".join(list(map(lambda c: " " if c is None else c, self.board[3:6])))
    row2 = "|".join(list(map(lambda c: " " if c is None else c, self.board[6:9])))

    return "\n".join([row0, row1, row2])

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self): # TODO: Finish this function in order to print the result based on the *winner*
    if self.winner is None:
      print("The game is tied!")
    elif self.winner == _PLAYER_SYMBOL:
      print("You win!")
    else:
      print("Loser!")
