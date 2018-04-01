
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
location_list = ['Detroit', 'Alderaan', 'Themyscira', 'Tarth', 'Amphipolis', 'Queens' 'The Citadel']
biggest_abmition = ['Make a billion dollars', 'Have a city named after me', 'Become the President of the United States', 'Win a Nobel Prize', 'Get married, have babies and settle down' ]

def index(request):
    
    
    context = {
        "location" : location_list,
        "ambition" : biggest_abmition
    }
    if 'counter' not in request.session:
        request.session['counter']=1
    

    return render(request, "surveys/index.html", context)

def process(request):
       
        request.session["counter"]=request.session['counter']+1
        request.session["location"]=request.POST["location"]
        request.session["name"]=request.POST["name"]
        request.session["ambition"]=request.POST["ambition"]
        request.session["story"]=request.POST["story"]
        
        
        return redirect('/results')

def results(request):
  
    return render( request, "surveys/success.html")
