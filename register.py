from flask import Flask, render_template,request,session,redirect,url_for
import json


class register_class :

    @staticmethod
    def login(username,password):
        
        data_string = open('accounts.json').read()
        data_converted=json.loads(data_string)
        
        # if username and password != "":
        
        if username in data_converted :
                    if data_converted[username] == password:
                            session.permanent=True
                            session['uname'] = request.form['username']
                            session['pass'] = request.form['password']
                            return "success", "<h1>You are logged in</h1>"
                    else:
                            return "wrong_password"
        else:
                    return "username doesnt exist, make an account"
        # else:   
        #     return render_template('sign-in.html')
        
    @staticmethod
    def signup(username,password):
        try:
            with open('accounts.json', 'r') as f:
                data_converted = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data_converted = {}

        if username in data_converted :
            return "<h1>username already taken :O</h1>"
        
        elif username and password != "":
            data_converted[username]=password
            with open('accounts.json', 'w') as f:       
                json.dump(data_converted, f, indent = 2)
            return "<h1>you have an accont now, cool! ;)</h1>"
        return render_template('sign-up.html')
           