
from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import os, binascii # include this at the top of your file
import md5 
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'key_to_my_heart'
mysql = MySQLConnector(app, 'walldb')

@app.route('/')
def index():
                
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():    

    session['logged_in']=False
    login=request.form['loginId']
    salt =  binascii.b2a_hex(os.urandom(15))
    pWord=request.form['loginPassword']
    


    query = "SELECT * FROM users where email= :email LIMIT 1"
    data={'email':login } 
    user_query = mysql.query_db(query, data)
    if(len(user_query))>0:
       
       encrypted_password = md5.new(pWord + user_query[0]['salt']).hexdigest()
       if user_query[0]['password'] == encrypted_password:
            session['user_name']="{} {}".format(user_query[0]["first_name"], user_query[0]["last_name"]) 
            session['logged_in']=True
            return redirect('/getWall')
            
       else:
           flash("Incorrect Password") 
           return redirect('/getRegistration')
    else:
       flash("User Not found, please register") 

@app.route('/getRegistration', methods=['GET'])
def get_registration():
    return render_template('/registration.html')
  

@app.route('/register', methods=['POST'])
def submit_form():
    email = request.form['email']
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    password=request.form['password']
    salt =  binascii.b2a_hex(os.urandom(15))
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
    if len(password)<8:
        flash("Password must be greater than 8 characters long")
    if password != request.form['confirm_password']:
        flash("Passwords must match")
        flash_error=True
    query = "SELECT * FROM users WHERE email = :email"
    data={ 'email': email}
    is_empty = mysql.query_db(query, data)
    if is_empty:
        flash('This email already exists, please enter a new email address')
        flash_error=True
    if flash_error:
        return redirect('/getRegistration')

      
        
    else:
       
        hashed_pw = md5.new(password + salt).hexdigest()
       
        insert_query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password,:salt, NOW(), NOW())"
        data={ 'first_name':first_name, 'last_name':last_name, 'email': email, 'password':hashed_pw, 'salt':salt}
        result= mysql.query_db(insert_query, data)
        session['userId']=result
        session['logged_in']=True
        return redirect('/getWall')
                     

@app.route('/getWall')
def return_wall():

    query_messages= "SELECT *  FROM messages"
    messages=mysql.query_db(query_messages)
    messages_arr=[]
    
    
    
    for message in messages:
       
        message_dict={}
        query_name_of_poster= "SELECT * FROM users WHERE id = :message_id"
        data={'message_id':message['user_id']}
        posters=mysql.query_db(query_name_of_poster, data)
        
        
        message_dict['message']=message["comment"]
        message_dict['id']=message["id"]
        for poster in posters:
           
            message_dict['user_name']= '{} {}'.format(poster['first_name'], poster['last_name'])
        
        message_dict['time']= message['created_at']
       


        query_comments = "SELECT * FROM comments WHERE message_id=:message_id"
        comment_data={'message_id':message['id']}
        comments=mysql.query_db(query_comments, comment_data)
        
        comments_arr=[]
        for comment in comments:
            comment_dict={}
            query_name_of_commenter= "SELECT * FROM users WHERE id =:user_id"
            data ={'user_id':comment['user_id']}
            commenter=mysql.query_db(query_name_of_commenter, data)
            
            comment_dict['comment_id']=comment['id']
            comment_dict['comment']=comment['comment']
            comment_dict['time_posted']=comment['created_at']
            
            for comm in commenter:
                comment_dict['comment_name']= '{} {}'.format(comm['first_name'], comm['last_name'])
            comments_arr.append(comment_dict)
            
        message_dict['comments']=comments_arr 

        messages_arr.append(message_dict)
   
    return render_template("/wall.html", messages_arr=messages_arr)

@app.route('/message', methods=['POST'])
def save_mess():
    
    insert_query="INSERT INTO messages(user_id, comment, created_at, updated_at) VALUES(:user_id, :comment, NOW(), NOW())"
    data={'user_id':session['userId'], 'comment':request.form['message']}
    mysql.query_db(insert_query, data)
    return redirect("/getWall")
    
@app.route('/comment', methods=['POST'])
def save_comm():
   
    insert_query="INSERT INTO comments(user_id,message_id, comment,  created_at, updated_at) VALUES(:user_id,:message_id, :comment, NOW(), NOW())"
 
    data={'user_id':session['userId'], 'message_id':request.form['message_id'], 'comment':request.form['comment']}
    mysql.query_db(insert_query, data)
    return redirect("/getWall")    





app.run(debug=True)