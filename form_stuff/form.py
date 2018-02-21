
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

location_list = ['Detroit', 'Alderaan', 'Themyscira', 'Tarth', 'Amphipolis', 'Queens' 'The Citadel']
biggest_abmition = ['Make a billion dollars', 'Have a city named after me', 'Become the President of the United States', 'Win a Nobel Prize', 'Get married, have babies and settle down' ]



@app.route('/')
def index():
    return render_template("index.html", location=location_list, ambition=biggest_abmition)
  

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    location = request.form['location']
    ambition = request.form['ambition']
    story = request.form['story']
    return render_template("success.html", name=name, location=location, ambition=ambition, story=story)  

app.run(debug=True)