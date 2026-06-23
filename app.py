from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=RedundancyDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    reg_date = request.form["reg_date"]
    role = request.form["role"]


    cursor.execute(
        """
        SELECT *
        FROM Records
        WHERE Email = ?
        """,
        (email,)
    )

    existing = cursor.fetchone()

    if existing:

        message = "Duplicate Email Found! Data Not Added."

    else:

        cursor.execute(
            """
            INSERT INTO Records
            (FullName, Email, Phone, RegistrationDate, UserRole)

            VALUES (?, ?, ?, ?, ?)
            """,
            (
                name,
                email,
                phone,
                reg_date,
                role
            )
        )

        conn.commit()

        message = "Data Added Successfully."

    return render_template(
        "result.html",
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)