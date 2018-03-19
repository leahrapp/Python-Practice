
from flask import Flask, render_template, request, redirect, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'key_to_my_heart'
mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"                 
    rows = mysql.query_db(query)                 
    return render_template('index.html', all_rows=rows)

  

@app.route('/input', methods=['POST'])
def submit_form():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at, fave_color) VALUES (:first_name, :last_name, :occupation, NOW(), NOW(), :fave_color)"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation'],

             'fave_color':  request.form['fave_color']

           }
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)