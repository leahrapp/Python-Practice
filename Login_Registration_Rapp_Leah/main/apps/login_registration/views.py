
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import Users
from django.core.urlresolvers import reverse
import hashlib
import datetime
from bcrypt import hashpw, gensalt
# Create your views here.

def index(request):
    return render(request, "login_registration/index.html")

def login(request):
    users = get_user(request.POST['email'])
    user=next(iter(users))
    post_pword=(request.POST['password'])
    post_pword=post_pword.encode()
    
    user_pword=user.password
    user_pword=user_pword.encode()
    
    
    
    if  hashpw(post_pword, user_pword)==user_pword:
        request.session["email"]=user.email
        return redirect('/success')
    else:
        messages.add_message(request, messages.INFO,"Either the email provided or the password is wrong")
        return redirect('/')
        


def add_user(request):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        user = get_user(request.POST["email"])
        if len(user)>1:
            messages.add_message(request, messages.INFO, 'This email is already registered. please use another')
            return redirect('/')

        else:     
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            email=request.POST["email"]
            password=request.POST["password"]
            temp_password=password.encode()
            hashed_password=hashpw(password.encode(), gensalt())

            user=Users.objects.create(first_name=first_name, last_name=last_name,password=hashed_password, email=email)
            request.session["email"]=user.email
            return redirect( '/success')





  
def success(request):
    email=request.session['email']
    
    users=get_user(str(email))
    for user in users:
        print(user.email)
    
    
    

    return render(request, 'login_registration/success.html', {'context':user})

def get_user(email):
    
    user=Users.objects.filter(email=email)

    return user



    