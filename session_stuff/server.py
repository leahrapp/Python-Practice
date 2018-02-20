
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)


app.secret_key = 'ChamberOfSecrets'

@app.route('/')
def index():
    index=1;
    session["count"]=index+session["count"]; 




    return render_template("index.html", count=session["count"])
  

@app.route('/count', methods=['POST'])
def count_session():
    session["count"]=session["count"]+1
    return redirect("/")  

@app.route('/reset', methods=['POST'])
def reset_session():
    session["count"]=0
    return redirect("/")  

app.run(debug=True)