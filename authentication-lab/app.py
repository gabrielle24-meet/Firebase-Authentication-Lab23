from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

firebase = 

config = {
"apiKey": "AIzaSyAFSxExGBR4zkhGJRK_Xb-BFz3mE5T4nBM",
  "authDomain": "example-9e0f4.firebaseapp.com",
  "projectId": "example-9e0f4",
  "storageBucket": "example-9e0f4.appspot.com",
  "messagingSenderId": "5891476454",
  "appId": "1:5891476454:web:920a5f8c52b0041e9be427",
  "measurementId": "G-LXM8YFZZ2B"
    
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()





app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method =='Post'
    email = request.form['email']
    password = request.form['password']
    try:
        login_session['user']=
            auth.create_user_with_email_and_password(email,password)
    except:       
        error = "Authentication failed"
        return render_template("sighnup.html")


    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)


