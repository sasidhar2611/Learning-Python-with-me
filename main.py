from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1}  :  {items}")

def createfile():

    try:
        readfileandfolder()
        name = input("Please tell your file name: ")
        p = Path(name)
        if not p.exists() and p.is_file():
            with open(p,"w") as fs:
                data = input("What you want to write in this file? : ")
                fs.write(data)

            print(f"FILE NAMED {name} CREATED SUCCESFULLY!!")
        else:
            print("This File already exits")
    except Exception as err:
        print(f"An error occured as {err}")


def readfile():
    try:
        readfileandfolder()
        name = input("Which file you wan to read? : ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)

            print("FILE READ SUCCESFULLY!!!")

        else:
            print("File dosen not exist")

    except Exception as err:
        print(f"An errro occured as {err}")

    
def updatefile():
    try:
        readfileandfolder()
        name = input("Tell which file you want to update? : ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for Changing the name of the file")
            print("Press 2 for overwriting the data of the file")
            print("Press 3 for appending some content in the file")

            res = int(input("Tell your Response"))

            if res == 1:
                name2 = input("Tell your New file name: ")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p, 'w') as fs:
                    data = input("Tell what you want to write? This will overrride the data: ")
                    fs.write(data)

            if res == 3:
                with open(p, 'a') as fs:
                    data = input("Tell what you want to append? This will append the data: ")
                    fs.write(" "+data) 
    
    except Exception as err:
        print("An error occured as {err}")


def deletefile():
    try:
        readfileandfolder()
        name = input("Which file you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)

            print("File removed succesfully!!")

        else:
            print("No such file exist")
    
    except Exception as err:
        print("An error occured as {err}")

print("Press 1 for Creating a file")
print("Press 2 for Reading a file")
print("Press 3 for Updating a file")
print("Press 4 for Deleting a file")

check = int(input("Please enter your response:- "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()