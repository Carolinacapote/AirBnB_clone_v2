#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from models import storage
from flask import Flask, render_template
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id=None):
    """Displays a State if one is found with this id"""
    states = storage.all(State)

    for state in states.values():
        if state.id == id:
            return  render_template('9-states.html', state=state, id=id)

        else:
            return render_template('9-states.html', state=None, id=id)

    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
