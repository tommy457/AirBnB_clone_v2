#!/usr/bin/python3
"""Modeul that starts a Flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Renders a template with list of states and its cities"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(error):
    """Closes the current session"""
    storage.close()


if __name__ == "__main__":
    """Entry point runs the server"""
    app.run(host="0.0.0.0")
