"""Models and database functions for THE:RATIO project."""

from flask_sqlalchemy import SQLAlchemy


# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


class Company(db.Model):
    """Companies in the:ratio."""

    __tablename__ = "companies"

    company_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return "company id={}, name={}".format(
            self.company_id, self.name)


class Number(db.Model):
    """diversity numbers"""

    __tablename__ = "numbers"

    number_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.company_id"), nullable=False)
    percent_women = db.Column(db.Integer)
    percent_womentech = db.Column(db.Integer)
    percent_womenleaders = db.Column(db.Integer)
    nps_score = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return "company id={}, percent_women={} percent_womentech={} percent_womenleaders={}".format(
            self.company_id, self.percent_women, self.percent_womentech, self.percent_womenleaders)


class User(db.Model):
    """User of the:ratio website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "User id={} email={}".format(
            self.user_id, self.email)


class Survey(db.Model):
    """Survey of the:ratio website."""

    __tablename__ = "surveys"

    suvery_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.company_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    def __repr__(self):
        return "Survey id={} company_id={} user_id={}".format(
            self.suvery_id, self.company_id, self.user_id)


class Attribute(db.Model):
    """Attribute of the:ratio website."""

    __tablename__ = "attributes"

    attribute_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    suvery_id = db.Column(db.Integer, db.ForeignKey("surveys.suvery_id"), nullable=False)
    question = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "attribute_id={} Survey id={}".format(
            self.attribute_id, self.suvery_id)


class Response(db.Model):
    """Survey response of the:ratio website."""

    __tablename__ = "responses"

    response_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    attribute_id = db.Column(db.Integer, db.ForeignKey("attributes.attribute_id"), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.company_id"), nullable=False)
    response = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "response_id={} response={}".format(self.response_id, self.response)


def connect_to_db(app, db_uri='postgresql:///theratio'):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)
