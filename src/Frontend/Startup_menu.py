from time import sleep

def Login_page():
    print("\n[---Log in---]")

    username = input("Username :\t")
    password = input("Password :\t")
    
    print("\nLogged in")

def SignUp_page():
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
