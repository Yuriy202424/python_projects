from flask import render_template, request, redirect, url_for
from .. import app

@app.post("/favouring")
def favouring():
    fav_word = request.form.get('fav_word')
    return render_template("form.html", fav_word=fav_word)
