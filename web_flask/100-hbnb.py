#!/usr/bin/python3
"""Modeul that starts a Flask web application"""
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display a list of states, cities, places and amenities"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)

    return render_template("100-hbnb.html",
                           states=states,
                           places=places,
                           amenities=amenities
                           )


@app.teardown_appcontext
def teardown(error):
    storage.close()


if __name__ == "__main__":
    """Entry point runs the server"""
    app.run(host="0.0.0.0")
