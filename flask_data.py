from flask import Flask

import json

from model import (
    session as db_session,
    User,
)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello hello"


@app.route("/users")
def view_all_users():
    user_list = db_session.query(User).all()
    return json.dumps(user_list)

if __name__ == "__main__":
    app.run(debug=True)
