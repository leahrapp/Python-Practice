
from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'key_to_my_heart'
mysql = MySQLConnector(app, 'email')

@app.route('/')
def index():
                
    return render_template('index.html')

  

@app.route('/input', methods=['POST'])
def submit_form():
  
    if len( request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match( request.form['email']):
        flash("Invalid Email Address!")
    else:
        
        query = "SELECT * FROM email WHERE email = :email"
        data={ 'email': request.form['email']}
        is_empty = mysql.query_db(query, data)
        if not is_empty:
          insert_query = "INSERT INTO email (email, created_on, updated_on) VALUES (:email, NOW(), NOW())"
          data={ 'email': request.form['email']}
          mysql.query_db(insert_query, data)
          return redirect('/success')
        else:
          flash('This email already exists, please enter a new email address')
                     

    return redirect('/')



@app.route('/success')
def success():
    
   

    query = "SELECT * FROM email"                 
    rows = mysql.query_db(query)  
    return render_template('success.html', all_rows=rows)


    

app.run(debug=True)