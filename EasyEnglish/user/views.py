from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('./credentials.json')

firebase_admin.initialize_app(cred, {'databaseURL': 'https://easyenglish-3b012-default-rtdb.europe-west1.firebasedatabase.app/'})

# Create your views here.
def index(request):
    """ref = db.reference('users')
    datos = ref.get() """
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')