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


class Classroom(db.Model):
    """Classroom."""

    __tablename__ = "classrooms"

    class_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    user_email = db.Column(db.String(200), db.ForeignKey('users.user_email'))
    subject_code = db.Column(db.String(4), db.ForeignKey('subjects.subject_code'))
    start_date = db.Column(db.DateTime, nullable=False)
    period = db.Column(db.Integer, nullable=True)
    year = db.Column(db.String(10), nullable=True)
    school = db.Column(db.String(50), nullable=True)

    user = db.relationship('User',
                           backref=db.backref("classrooms",
                                              order_by=class_id))
    subject = db.relationship('Subject',
                              backref=db.backref("classrooms",
                                                 order_by=class_id))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Classroom class_id=%s user_email=%s>" % (self.class_id,
                                                          self.user_email)


class Exam(db.Model):
    """Test or quiz."""

    __tablename__ = "exams"

    exam_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    topic = db.Column(db.String(100), nullable=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classrooms.class_id'))
    total_points = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    classroom = db.relationship('Classroom',
                                backref=db.backref("exams",
                                                   order_by=exam_id))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Exam exam_id=%s name=%s>" % (self.exam_id,
                                              self.name)


class ExamResult(db.Model):
    """Result of exam."""

    __tablename__ = "examresults"

    examresult_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.exam_id'))
    student_email = db.Column(db.String(200), db.ForeignKey('students.student_email'))
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<ExamResult examresult_id=%s exam_id=%s student_email=%s>" % (self.examresult_id,
                                                                              self.exam_id,
                                                                              self.student_email)


class Exercise(db.Model):
    """Exercise on Khan Academy."""

    __tablename__ = "exercises"

    exercise_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    is_quiz = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Exercise exercise_id=%s name=%s>" % (self.exercise_id,
                                                      self.name)


class ExerciseResult(db.Model):
    """Result of exercise."""

    __tablename__ = "exerciseresults"

    exerciseresult_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.exercise_id'))
    student_email = db.Column(db.String(200), db.ForeignKey('students.student_email'))
    timestamp = db.Column(db.DateTime, nullable=False)
    num_correct = db.Column(db.Integer, nullable=True)
    num_done = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<ExerciseResult exerciseresult_id=%s exercise_id=%s student_email=%s>" % (self.exerciseresult_id,
                                                                                          self.exercise_id,
                                                                                          self.student_email)


class Video(db.Model):
    """Video on Khan Academy."""

    __tablename__ = "videos"

    video_id = db.Column(db.String(50), autoincrement=False, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    url = db.Column(db.String(200), nullable=False)
    youtube_url = db.Column(db.String(200), nullable=True)
    topic = db.Column(db.String(100), nullable=True)
    length = db.Column(db.Integer, nullable=False)
    order_num = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Video video_id=%s name=%s>" % (self.video_id,
                                                self.name)


class VideoResult(db.Model):
    """Result of video."""

    __tablename__ = "videoresults"

    videoresult_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    video_id = db.Column(db.String(50), db.ForeignKey('videos.video_id'))
    student_email = db.Column(db.String(200), db.ForeignKey('students.student_email'))
    timestamp = db.Column(db.DateTime, nullable=False)
    points = db.Column(db.Integer, nullable=True)
    secs_watched = db.Column(db.Integer, nullable=True)
    last_sec_watched = db.Column(db.Integer, nullable=True)

    video = db.relationship('Video',
                            backref=db.backref("videoresults",
                                               order_by=videoresult_id))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<VideoResult videoresult_id=%s video_id=%s student_email=%s>" % (self.videoresult_id,
                                                                                 self.video_id,
                                                                                 self.student_email)


#####

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///project'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."
