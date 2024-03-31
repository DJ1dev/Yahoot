import sys
from pathlib import Path
root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(root_path))


from Backend import useraccount
from time import sleep



def Login_page():                                                                               #handles The log in page
    print("\n[---Log in---]")

    username = input("Username :\t")
    password = input("Password :\t")
    
    useraccount.Account_Verify(username, password)


def SignUp_page():                                                                              #handles The Sign up page
    print("\n[---Sign up---]")

    username = input("Username :\t")
    password = input("Password :\t")
    
    print("\nSuccessful")


def startmenu():
    while True:
        operation_choice = input("[---Menu---]\n1: Log In\n2: Sign Up\n3:Exit\nAnswer:\t")
        if operation_choice == "1" or operation_choice ==  "Log in":
            Login_page()
            break
        elif operation_choice == "2" or operation_choice ==  "Sign up":
            SignUp_page()
            break
        elif operation_choice == "3" or operation_choice ==  "Exit":
            print("Come Back Soon")
            break
        else:
            print("Invalid option, please enter the corresponding option's number")


print("Welcome Student")
sleep(0.5)
print("Please Choose an option lsited below \n")
sleep(0.5)

startmenu()
