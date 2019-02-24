import time
from getpass import getpass

global secret1
global secret2

secret1 = input("A secret: ")
secret2 = input("Another secret: ")
# clear lines 
print("\x1B[2J")

def reg():
    print("register!")
    time.sleep(1)
    global user
    global psw
    user = str(input("New Username: "))
    psw = getpass("New Password: ")
    time.sleep(1)
    print("Password and Username has been set successfully! continue.")
    print("\x1B[2J")

def login():
    print("Login with Username and Password!")
    login_username = str(input("Username: "))
    login_password = getpass("Password: ")
    if(login_username != user or login_password != psw):
        print("\x1B[2J")
        print("username or password is incorrect please try again!")
        login()
    else:
        print("Success!")
        time.sleep(1)
        print("\x1B[2J")

def result():
    print("You now have access to the secerts...")
    print("the first secert --> "+ str(secret1))
    print("the second secret --> "+ str(secret2))


def run():
  reg()
  login()
  result()
run()
