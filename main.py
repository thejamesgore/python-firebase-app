from rsa import sign
from auth import login, signUp
from storage import upload

startUp = input("Welcome to the firebase test app. Do you want to (L)ogin or (S)ign Up? ").upper()

if startUp == "L":
    login()
elif startUp == "S":
    signUp()

print("What would you like to do?")
mode = input("(U)pload a file, (Q)uit?: ").upper()

if mode == "U":
    upload()
elif mode =="Q":
    pass

