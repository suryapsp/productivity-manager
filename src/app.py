from flask import Flask, render_template, request
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
        return f"{self.course_name} | {self.completion_status}"

#index page
@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == "post":
        title = request.form['title']
        desc = request.form['desc']
        status = courses(course_name=title, completion_status=desc)
        db.session.add(status)
        db.session.commit()
    allCourses = courses.query.all()
    return render_template('index.html', allCourses=allCourses)

#login page
@app.route("/login")
def login():
    allCourses = courses.query.all()
    print(allCourses)
    return "login page"