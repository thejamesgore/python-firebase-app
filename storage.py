import pyrebase
from config import firebaseConfig
import os


firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()


# Viewing web folder
def view():
    projectID = os.environ.get('PROJECT_ID')
    storage_url = os.environ.get('STORAGE_BUCKET')
    url = f"https://console.firebase.google.com/u/0/project/{projectID}/storage/{storage_url}/files"
    print("👇 The storage folder url is 👇 " + "\n",  url)

# Uploading files
def upload():

    with open('.token') as file:
        token = file.read()

    filename = input("Enter the name of the file you wish to upload: ")
    storage.child(filename).put(filename, token)
    
    print("File uploaded successfully.")
    print(storage.child(filename).get_url(None))


# Downloading files
def download():

    filename = input("Enter the name of the file you wish to download: ")
    localname = input("What do you wish to save the file as?: ")
    storage.child(filename).download("", localname)
    print("File downloaded successfully")
