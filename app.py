from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL Database Configuration
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="12345",
    database="project_registration"
)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Get user input from the form
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        sex = request.form["sex"]
        age = request.form["age"]

        # Insert the data into the MySQL database
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (first_name, last_name, email, sex, age) VALUES (%s, %s, %s, %s, %s)",
                       (first_name, last_name, email, sex, age))
        db.commit()
        cursor.close()

        return redirect(url_for("success"))

    return render_template("registration.html")

@app.route("/success")
def success():
    return "Registration successful!"

if __name__ == "__main__":
    app.run(debug=True)
