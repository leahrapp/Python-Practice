from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html", hola ="I Said HELLO")
  

@app.route('/ninjas')
def ninja():  
    return render_template("ninjas.html", ninja ="NINAS")

@app.route('/dojo/new', builtin_method_descriptor=['POST'])    
def new():
    name = request.form['name']
    email = request.form['email']
    return redirect("/")  

app.run(debug=True)
