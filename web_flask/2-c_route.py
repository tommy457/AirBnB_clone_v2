#!/usr/bin/python3
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


if __name__ == "__main__":
    """Entry point runs the server"""
    app.run(host="0.0.0.0")
