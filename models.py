"""Models and database functions."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#####

class Airport(db.Model):
    """Airport."""

    __tablename__ = "airports"

# "id","ident","type","name","latitude_deg","longitude_deg","elevation_ft","continent",
# "iso_country","iso_region","municipality","scheduled_service","gps_code","iata_code","local_code",
# "home_link","wikipedia_link","keywords"
# 3878,"KSFO","large_airport","San Francisco International Airport",37.61899948120117,-122.375,13,"NA",
# "US","US-CA","San Francisco","yes","KSFO","SFO","SFO",
# "http://www.flysfo.com/","http://en.wikipedia.org/wiki/San_Francisco_International_Airport","QSF, QBA"

    airport_id = db.Column(db.Integer, autoincrement=False, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    iata_code = db.Column(db.String(10), nullable=False)
    latitude_deg = db.Column(db.Integer, nullable=False)
    longitude_deg = db.Column(db.Integer, nullable=False)
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

# "id","code","name","continent","wikipedia_link","keywords"
# 302672,"AD","Andorra","EU","http://en.wikipedia.org/wiki/Andorra",

    __tablename__ = "countries"

    code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Country code=%s name=%s>" % (self.code,
                                              self.name)


class Region(db.Model):
    """Region codes corresponding to region names."""

# "id","code","local_code","name","continent","iso_country","wikipedia_link","keywords"
# 302811,"AD-02",02,"Canillo","EU","AD","http://en.wikipedia.org/wiki/Canillo",

    __tablename__ = "regions"

    code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Region code=%s name=%s>" % (self.code,
                                             self.name)


#####


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///air-anywhere'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."
