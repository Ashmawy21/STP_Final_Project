from flask import Flask, render_template,request,session,redirect,url_for


app=Flask(__name__)
app.secret_key="STP"



@app.route('/journy pricing')
def journy_pricing():
    return render_template('journy_pricing.html')


@app.route('/sign in', methods=["GET","POST"])
def sign_in ():
    if 'uname' in session:
        return redirect(url_for('index'))
    elif request.method =="POST":
        session.permanent=True
        session['uname'] = request.form['username']
        session['pass'] = request.form['password']
        return redirect(url_for('index'))
    else:
        return  render_template('sign-in.html')

@app.route('/sign up')
def sign_up():
    return render_template('sign-up.html')


@app.route('/')
def index():
    if "uname" in session:
        return render_template('home_page.html')
    else:
        return render_template('sign-in.html')



if __name__=='__main__':
    app.run(debug=True)