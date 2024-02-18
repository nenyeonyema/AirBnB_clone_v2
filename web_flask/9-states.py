#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """teardown"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State objects"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_cities_list(id):
    """Display a HTML page with cities of a specific state"""
    state = storage.get(State, id)
    if state:
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html', not_found=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
