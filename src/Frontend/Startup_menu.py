# import functions for python file connections
import sys
from pathlib import Path

# Get the parent directory of the current file (i.e., the parent directory of the script)
root_path = Path(__file__).resolve().parent.parent

# Add the parent directory to the Python path
sys.path.append(str(root_path))

# Import necessary modules from the Backend package
from Backend import useraccount, text_format

# Import Main_menu module
import Main_menu

# Import sleep function from the time module
from time import sleep

# Define a function for handling the login page
def Login_page():
    print("\n[---Log in---]")

    # Prompt user for username and password
    username = input("Username :\t")
    password = input("Password :\t")
    
    # Verify the entered credentials
    if useraccount.Account_Verify(text_format.admin_formatting(username), password) == True:
        print('Successful Login')
        # Redirect to the logged-in menu
        Main_menu.logged_Menu(text_format.admin_formatting(username))
    else:
        print('Invalid Username or Password, Please try again or Sign up')

# Define a function for handling the signup page
def SignUp_page():
    print("\n[---Sign up---]")

    # Prompt user for username and password
    username = input("Username :\t")
    while True:
        password = input("Password :\t")
        if len(password) >= 5:
            if useraccount.Add_Accounts(text_format.admin_formatting(username), password) == True:
                print('Successfully Registered')
                break
        else:
            print('The password is too short \n')

# Define a function to display the start menu and handle user choices
def startmenu():
    while True:
        operation_choice = input("\n[---Menu---]\n1: Log In\n2: Sign Up\n3: Exit\nAnswer:\t")
        if operation_choice == "1" or operation_choice.lower() == "log in":
            Login_page()
            break
        elif operation_choice == "2" or operation_choice.lower() == "sign up":
            SignUp_page()
            break
        elif operation_choice == "3" or operation_choice.lower() == "exit":
            return False
        else:
            print("Invalid option, please enter the corresponding option's number")

# Main execution begins here
print("Welcome Student")
sleep(0.5)
print("Please Choose an option listed below")
sleep(0.5)

# Loop to display the start menu until the user chooses to exit
while True:
    if startmenu() == False:
        print("Come Back Soon")
        break
