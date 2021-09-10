#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'
    

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return 'C' + '%s' % text


@app.route('/python/(<text>)', strict_slashes=False)
def python_text(text):
    text = text.replace('_', ' ')
    return 'C' + '%s' % text

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
