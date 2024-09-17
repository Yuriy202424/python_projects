from flask import render_template, request, flash, redirect, url_for
from .. import app

@app.post("/letters")
def letter():
    fav_word = request.form.get('fav_word')
    age = request.form.get('age')
    gmail = request.form.get('gmail')
    name = request.form.get('name')
    print(" NAME " * 20)
    print(name)
    
    try:
        age = int(age)
    except ValueError:
        flash("Некорректный возраст")
        return render_template("form.html", fav_word=fav_word)

    if not name.isalpha():
        flash("Имя должно состоять только из букв")
        return render_template("form.html", fav_word=fav_word)
    
    if age < 10 or age > 60:
        flash("Некорректный возраст")
        return render_template("form.html", fav_word=fav_word)

    nickname = gmail.split('@')[0]

    return render_template("esse.html", age=age, gmail=gmail, nickname=nickname, name=name, fav_word=fav_word)
