from os import name

from main import app, get_connection
from flask import render_template, request, redirect, url_for

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form["nome"]
    nota = request.form["nota"]

    if nome.strip() and nota.strip():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO ratings (nome, nota) VALUES (%s, %s)",
            (nome, nota)
        )

        conn.commit()
        conn.close()

    return redirect(url_for("ratings"))
@app.route("/ratings")
def ratings():
    conn = get_connection()
    cursor = conn.cursor()
    print(conn, cursor)
    cursor.execute("SELECT nome, nota FROM ratings")
    dados = cursor.fetchall()

    conn.close()
    return render_template("ratingPage.html", ratings=dados)