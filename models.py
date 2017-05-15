"""Models and database functions."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#####

class Airport(db.Model):
    """Airport."""

    __tablename__ = "airports"

    airport_id = db.Column(db.Integer, autoincrement=False, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    latitude_deg = db.Column(db.Float, nullable=False)
    longitude_deg = db.Column(db.Float, nullable=False)
    continent = db.Column(db.String(10), nullable=False)
    iso_country = db.Column(db.String(10), db.ForeignKey('countries.code'))
    iso_region = db.Column(db.String(10), db.ForeignKey('regions.code'))
    municipality = db.Column(db.String(200), nullable=False)

    country = db.relationship('Country',
                              backref=db.backref("airports",
                                                 order_by=airport_id))
    region = db.relationship('Region',
                             backref=db.backref("airports",
                                                order_by=airport_id))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Airport name=%s country=%s>" % (self.name,
                                                 self.iso_country)


class Country(db.Model):
    """Country codes corresponding to country names."""

    __tablename__ = "countries"

    code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Country code=%s name=%s>" % (self.code,
                                              self.name)


class Region(db.Model):
    """Region codes corresponding to region names."""

    __tablename__ = "regions"

    code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Region code=%s name=%s>" % (self.code,
                                             self.name)


#####

def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///air-anywhere'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
