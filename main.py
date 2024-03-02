import flask
from flask import Flask, render_template, request, session, redirect, url_for, make_response, jsonify
from flask_cors import CORS, cross_origin
from register import register_class
from DeploymentV1 import monopred
import pandas as pd
from flask_session import Session



app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)
app.secret_key = "STP"
app.config['SECRET_KEY'] = 'STP'

@app.route('/journy_pricing', methods=["GET", "POST"])
def journy_pricing():
    
    # print(data)

    if request.method == "GET":
        print('HI')
        return render_template("Journy_pricing.html")
    elif request.method == "POST":
        print('hello')
        data = request.json
        kilo = data['distanceInKilometers']
        Price = monopred(kilo)
        print(type(Price))
        # return jsonify({'price': price})
        payload= f'The price is {Price} L.E'
        print(payload)
        print(kilo)
        return jsonify({'price':Price})   #wrote while testing
        # if Price == None:
            
        #     return render_template("Journy_pricing.html")
        # return f'the price is {Price}'
       

        

@app.route('/price')
def price():
    #print(session)
    #print(type(session))
    #money=session.get('price', 'not assigned yet')
    return render_template('price.html')

@app.route('/sign in', methods=["GET", "POST"])
def sign_in():
    if 'uname' in session:
        return redirect(url_for('index'))
    else:
        username = request.form.get('username')
        email = request.args.get('email')
        password = request.form.get('password')

        return register_class.login(username, password)


@app.route('/sign up')
def sign_up():
    username = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')
    confirmPassword = request.args.get('confirmPassword') 
    if username and email:
        session.permanent = True
        session['profileName'] = username
        session['profilemail'] = email

    return register_class.signup(username,email,password,confirmPassword)


@app.route('/profile')
def profile():
    if "uname" in session:
        username = session.get('profileName')
        email = session.get('profilemail')
        return render_template('profile.html', Username=username, Email=email)

    else:
        return render_template('sign-in.html')


@app.route('/')
def index():
    if "uname" in session:
        return render_template('Journy_pricing.html', )

    else:
        return render_template('sign-in.html')


@app.route('/forget-pass', methods=["GET", "POST"])
def forget():
    username = request.args.get('username')
    email = request.args.get('email')
    new_password = request.args.get('password')
    password_verify = request.args.get('password-verify')
    return register_class.forget(username,email,new_password,password_verify)





@app.route('/logout')
def logout():
    try:
        session.pop('uname')
        session.pop('pass')
        return render_template('sign-in.html')
    except:
        return "You don't have an existing account!"

if __name__ == '__main__':
    app.run(debug=True)
