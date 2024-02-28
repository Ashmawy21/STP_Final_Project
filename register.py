from flask import Flask, render_template,request,session,redirect,url_for
import json
import hashlib


class register_class :

    @staticmethod
    def login(username,email,password):
        try:
            with open('accounts.json', 'r') as f:   #read the json file to check for existing accounts
                data_converted = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):  #if account doesn't exist, redirect to sign up 
            return 'make account first'
        
        data_string = open('accounts.json').read()   
        data_converted=json.loads(data_string)   #getting data from the json file as read only

        if password != None:
            hashed_pass=hashlib.sha256(password.encode()).hexdigest()   #hashing the data for user's privacy
        else:
            return render_template('sign-in.html')   #if password not given, user won't be able to sign in
        
        # if username and password != "":
        
        if username in data_converted or email in data_converted :   #login using emal or username that must be already existing in the json file
            if data_converted[username or email] == hashed_pass:     #checking that the password given by user is for the correct email/username
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
    def signup(username,email,password):
        try:
            with open('accounts.json', 'r') as f:   #checking if data already exists in the json file to avoid saving the same data more than once 
                data_converted = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data_converted = {}

        if username in data_converted :   #checking that the username has a unique username
            return "<h1>username already taken :O</h1>"
        
        elif email in data_converted :   #checking that the username has a unique email
            return "<h1>email already taken :O</h1>"
        
        elif username and password != "":    
            data_converted[username]=hashlib.sha256(password.encode()).hexdigest()   #assigning each email/username to its hashed password 
            data_converted[email]=hashlib.sha256(password.encode()).hexdigest()
            with open('accounts.json', 'w') as f:       
                json.dump(data_converted, f, indent = 2)   #saving the user's data in the json file
            return "<h1>you have an account now, cool! ;)</h1>"
        return render_template('sign-up.html')
           