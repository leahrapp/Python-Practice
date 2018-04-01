
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Users
from django.core.urlresolvers import reverse
import datetime
# Create your views here.

def index(request):
    
    users= Users.objects.all()
    if (len(users)<1):
        messages.add_message(request, messages.WARNING, 'There are currently no users, please add one now')
        return redirect('/add')

    
          
    return render(request, "semi_rest/index.html", {'context':users})

def add(request):
        
    return render(request, 'semi_rest/add.html')

def edit(request, id):
    user = get_user(id)
  
   

    return render( request, "semi_rest/edit.html", {'context':user})

def add_user(request):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/add')
    else:
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            email=request.POST["email"]
            Users.objects.create(first_name=first_name, last_name=last_name, email=email)
            return redirect('/')




def delete(request, id):
    user = get_user(id)
    user.delete()
    
   
    return redirect('/')
  
def show(request, id):
   
    user = get_user(id)
    

    return render(request, 'semi_rest/show.html', {"context":user})

def get_user(id):
    
    user=Users.objects.get(id=id)

    return user

def save_edit(request, id):

    errors = Users.objects.basic_validator(request.POST)
    if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect( 'my_edit', id=id)   
    else:
            user=get_user(id)
            user.first_name=request.POST["first_name"]
            
            user.last_name=request.POST["last_name"]
            email=request.POST["email"]
            user.save()
            return redirect('/')


    