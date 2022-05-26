#!/usr/bin/env python3
""" module for a flask app
"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route('/', strict_slashes=False)
def index():
    """ basic Flask app returning message """
    return jsonify(message='Bienvenue')


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ method to register user """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email,
                        "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ method to check if email and pass are valid
        and generate session id for login
    """
    email = request.form.get('email')
    password = request.form.get('password')
    resp = make_response()
    if AUTH.valid_login(email=email, password=password):
        sess_id = AUTH.create_session(email=email)
        resp = make_response(jsonify({"email": email,
                                      "message": "logged in"}))
        resp.set_cookie("session_id", sess_id)
        return resp
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ function to destroy session of logged in user
    """
    session_id = request.form.get('session_id')
    usr = AUTH.get_user_from_session_id(session_id)
    if not session_id or not usr:
        abort(403)
    AUTH.destroy_session(usr.id)
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
