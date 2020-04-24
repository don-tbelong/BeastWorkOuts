from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Student(db.Model):
    studentId = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def toDict(self):
        return {
            "Student Id": self.studentId,
            "email": self.email,
            "password": self.password
        }

    # hashes the password parameter and stores it in the object
    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    # Returns true if the parameter is equal to the object's password property
    def check_password(self, password):
        return check_password_hash(self.password, password)

    # To String method
    def __repr__(self):
        return '<Student Id {}>'.format(self.studentID)