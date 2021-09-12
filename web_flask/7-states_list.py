#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def index():
    """Displays a template with a list of cities of a specific state"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
