#!/usr/bin/env python3
"""
Define a basic Flask application to handle
requests to the index route.
"""
from flask import (
        Flask,
        jsonify
        )


app = Flask(__name__)


@app.route(
        "/",
        strict_slashes=False
        )
def index():
    """
    Handle request to the index endpoint.
    """
    return (jsonify({"message": "Bienvenue"}))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
