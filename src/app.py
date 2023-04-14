from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#database
class courses(db.Model):
    course_name = db.Column(db.String(100), primary_key=True)
    completion_status = db.Column(db.String(30), nullable=False)

    def __repr__(self) -> str:
        return f"{self.course_name} | {self.course_status}"

#index page
@app.route("/")
def hello_world():
    return render_template('index.html')

#login page
@app.route("/login")
def login():
    return "login page"