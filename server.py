"""Travel destination app."""

from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
# from flask_debugtoolbar import DebugToolbarExtension
from models import Airport, Country, Region, connect_to_db
from datetime import datetime

db = SQLAlchemy()
app = Flask(__name__)
app.secret_key = 'skahgwgjrnwrijog'
app.jinja_env.undefined = StrictUndefined


#####

@app.route('/')
def index():
    """Displays homepage.

    Homepage contains Origin Location field and Find a Destination button."""

    airports = db.session.query(Airport.name, Airport.code).all()

    return render_template('homepage.html',
                           airports=airports)


@app.route('/find-destination', methods=['POST'])
def find_destination():
    """Generates random destination and loads flight information."""

    pass


#####

if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
