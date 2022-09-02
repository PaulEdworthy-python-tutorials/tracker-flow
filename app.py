import os

# remove at some point
# from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

# configure app (it tells the os the webapp starts here)
app = Flask(__name__)

# Ensure templates auto reload
app.config["TEMPLATES_AUTO_RELOAD"] = True

# config SQL to work with CS50 library
# db = SQL("sqlite:///dbname_here.db")

# ensure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

@app.route('/')
@login_required
def index():
    current_user = session["user_id"]
