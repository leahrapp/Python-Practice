
from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'key_to_my_heart'




@app.route('/')
def index():
    session["random"] = random.randrange(0, 101)
    name = "hello"
    img = "hello.jpg"
    
    button_text = "Submit"
    redir="/guess"
    return render_template("index.html", redir=redir, name=name, img=img, button_text=button_text)
  



@app.route('/guess', methods=['POST'])
def submit_form():
    guess = int(request.form["guess"]) 
    rand = int(session["random"])   
    redir='/guess'    
    button_text = "Submit"

    if guess > rand:
       name = "too high"
       img = "too_high.jpg"
       
    elif guess < rand:
        name = "too low"
        img = "too_low.jpg"


    else:
        name = "correct"
        img = "success.jpg"
        button_text = "Again?!?!?"
        redir="/redir"
    return render_template("index.html",redir=redir,name=name, img=img, button_text=button_text)

@app.route('/redir', methods=['POST'])
def redir_form():


    return redirect("/")
app.run(debug = True)


@app.route('/guess', methods=['POST'])
def submit_form():
  
    return render_template("success.html")  

app.run(debug=True)