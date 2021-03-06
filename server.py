"""Travel destination app."""

from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
# from flask_debugtoolbar import DebugToolbarExtension
from models import Airport, Country, Region, connect_to_db
# from datetime import datetime

db = SQLAlchemy()
app = Flask(__name__)
app.secret_key = 'skahgwgjrnwrijog'
app.jinja_env.undefined = StrictUndefined


#####

@app.route('/')
def index():
    """Displays homepage.

    Homepage contains Origin Location field and Find a Destination button."""

    airports = db.session.query(Airport.name, Airport.code).filter(Airport.code != '').all()

    return render_template('homepage.html',
                           airports=airports)


@app.route('/find-destination', methods=['POST'])
def find_destination():
    """Generates random destination and loads flight information."""

    origin_airport = request.form.get('origin_airport')

    # Check for invalid empty request.
    if origin_airport == '':
        return jsonify({'is_valid_request': False})

    origin_airport_list = origin_airport.split('(')
    origin_airport_code = origin_airport_list[1][:-1]

    session['origin_airport'] = origin_airport_code
    print session['origin_airport']

    destination = db.session.query(Airport).filter((Airport.code != '') & \
                                                   (Airport.code != session['origin_airport']) & \
                                                   (Airport.size == 'large_airport'))\
                                           .order_by(func.random()).limit(1).first()

    destination_dict = {'is_valid_request': True,
                        'destination_name': destination.name,
                        'destination_code': destination.code}

    return jsonify(destination_dict)


#####

if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
