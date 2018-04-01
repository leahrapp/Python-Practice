from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
from django.core import serializers
from django.http import JsonResponse
import json

# Create your views here.

def index(request):
    
    #return render(request, "ajax/index.html" )
   
    if "note" in request.POST:
        data=request.POST["note"]
        print(data)
        return HttpResponse(json.dumps(data), content_type="application/json" )
    else:
        return render(request, "ajax/index.html" )


