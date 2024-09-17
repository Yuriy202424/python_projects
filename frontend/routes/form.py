from flask import render_template, request
from .. import app


@app.get("/questioning")
def result():
        return render_template("form.html")
