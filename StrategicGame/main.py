
import game_platform
import project_se as comm
import projectse.game_manager as game_manager
import playAIGame

comm_part = game_manager.GameManager()

# Description: Prints a menu to standard output
# and acts on input from the user
def main_menu_func():

    #130.242.110.181
    ip = input('please enter the servers IP address: ')
    comm_part.connect(ip)
    menu_callback = True
    playAIGame.init(comm_part)
    while (menu_callback == True):
        print("\n"+game_platform.welcomeMsg)
        print("Mode of the Game:\n[P] 1 vs 1 \n[T] Tournament\n[Q] Quit")
        choice = input("Please enter the mode of Game: ")
        if (choice == "P" or choice == "p"):
            menu_callback = game_platform.play_game(config=False) is None
            continue
        if (choice == "T" or choice == "t"):
            print("Tournament Mode")
            comm.ProjectSE().init()

        if (choice == "Q" or choice == "q"):
            quit_game()
        print(
            "Invalid input!\nMode of the Game:\n[P] 1 vs 1 \n[T] Tournament\n[Q] Quit")
# Description: Exits game if input is yes, else
# returns back to main menu


def quit_game():
    areYouSure = input("Are you sure you want to quit?\n[Y]es or [N]o?\n")
    global comm_part
    if (areYouSure == ('y' or 'Y')):
        comm_part.close()
        exit()


main_menu_func()
