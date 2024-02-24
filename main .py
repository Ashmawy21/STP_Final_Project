from flask import Flask, render_template, request, jsonify
import json
from register import register_class

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('home_page.html')
    

@app.route('/sign up')
def sign_up():
    username = request.args.get('username')
    password = request.args.get('password')
    return register_class.signup(username,password)
    

@app.route('/sign in',  methods=["GET","POST"])
def sign_in ():
    username = request.form.get('username')
    password = request.form.get('password')
    return register_class.login(username,password)
    
    


@app.route('/journy pricing')
def journy_pricing():
    return render_template('journy_pricing.html')




if __name__=='__main__':
    app.run(debug=True)