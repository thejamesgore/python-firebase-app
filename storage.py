import pyrebase
from config import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)

storage=firebase.storage()

# Uploading files

def upload():
    filename=input("Enter the name of the file you wish to upload: ")
    storage.child(filename).put(filename)