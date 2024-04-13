from Backend import useraccount, Hangman, text_format

def Play_mode():
    Game_Choice = input("\nSelect The Game Mode:\n1: Hangman\n2: Word Matching\nAnswer:\t")
    if text_format.admin_formatting(Game_Choice) == '1':
        game_result = Hangman.Setup()
        if game_result[0] == True:
            
    elif text_format.admin_formatting(Game_Choice) == '2':
        pass
    else:
        print("Invalid Input, please try again")

def Leaderboard():
    print("\n[---Leaderboard---]")
    for x in useraccount.Scan_Accounts():
        print(x[0].capitalize(),x[1])

def logged_Menu(username):
    print('Hello,' , username)
    while True:
        operation_choice = input("\n[---Main Menu---]\n1: Leaderboard\n2: Play\n3: Log Out\nAnswer:\t")
        if operation_choice == '1' or operation_choice == 'Leaderboard':
            Leaderboard()
        elif operation_choice == '2' or operation_choice == 'Play':
            Play_mode()
        elif operation_choice == '3' or operation_choice == 'Log Out':
            break
        else:
            print("Invalid option, please enter the corresponding option's number")