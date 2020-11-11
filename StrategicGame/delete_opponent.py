import sequence as s

# Description: Presents all valid deletes and asks the user to delete one
# their opponent's stones. Keeps asking until valid input is given.


def delete_opp_stone(player, board, position):
    invalid_moves = []
    valid_moves = []

    if (player == "W "):
        opp_player = "B "

        for m in range(len(board)):
            if (board[m] == opp_player):
                check_opp_player_seq, opp_player_seq = s.check_sequence(
                    opp_player, m+1, board)
                if check_opp_player_seq:
                    invalid_moves = invalid_moves + opp_player_seq

        if (len(invalid_moves) >= 3):
            print("The valid moves for deleting B are:")
            for i in range(len(board)):
                if (i not in invalid_moves):
                    if (board[i] == opp_player):
                        print(i + 1)
                        valid_moves.append(i+1)
            if(len(invalid_moves)<1):
              print ("No opponent stone can be deleted!")

            else:
              position = input("Input the position for deleting B:")
              valid = False

              while not valid:
                  while int(position) not in valid_moves:
                      position = input("Input the position for deleting B:")
                  position = int(position) - 1

                  if (board[position] == opp_player):
                      valid = True
                  else:
                      print("You can't go there. Go again.")
              board[position] = "**"

        else:
            print("The valid moves for deleting B are:")
            for i in range(len(board)):
                if (board[i] == opp_player):
                    print(i + 1)
                    valid_moves.append(i+1)
            position = input("Input the position for deleting B:")
            valid = False

            while not valid:
                while int(position) not in valid_moves:
                    position = input("Input the position for deleting B:")
                position = int(position) - 1

                if (board[position] == opp_player):
                    valid = True
                else:
                    print("You can't go there. Go again.")
            board[position] = "**"

    else:
        opp_player = "W "
        for m in range(len(board)):
            if (board[m] == opp_player):
                check_opp_player_seq, opp_player_seq = s.check_sequence(
                    opp_player, m+1, board)
                if check_opp_player_seq:
                    invalid_moves = invalid_moves + opp_player_seq

        if (len(invalid_moves) >= 3):

            print("The valid moves for deleting W are:")
            for i in range(len(board)):
                if (i not in invalid_moves):
                    if (board[i] == opp_player):
                        print(i + 1)
                        valid_moves.append(i+1)
            
            if (len(valid_moves)<1):
              print ("No opponent stone can be deleted!")
            else:

              position = input("Input the position for deleting W:")
              valid = False

              while not valid:
                  while int(position) not in valid_moves:
                      position = input("Input the position for deleting W:")
                  position = int(position) - 1

                  if (board[position] == opp_player):
                      valid = True
                  else:
                      print("You can't go there. Go again.")
              board[position] = "**"

        else:
            print("The valid moves for deleting W are:")
            for i in range(len(board)):
                if (board[i] == opp_player):
                    print(i + 1)
                    valid_moves.append(i+1)
            position = input("Input the position for deleting W:")
            valid = False

            while not valid:
                while int(position) not in valid_moves:
                    position = input("Input the position for deleting W:")
                position = int(position) - 1

                if (board[position] == opp_player):
                    valid = True
                else:
                    print("You can't go there. Go again.")

            board[position] = "**"
