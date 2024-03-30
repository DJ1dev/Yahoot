import os
def Scan_Accounts():
    with open(r"Python/School/Yahoot/src/Storage/Accounts.txt",'r') as file:
        data = file.readlines()
        print(data)
        for x in data:
            w = x.split()
            print(w)