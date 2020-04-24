from flask import Flask
import json

from models import db
from models import User


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

@app.route('/')
def index():
    bob = User(username="bob", email="bob@mail.com")  # creates an object from the User class/model
    bob.set_password("bobpass")  # use method to hash password
    john = User(username="john", email="john@mail.com")
    john.set_password('johnpass')
    users = [bob.toDict(), john.toDict()]
    return json.dumps(users)  # prints a json string representation of our object


app.run(host='0.0.0.0', port=8080, debug=True)
