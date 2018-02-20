
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

turtle_dic={"blue":"leonardo", "purple":"donatello", "red":"raphael", "orange":"michelangelo","notapril":"notapril", "tmnt":"tmnt" }



@app.route('/')
def index():
    return render_template("index.html")
  
@app.route('/ninja/<color>')
def get_ninja(color):    
   
   turtle=turtle_dic.get(color, "notapril")
   ext="jpg" if color != "tmnt" else "png"
   jpg="{}.{}".format(turtle, ext)
   return render_template("ninja.html", jpg=jpg)  


app.run(debug=True)