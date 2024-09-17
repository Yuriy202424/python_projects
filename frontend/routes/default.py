from flask import render_template, request
from .. import app


@app.get("/")
def index():
    return render_template("index.html")