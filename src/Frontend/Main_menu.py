from Backend import useraccount

def Play_mode():
    print('Playing')

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