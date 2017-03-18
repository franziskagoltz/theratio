from model import Company, Number, connect_to_db, db
from server import app
from datetime import datetime


def load_companies():
    """Load companies from companies.txt into database."""

    print "Companies"

    Company.query.delete()

    for row in open("seed_data/companies.txt"):
        name = row.rstrip()
        company = Company(name=name)

        db.session.add(company)

    db.session.commit()


# def load_numbers():
#     """Load numbers from numbers.txt into database."""

#     print "Numbers"

#     Number.query.delete()

#     for row in open("seed_data/companies.txt"):
#         row = row.rstrip()
#         percent_women, percent_womentech, percent_womenleaders, nps_score = row.split("|")
#         date = datetime.now()
#         number = Number(percent_women=percent_women,
#                         percent_womentech=percent_womentech,
#                         percent_womenleaders=percent_womenleaders,
#                         date=date,
#                         nps_score=nps_score)
#         db.session.add(number)

#     db.session.commit()



# def load_users():
#     """Load users from users_data into database."""

#     print "Users"

#     User.query.delete()

#     for row in open("seed_data/users.txt"):
#         row = row.rstrip()
#         user_id, first_name, last_name, email, password = row.split("|")

#         user = User(user_id=user_id,
#                     first_name=first_name,
#                     last_name=last_name,
#                     email=email,
#                     password=password)

#         db.session.add(user)

#     db.session.commit()


if __name__ == '__main__':
    connect_to_db(app)

    db.create_all()

    load_companies()

    load_numbers()