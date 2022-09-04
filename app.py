import os

# remove at some point
# from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
# from werkzeug.security import check_password_hash, generate_password_hash
# from datetime import datetime

# configure app (it tells the os the webapp starts here)
app = Flask(__name__)

# Ensure templates auto reload
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "python#001"
Session(app)

# config SQL to work with CS50 library
# db = SQL("sqlite:///dbname_here.db")


@app.route('/')
# @login_required
def index():
    # current_user = session["user_id"]
    session["secrrt"]='sec'

    # username = "Paul"

    return render_template("/index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":

        username = request.form.get("username")

        # username admin is admin, dev is dev
        session["user_id"] = username

        return redirect("/")

    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")


if __name__ == '__main__':
    app.run()
