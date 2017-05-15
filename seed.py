"""Utility file to seed database."""

from server import app
from models import Airport, Country, Region, connect_to_db, db
import csv


#####

def load_airports():
    """Load airports from CSV file into database."""

    Airport.query.delete()

    with open('static/data/airports.csv', 'rb') as csvfile:
        next(csvfile)
        airports_reader = csv.reader(csvfile)
        for row in airports_reader:
            airport_id = row[0]
            name = row[3]
            code = row[13]          # iata_code
            latitude_deg = row[4]
            longitude_deg = row[5]
            continent = row[7]
            iso_country = row[8]
            iso_region = row[9]
            municipality = row[10]

            # if iata_code is empty, try local_code
            if code == '':
                code = row[14]

            # if local_code is also empty, try gps_code
            if code == '':
                code = row[12]

            airport = Airport(airport_id=airport_id,
                              name=name,
                              code=code,
                              latitude_deg=latitude_deg,
                              longitude_deg=longitude_deg,
                              continent=continent,
                              iso_country=iso_country,
                              iso_region=iso_region,
                              municipality=municipality)

            db.session.add(airport)

        db.session.commit()


def load_countries():
    """Load countries from CSV file into database."""

    Country.query.delete()

    with open('static/data/countries.csv', 'rb') as csvfile:
        next(csvfile)
        countries_reader = csv.reader(csvfile)
        for row in countries_reader:
            code = row[1]
            name = row[2]

            country = Country(code=code,
                              name=name)

            db.session.add(country)

        db.session.commit()


def load_regions():
    """Load regions from CSV file into database."""

    Region.query.delete()

    with open('static/data/regions.csv', 'rb') as csvfile:
        next(csvfile)
        regions_reader = csv.reader(csvfile)
        for row in regions_reader:
            code = row[1]
            name = row[3]

            region = Region(code=code,
                            name=name)

            db.session.add(region)

        db.session.commit()


#####

def call_all_functions():
    """Call all seeding functions."""

    load_countries()
    load_regions()
    load_airports()


if __name__ == "__main__":

    connect_to_db(app)
    db.create_all()
    call_all_functions()
