#Description: Checks if one of the players have won, this happens when one player only have 2 stones left
def check_winning_condition(board):
  count_W_board = 0
  count_B_board = 0

  for i in board:
        if (i == "W "):
            count_W_board = count_W_board + 1
        if (i == "B "):
            count_B_board = count_B_board + 1

  if(count_W_board < 3):
    print ("B is the winner!\n")
    return "Black"
  elif(count_B_board <3):
    print ("W is the winner!\n")
    return "White"
  else:
    return None
