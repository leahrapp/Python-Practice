from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
import time
from datetime import datetime 
def index(request):
    context = {
        "time" : datetime.now().strftime("%Y-%m-%d %H:%M %p")
    }
    return render(request, "time_display/index.html", context)
