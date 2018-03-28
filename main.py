from flask import Flask, request, redirect, render_template
import cgi
import os



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('user_form.html')

def space_chk(word):
    if " " in word:
        return False
    else:
        return True

def email_check(word):
    if word.find("@") == -1 or word.find(".") == -1:
        return False
    else:
        return True

def email_chk(word):
    if word.count("@")> 1 or word.count(".") > 1:
        return False
    else:
        return True
      

@app.route("/user", methods=['POST'])
def signup():

    user_name = request.form['user_name']
    password= request.form['password']
    confirm= request.form['confirm']  
    email= request.form['email']

    user_error = ''
    password_error = ''
    confirm_error = ''
    email_error = ''
    user_name_count = len(user_name)
    password_count = len(password)
    email_count = len(email)

    
    if (user_name_count > 20 or user_name_count < 3) or (user_name.strip() == "")  or (not space_chk(user_name)):
        user_error = 'Not a valid user name'
        user_name = ''
    
    if (password_count > 20 or password_count < 3) or (password.strip() == "") or (not space_chk(password)):
        password_error = 'Not a valid password'
        password = ''

    if confirm != password :
        confirm_error = 'Password doesnt match'
        confirm = ''

    if  (email_count == 0):
        email= request.form['email']

    else:
        if (email_count > 20 or email_count < 3) or (not email_check(email)) or (not email_chk(email)) or (not space_chk(email)):
           email_error = 'Not a valid email'
           email = ''


    if not user_error and not password_error and not confirm_error and not email_error:
        return render_template('welcome_greeting.html', name=user_name)
    
    else: 
        return render_template('user_form.html',user_name=user_name, email=email, user_error=user_error, password_error=password_error, confirm_error=confirm_error, email_error=email_error)


app.run()