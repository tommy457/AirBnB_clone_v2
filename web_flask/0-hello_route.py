#!/usr/bin/python3
"""Module that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    """Entry point runs the server"""
    app.run(host="0.0.0.0")
