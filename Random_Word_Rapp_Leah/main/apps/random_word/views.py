from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# Create your views here.
import time
from datetime import datetime 

def index(request):
    if 'counter' not in request.session:
        request.session['counter']=0
    request.session['counter']+=1
    
    
    word=get_random_string(length=14)
    request.session["word"]=word
    return render(request, "random_word/index.html")
