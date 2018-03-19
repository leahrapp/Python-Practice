
from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
location_list = ['Detroit', 'Alderaan', 'Themyscira', 'Tarth', 'Amphipolis', 'Queens' 'The Citadel']
biggest_abmition = ['Make a billion dollars', 'Have a city named after me', 'Become the President of the United States', 'Win a Nobel Prize', 'Get married, have babies and settle down' ]


app.secret_key = 'ChamberOfSecrets'


@app.route('/')
def index():
     return render_template("index.html", location=location_list, ambition=biggest_abmition)
  



@app.route('/submit', methods=['POST'])
def submit_form():
     location = request.form['location']
     ambition= request.form['ambition']
     story = request.form['story']
     name = request.form['name']
     if len(request.form['name']) < 1:
        flash("Name cannot be empty!") # just pass a string to the flash function
       
     if len(request.form['story'])>120:
         flas("Story has to be super small, like, less than 120 characters")
                             
     return redirect("/")  

app.run(debug=True)