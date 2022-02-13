import os.path
import pyrebase
from config import firebaseConfig

firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

# Authentication
# Login

def login():

    login_attempts = 0

    while True:
        email=input("Enter your email: ")
        password=input("Enter your password: ")

        try:
            user = auth.sign_in_with_email_and_password(email,password)
            print("Signed in successfully")
            break
        except:
            if login_attempts < 2:
                login_attempts = login_attempts + 1
                print("Invalid user or password. Try again.")
            else:
                print("Too many login attempts")
                break
    
    with open('.token', 'a') as file:
        file.write(user['idToken'])




# SignUp

def signUp():
    print("Fantastic. Lets sign you up!")
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    confirmpass=input("Confirm your password: ")

    if password == confirmpass:
        try:
            auth.create_user_with_email_and_password(email, password)
            print("Account created succesfully")
        except:
            print("Account already exists")
