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
                  'measurementId': os.environ.get('MEASUREMENT_ID')
                  }

print(firebaseConfig)

