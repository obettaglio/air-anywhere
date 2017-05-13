"""Travel destination app."""

from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime

db = SQLAlchemy()

app = Flask(__name__)

app.secret_key = 'skahgwgjrnwrijog'

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Displays homepage.

    Homepage contains Origin Location field and Find a Destination button."""

    return render_template('homepage.html')


@app.route('/load-destination', methods=['POST'])
def load_destination():
    """Generates random destination and loads flight information."""

    pass


#####


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///air-anywhere'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
