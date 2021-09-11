#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Return a string as a content"""
    return 'Hello HBNB!'
    

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return a string as a content"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Return a string as a content"""
    text = text.replace('_', ' ')
    return 'C ' + text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Return a string as a content"""
    text = text.replace('_', ' ')
    return 'Python ' + text


@app.route('/number/<int:n>', strict_slashes=False)
def is_int(n):
    """Return a string as a content"""
    if type(n) == int:
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_int_template(n):
    """Return a string as a content"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
