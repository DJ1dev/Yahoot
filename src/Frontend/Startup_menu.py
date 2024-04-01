import sys
from pathlib import Path
root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(root_path))


from Backend import useraccount, text_format
from time import sleep

import Main_menu


def Login_page():                                                                               #handles The log in page
    print("\n[---Log in---]")

    username = input("Username :\t")
    password = input("Password :\t")
    
    if useraccount.Account_Verify(text_format.admin_formatting(username), password) == True:
        print('Successfull Login')
        Main_menu.logged_Menu(username)
    else:
        print('Invalid Username or Password, Please try again or Sign up')


def SignUp_page():                                                                              #handles The Sign up page
    print("\n[---Sign up---]")

    username = input("Username :\t")
    while True:
        password = input("Password :\t")
        if len(password) >= 5:
            if useraccount.Add_Accounts(text_format.admin_formatting(username), password) == True:
                print('Succesfully Registered')
                break
        else:
            print('The password is too short \n')
    
    


def startmenu():
    while True:
        operation_choice = input("\n[---Menu---]\n1: Log In\n2: Sign Up\n3: Exit\nAnswer:\t")
        if operation_choice == "1" or operation_choice ==  "Log in":
            Login_page()
            break
        elif operation_choice == "2" or operation_choice ==  "Sign up":
            SignUp_page()
            break
        elif operation_choice == "3" or operation_choice ==  "Exit":
            return False
        else:
            print("Invalid option, please enter the corresponding option's number")


print("Welcome Student")
sleep(0.5)
print("Please Choose an option listed below")
sleep(0.5)

while True:
    if startmenu() == False:
        print("Come Back Soon")
        break
