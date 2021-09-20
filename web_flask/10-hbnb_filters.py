#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from models import storage
from flask import Flask, render_template
from models.state import State
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def index():
    """Displays an AirBnB html page """
    states = storage.all(State)
    cities = storage.all(City)
    amenities = storage.all(Amenity)

    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
