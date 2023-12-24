#!/usr/bin/python3
"""Module that starts a Flask web application"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays C followed by the value of the text"""
    text = escape(text.replace("_", " "))
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show(text="is cool"):
    """Displays python followed by the value of the text"""
    text = escape(text.replace("_", " "))
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """display n is a number only if n is an integer"""
    return "{} is a number".format(escape(n))


if __name__ == "__main__":
    """Entry point runs the server"""
    app.run(host="0.0.0.0")
