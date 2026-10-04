from flask import Flask, render_template, request, redirect
from database import create_table, get_connection

app = Flask(__name__)

create_table()


@app.route("/")
def home():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("index.html", employees=employees)


@app.route("/ajouter", methods=["POST"])
def ajouter():
    nom = request.form["nom"]
    knia = request.form["knia"]
    maham = request.form["maham"]

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO employees (nom, knia, maham) VALUES (%s, %s, %s)",
        (nom, knia, maham)
    )

    connection.commit()
    cursor.close()
    connection.close()

    return redirect("/")


@app.route("/supprimer/<int:id>", methods=["POST"])
def supprimer(id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id = %s",
        (id,)
    )

    connection.commit()
    cursor.close()
    connection.close()

    return redirect("/")


@app.route("/supprimer-tout", methods=["POST"])
def supprimer_tout():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM employees")

    connection.commit()
    cursor.close()
    connection.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
