#!/usr/bin/python3
"""Modeul that starts a Flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """Display a list of states"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def cities_by_state_id(id):
    """Display a list of cities by state id"""
    states = storage.all(State)
    state = states[f"State.{id}"]
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def teardown(error):
    storage.close()


if __name__ == "__main__":
    """Entry point runs the server"""
    app.run(host="0.0.0.0")
