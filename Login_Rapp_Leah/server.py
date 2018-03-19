
from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import os, binascii # include this at the top of your file
import md5 
import re
salt = binascii.b2a_hex(os.urandom(15))
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'key_to_my_heart'
mysql = MySQLConnector(app, 'logindb')

@app.route('/')
def index():
                
    return render_template('index.html')

  

@app.route('/input', methods=['POST'])
def submit_form():
    email = request.form['email']
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    password=request.form['password']
    flash_error=False

    
    if len(email) < 1:
        flash("Email cannot be blank!")
        flash_error=True
    if not EMAIL_REGEX.match( request.form['email']):
        flash("Invalid Email Address!")
        flash_error=True
    if len(first_name)<2:
        flash("Please put in your full first name.")
        flash_error=True
    if len(last_name)<2:
        flash("Please put in your full last name.")
        flash_error=True
    
    if password != request.form['confirm_password']:
        flash("Passwords must match")
        flash_error=True
    query = "SELECT * FROM login WHERE email = :email"
    data={ 'email': email}
    is_empty = mysql.query_db(query, data)
    if is_empty:
        flash('This email already exists, please enter a new email address')
        flash_error=True
    if flash_error:
        return redirect('/')

      
        
    else:
       
        hashed_pw = md5.new(password + salt).hexdigest
        insert_query = "INSERT INTO login (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data={ 'first_name':first_name, 'last_name':last_name, 'email': email, 'password':hashed_pw}
        result= mysql.query_db(insert_query, data)
        print('result', result)
        return redirect('/success')
                     




@app.route('/success')
def success():
    
   

  
    return render_template('success.html')


    

app.run(debug=True)