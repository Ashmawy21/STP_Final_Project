from flask import Flask, render_template,request,session,redirect,url_for
from register import register_class
import json
import hashlib


app=Flask(__name__)
app.secret_key="STP"



@app.route('/journy pricing')
def journy_pricing():
    return render_template('journy_pricing.html')


@app.route('/sign in', methods=["GET","POST"])
def sign_in ():
    if 'uname' in session:
        return redirect(url_for('index'))
    
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if password!=None:
            hashed_pass=hashlib.sha256(password.encode()).hexdigest()
            return register_class.login(username,hashed_pass)
        else:
            return render_template('sign-in.html')
@app.route('/sign up')
def sign_up():
    username = request.args.get('username')
    password = request.args.get('password')
    return register_class.signup(username,password)


@app.route('/')
def index():
    if "uname" in session:
        return render_template('home_page.html')
    
    else:
        return render_template('sign-in.html')



if __name__=='__main__':
    app.run(debug=True)