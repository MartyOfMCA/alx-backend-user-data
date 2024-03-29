#!/usr/bin/env python3
"""
Define a basic Flask application to handle
requests to the index route.
"""
from flask import (
        Flask,
        jsonify,
        request
        )

from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route(
        "/",
        strict_slashes=False
        )
def index():
    """
    Handle request to the index endpoint.
    """
    return (jsonify({"message": "Bienvenue"}))


@app.route(
        "/users",
        methods=["POST"],
        strict_slashes=False
        )
def register():
    """
    Handle requests to register a new user.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user_created = AUTH.register_user(email, password)
        return (jsonify({"email": email, "message": "user created"}))
    except ValueError:
        return (jsonify({"message": "email already registered"}), 400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
