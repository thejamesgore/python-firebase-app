import os
import pyrebase
from dotenv import load_dotenv

load_dotenv('.env')

firebaseConfig = {'apiKey': os.environ.get('API_KEY'),
                  'authDomain': os.environ.get('AUTH_DOMAIN'),
                  'projectId': os.environ.get('PROJECT_ID'),
                  'storageBucket': os.environ.get('STORAGE_BUCKET'),
                  'messagingSenderId': os.environ.get('MESSAGING_SENDER_ID'),
                  'appId': os.environ.get('APP_ID'),
                  'measurementId': os.environ.get('MEASUREMENT_ID'),
                  'databaseURL': os.environ.get('DB_URL')
                  }

firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

# Authentication
email=input("Enter your email: ")
password=input("Enter your password: ")

auth.sign_in_with_email_and_password(email,password)
