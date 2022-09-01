import os

# remove at some point
# from cs50 import SQL

from flask import Flask, flash, redirect, render_template, request, session
# from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

# configure app
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

# config SQL to work with CS50 library
# db = SQL("sqlite:///dbname_here.db")

# ensure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")