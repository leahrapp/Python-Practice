
from django.shortcuts import render, HttpResponse, redirect
import datetime
# Create your views here.

def index(request):
    
   
   
    return render(request, "session_words/index.html")

def add_word(request):
       
        

        
        if "bold" in request.POST:
            font_weight="bold"
        else:
            font_weight="normal"

        word=request.POST["word"]
        
        time=str(datetime.datetime.now())
        color=request.POST["radio"]
        
        row_dict={
            "font_weight":font_weight,
            "word":word,
            "time":time,
            "color":color
            
            
            }
        if "row" not in request.session:
            request.session["row"]=[row_dict]
        else:
            temp_list=request.session["row"]
            temp_list.append(row_dict)
            request.session["row"]=temp_list
        
        
        
        return redirect( '/session_words')

def clear_word(request):
    request.session.clear()
    return redirect( "/session_words")
