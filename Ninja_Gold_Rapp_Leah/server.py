
from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = 'key_to_my_heart'




@app.route('/')
def index():
    session['gold']=0 
    session["arr"]=[]
    return render_template("/index.html")
  



@app.route('/process_money', methods=['POST'])
def add_gold():
    won=0
    print("asdfasdfasdfasdfasdfasdf",won)
    if request.form["action"]=="farm":
        
        won=random.randint(10, 20)     
        session['gold']+= won    
    if request.form["action"]=="cave":
        won=random.randint(5, 10)
        session['gold']+=won
    if request.form["action"]=="home":
        won=random.randint(2, 5)
        session['gold']+=won
    if request.form["action"]=="casino":
        coin=random.randint(0, 1)
        

        if coin==1:
            won=random.randint(0, 50)
            session['gold']=won
        else:
            won=random.randint(0, 50)
            session['gold']-=won

    tiempo =datetime.datetime.now()
    session["arr"].append("You entered the {} at {} and won {}".format(request.form["action"], tiempo, won))
   
    return render_template("index.html", all_dat_gold=session["gold"], won=won, winnings=session["arr"] )

app.run(debug=True)