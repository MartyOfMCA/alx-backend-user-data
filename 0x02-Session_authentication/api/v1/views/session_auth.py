#!/usr/bin/env python3
"""
Define a module that defines endpoint
handlers to all routes for Session
authentication.
"""
from flask import (
        request,
        jsonify
        )
from os import getenv

from api.v1.views import app_views
from models.user import User
from api.v1.auth.session_auth import SessionAuth


@app_views.route(
        "/auth_session/login",
        strict_slashes=False,
        methods=["POST"]
        )
def login():
    """
    Handle user login requests.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if (not email or email == ""):
        return (jsonify({"error": "email missing"}), 400)

    if (not password or password == ""):
        return (jsonify({"error": "password missing"}), 400)

    list_of_users = User.search({"email": email})
    if (len(list_of_users) == 0):
        return (jsonify({"error": "no user found for this email"}), 404)

    user = list_of_users[0]
    if (not user.is_valid_password(password)):
        return (jsonify({"error": "wrong password"}), 401)

    from api.v1.app import auth
    new_session_id = auth.create_session(user.id)

    response = jsonify(user.to_json())
    response.set_cookie(getenv("SESSION_NAME"), new_session_id)

    return (response)
