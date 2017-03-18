""" Server file for connect++ """

from jinja2 import StrictUndefined

from flask import Flask, jsonify, render_template, redirect, request, flash, session, g

from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABCDE"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True




@app.route("/")
def index():
    """renders landing page"""

    return render_template("index.html")


@app.route("/company/apple")
def display_apple():
    """shows company details"""

    name = "Apple"

    return render_template("company_info.html", name=name)


@app.route("/company/google")
def display_google():
    """shows company details"""

    name = "Google"

    return render_template("company_info.html", name=name)


@app.route("/company/facebook")
def display_facebook():
    """shows company details"""

    name = "Facebook"

    return render_template("company_info.html", name=name)


@app.route("/survey")
def show_survey():
    """renders survey"""

    return render_template("survey.html")


@app.route("/faq")
def faq():
    """renders faq page"""

    return render_template("faq.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = False

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
