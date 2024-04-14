# Import necessary modules from a backend package and specific games
from Backend import useraccount, Hangman, text_format, Wordmatch

def Play_mode(username):
    # Prompt the user to select a game mode
    Game_Choice = input("\nSelect The Game Mode:\n1: Hangman\n2: Word Matching\nAnswer:\t")
    
    # Format the user's choice to ensure it matches expected values
    if text_format.admin_formatting(Game_Choice) == '1':
        # Start the Hangman game and store the result
        game_result = Hangman.Setup()
        # If the result indicates a win, manage the user's points
        if game_result[0] == True:
            useraccount.point_management(username, game_result[1])
    elif text_format.admin_formatting(Game_Choice) == '2':
        # Start the Word Matching game and store the result
        game_result = Wordmatch.Setup()
        # If the result indicates a win, manage the user's points
        if game_result[0] == True:
            useraccount.point_management(username, game_result[1])
    else:
        # Handle invalid inputs for game choice
        print("Invalid Input, please try again")

def Leaderboard():
    # Display the leaderboard header
    print("\n[---Leaderboard---]")
    # Retrieve and print user account details from the backend
    for x in useraccount.Scan_Accounts():
        print(x[0].capitalize(), x[1])  # Display user names with scores

def logged_Menu(username):
    # Welcome the logged in user
    print('Hello,', username)
    while True:
        # Display the main menu options
        operation_choice = input("\n[---Main Menu---]\n1: Leaderboard\n2: Play\n3: Log Out\nAnswer:\t")
        
        # Navigation based on user input
        if operation_choice == '1' or operation_choice.lower() == 'leaderboard':
            Leaderboard()
        elif operation_choice == '2' or operation_choice.lower() == 'play':
            Play_mode(username)
        elif operation_choice == '3' or operation_choice.lower() == 'log out':
            break  # Exit the loop to log out
        else:
            # Handle invalid menu options
            print("Invalid option, please enter the corresponding option's number")
