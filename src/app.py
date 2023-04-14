from flask import Flask, render_template

app = Flask(__name__)



#index page
@app.route("/")
def hello_world():
    return render_template('index.html')

#login page
@app.route("/login")
def login():
    return "login page"