from flask import Flask, render_template,request
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('home_page.html')

@app.route('/journy pricing')
def journy_pricing():
    return render_template('journy_pricing.html')

@app.route('/sign in')
def sign_in ():
    return render_template('sign-in.html')

@app.route('/sign up')
def sign_up():
    return render_template('sign-up.html')






if __name__=='__main__':
    app.run(debug=True)