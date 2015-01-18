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
    
@app.route('/register', methods = ['POST'])
def register():
    reg_nameF = request.form['FNAME']
    reg_nameL = request.form['LNAME']
    reg_email = request.form['EMAILR']
    reg_email_conf = request.form['EMAILR1']
    reg_pass = request.form['PWORD']
    reg_pass_conf = request.form['PWORD1']
    
    if (reg_email != reg_email_conf) or (reg_pass != reg_pass_conf):
        return redirect('/')
    
    print("pretending to add " + str(reg_nameF) + " " + str(reg_nameL))
    print("email: " + reg_email)
    print("pass:  " + reg_pass)
    return redirect('/add')

@app.route('/add')
def add():
    return render_template('addClasses.html')

@app.route('/majors')
def majors():
    return render_template('Majorspageremake.html')
    
    
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()