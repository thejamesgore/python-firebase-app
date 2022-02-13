from rsa import sign
from auth import login, signUp
from storage import upload, download, view

startUp = input("Welcome to the firebase test app. Do you want to (L)ogin or (S)ign Up? ").upper()

if startUp == "L":
    login()
elif startUp == "S":
    signUp()

# Main Menu
while True:
    print("What would you like to do?")
    mode = input("(A)ccount management, (S)torage, (D)atabase, (Q)uit?: ").upper()

    if mode == "A":
        print("Not built out yet...")

    if mode == "S":

        # Storage Menu
        while True:
            storage_mode = input("(V)iew files in browser, (U)pload file, (D)ownload, (Q)uit to main menu: ").upper()
            if storage_mode == "V":
                view()
            if storage_mode == "U":
                upload()
            if storage_mode == "D":
                download()
            elif storage_mode == "Q":
                break
    
    if mode == "D":
        print("Database functionality not built out yet")

    elif mode =="Q":
        break