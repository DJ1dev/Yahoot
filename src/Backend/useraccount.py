results = []

def Scan_Accounts():                                                                #Function used to scan account storage file
    with open(r"Python/School/Yahoot/src/Storage/Accounts.txt",'r') as file:
        record = file.readlines()
        for data in record:
            info = data.split()
            results.append([info[0],info[2]])
    return sorted(results, key=lambda x : x[1], reverse=True)

def Account_Verify(username, password):                                             #Function used to find existing accounts in storage file
    with open(r"Python/School/Yahoot/src/Storage/Accounts.txt",'r') as file:
        record = file.readlines()
        for data in record:
            info = data.split()
            if str(username) == info[0]:                                            #Verify the username
                if str(password) == info[1]:                                        #Verify the password
                    return True

def Add_Accounts(username, password):                                               #Function used to Create new Accounts in storage file
    with open(r"Python/School/Yahoot/src/Storage/Accounts.txt", 'a') as file:
        file.write('\n' + str(username) + ' ' + str(password) + ' ' + '0')          #Adds the new user's details to a new line in the text file
        return True
