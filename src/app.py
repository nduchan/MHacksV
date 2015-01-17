from flask import Flask
from flask import render_template, request, redirect
app = Flask(__name__)
email_addresses = []

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()