def gameRules():
    print("PHASE ONE:")
    print("   The game is for two players, that take turns placing stones on the board.")
    print("   The players start with 9 stones each.")
    print("   The goal is to take all of the opponents stones out of the game.")
    print("   Stones can be taken from the board when a row of three is created by the opponent.")
    print("   Rows can only be straight (not around corners) and have to be along the lines on the board.")
    print("   Stones within a row cannot be taken away.")
    print("PHASE TWO:")
    print("   When all stones are placed, you are able to move stones on the board.")
    print("   A stone can only be moved to a connected position.")
    print("   Stones within a row cannot be moved")
    print("PHASE 3:")
    print("   When a player has 3 stones left, they can jump instead of move.")
    print("   Stones are not stolen from the board when a row of three is created.")
    print("   Stones within a row cannot be taken.")
    print("WIN CONDITION:")
    print("   The player with 2 stones left loses the game.")
    print("OR")
    print("   The player who is unable to move any of their stones loses the game")

    getBack = input("Press [Q] to go back\n")

    while (getBack not in ["Q", "q"]):
        print("Invalid input!")
        getBack = input("Press [Q] to go back\n")

    if (getBack == "Q" or "q"):
        return 0
