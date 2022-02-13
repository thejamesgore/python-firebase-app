from rsa import sign
from auth import login, signUp

mode = input("Welcome to the firebase test app. Do you want to (L)ogin or (S)ign Up? ").upper()

if mode == "L":
    login()
elif mode == "S":
    signUp()