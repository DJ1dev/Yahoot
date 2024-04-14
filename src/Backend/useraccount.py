#Function used to scan account storage file as readable
def point_management(username, points):
    with open(r"Python/School/Yahoot/src/Storage/Accounts.txt",'r') as file:    
        record = file.readlines()                                               #Pulls all the lines of the txt file and assigns it to the variable 'records'
        for index, line in enumerate(record):                                   #for every element and its index in an enumerated record the following code is executed                          
            data = line.split()                                                 #Splits the contents of elements in the record
            if username in data:                                                #Scans the element if the username is located in the element, if true the following code is executed 
                new_points = int(data[2]) + points                              #Assigns the variable "new_points" to the current points added to the assigned points variable
                data[2] = str(new_points) + "\n"                                #Replaces the current score with the  new_points
                line = data[0] +" "+ data[1]+" "+ data[2]                       #properly formats the entry
                record[index] = line                                            #replaces the formatted entry into the records data at the username's index  
    file = open(r"Python/School/Yahoot/src/Storage/Accounts.txt",'w')           #Opens the file path for rewriting
    file.writelines(record)                                                     #Updates the entire file
    file.close()                                                                #Closes the file

def Scan_Accounts():  
    results = []                                                                #Function used to scan account storage file
    with open(r"Python/School/Yahoot/src/Storage/Accounts.txt",'r') as file:
        record = file.readlines()                                               #Pulls all the lines of the txt file and assigns it to the variable 'records'
        for data in record:
            info = data.split()
            results.append([info[0],info[2]])
    return sorted(results, key=lambda x : int(x[1]), reverse=True)

def Account_Verify(username, password):                                          #Function used to find existing accounts in storage file
    with open(r"Python/School/Yahoot/src/Storage/Accounts.txt",'r') as file:
        record = file.readlines()                                                #Pulls all the lines of the txt file and assigns it to the variable 'records'
        for data in record:
            info = data.split()
            if str(username) == info[0]:                                         #Verify the username
                if str(password) == info[1]:                                     #Verify the password
                    return True

def Add_Accounts(username, password):                                            #Function used to Create new Accounts in storage file
    with open(r"Python/School/Yahoot/src/Storage/Accounts.txt", 'a') as file:
        file.write('\n' + str(username) + ' ' + str(password) + ' ' + '0')       #Adds the new user's details to a new line in the text file
        return True

