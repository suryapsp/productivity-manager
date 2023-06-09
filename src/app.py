from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

#config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


#database
class courses(db.Model):
    course_name = db.Column(db.String(100), primary_key=True)
    completion_status = db.Column(db.String(30), nullable=False)

    def __repr__(self) -> str:
        return f"{self.course_name} | {self.completion_status}"

#index page
@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        status = courses(course_name=title, completion_status=desc)
        db.session.add(status)
        db.session.commit()
    allCourses = courses.query.all()
    return render_template('index.html', allCourses=allCourses)

#delete
@app.route("/delete/<course_name>")
def delete(course_name):
    course = courses.query.filter_by(course_name = course_name).first()
    db.session.delete(course)
    db.session.commit()
    return redirect("/")