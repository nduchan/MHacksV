from flask import Flask
from flask import render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
    login_email = request.form['EMAIL']
    login_password = request.form['PASS']
    print("login = " + login_email)
    print("pass  = " + login_password)
    if login_password == "password":
        return redirect('/home')
    else:
        return redirect('/')
    
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()