#!/usr/bin/env python3

from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from flask import redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def message_Bienvenue() -> str:
    msg = {"message": "Bienvenue"}
    return jsonify(msg)


@app.route('/users', methods=['POST'])
def users() -> str:

    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.users(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    
    msg = {"email": email, "message": "user created"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
