#!/usr/bin/python3
"""Modeul that starts a Flask web application"""
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Display a list of states, cities and amenities"""
    states = storage.all(State)
    amenities = storage.all(Amenity)

    return render_template("10-hbnb_filters.html",
                           flag=True,
                           states=states,
                           amenities=amenities
                           )


@app.teardown_appcontext
def teardown(error):
    storage.close()


if __name__ == "__main__":
    """Entry point runs the server"""
    app.run(host="0.0.0.0")
