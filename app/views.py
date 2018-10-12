from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           user = "Альянс")

@app.route('/alliance')
def alliance():
    return render_template("alliance.html")

@app.route('/horde')
def horde():
    return render_template("horde.html")
