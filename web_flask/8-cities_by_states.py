#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from models import storage
from flask import Flask, render_template
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def index():
    """Displays a list of all states with a description"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
