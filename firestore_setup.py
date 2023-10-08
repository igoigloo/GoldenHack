import firebase_admin
from firebase_admin import credentials, firestore

# Replace with the path to your service account key
cred = credentials.Certificate("goldenhacks-18e68-firebase-adminsdk-ywa05-28fcbdbd8b.json") 
firebase_admin.initialize_app(cred)

db = firestore.client()