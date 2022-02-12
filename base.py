import os
import pyrebase
from dotenv import load_dotenv

load_dotenv('.env')
apiKey = os.environ.get('APIKEY')

firebaseConfig = {'apiKey': apiKey,
                  'authDomain': "python-firebase-5af18.firebaseapp.com",
                  'projectId': "python-firebase-5af18",
                  'storageBucket': "python-firebase-5af18.appspot.com",
                  'messagingSenderId': "179444754339",
                  'appId': "1:179444754339:web:85f74a033a46a31f135c16",
                  'measurementId': "G-99M299LF01"
                  }
