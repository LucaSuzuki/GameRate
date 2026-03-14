from os import name

from main import app
from flask import render_template, request, redirect, url_for

lista_ratings = []
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form["nome"]
    nota = request.form["nota"]

    if nome != "" and nota != "":
        lista_ratings.append({"nome": nome, "nota": nota})

    return redirect(url_for("ratings"))
@app.route("/ratings")
def ratings():
    return render_template("ratingPage.html", ratings=lista_ratings)

