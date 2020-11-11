import game_platform as gp

# Description: Handles the logic for moving stones and writes information


def move_stone_third_phase(player, board):

    print(player + "'s turn.")

    if (player == "W "):
        valid_stones_W = []

        print("Positions having W: ")
        for i in range(len(board)):
            #count_empty = 0
            if (board[i] == player):
                print (i+1)
                valid_stones_W.append(i)

        stone_to_be_moved = input(
            "Please enter the position of W that is to be moved:")

        valid = False
        while not valid:
            while int(stone_to_be_moved)-1 not in valid_stones_W:
                stone_to_be_moved = input(
                    "Please enter the position of W that is to be moved:")
            valid = True

        print("Valid nodes to move the stone are:")
        valid_nodes_W = []
        for i in range(len(board)):
          if (board[i] == "**"):
            print (i+1)
            valid_nodes_W.append(i+1)


        position_move_W = input("Enter the position to move W:")

        valid = False
        while not valid:
            while int(position_move_W) not in valid_nodes_W:
                position_move_W = input("Enter the position to move W:")
            if (board[int(position_move_W)-1] == "**"):
                valid = True
            else:
                print("You can't go there. Go again.")
        board[int(position_move_W)-1] = player
        board[int(stone_to_be_moved)-1] = "**"
        return int(position_move_W)

    if (player == "B "):
        valid_stones_B = []

        print("Positions having B: ")
        for i in range(len(board)):
            count_empty = 0
            if (board[i] == player):
              print (i+1)
              valid_stones_B.append(i)
                
        stone_to_be_moved = input(
            "Please enter the position of B that is to be moved:")

        valid = False
        while not valid:
            while int(stone_to_be_moved)-1 not in valid_stones_B:
                stone_to_be_moved = input(
                    "Please enter the position of B that is to be moved:")
            valid = True

        print("Valid nodes to move the stone are:")
        valid_nodes_B = []
        for i in range(len(board)):
          if (board[i] == "**"):
            print (i+1)
            valid_nodes_B.append(i)
            

        position_move_B = input("Enter the position to move B:")

        valid = False
        while not valid:
            while int(position_move_B) not in valid_nodes_B:
                position_move_B = input("Enter the position to move B:")
            if (board[int(position_move_B)-1] == "**"):
                valid = True
            else:
                print("You can't go there. Go again.")
        board[int(position_move_B)-1] = player
        board[int(stone_to_be_moved)-1] = "**"
        return int(position_move_B)
