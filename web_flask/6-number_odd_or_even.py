#!/usr/bin/python3
"""Module that starts a Flask web application"""
from flask import Flask, render_template
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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Renders a template only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Renders a template only if n is an integer"""
    odd_or_even = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html",
                           number=n,
                           odd_or_even=odd_or_even
                           )


if __name__ == "__main__":
    """Entry point runs the server"""
    app.run(host="0.0.0.0")
