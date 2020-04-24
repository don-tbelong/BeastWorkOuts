from flask import Flask, render_template
import json

from models import db
from models import Student


# app = Flask(__name__)
# begin boilerplate code

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.test.db'
    db.init_app(app)
    return app


app = create_app()

app.app_context().push()
db.create_all(app=app)


# end boilerplate code#


@app.route("/test")
def hello():
    return "Hello World!"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup", methods=['POST'])
def signup():
    data = request.get_json()
    student = Student(studentId=data['Student ID'], email=data['Email'])
    studentID.set_password(data['Password'])
    try:
        db.session.add(student)

    return render_template("signup.html")


@app.route("/workouts")
def workouts():
    return render_template("workouts.html")

# app.run(host='0.0.0.0', port=8080)
