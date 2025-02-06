# ===================================================
#                   IMPORTS SECTION
# ===================================================

# Standard library imports
import os

# Third-party libraries
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash

# Local imports
from helpers import login_required, db_execute


# ===================================================
#                FLASK CONFIGURATION
# ===================================================

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

app.config["SESSION_PERMANENT"] = True

# Database configuration using environment variables
app.config["DATABASE"] = {
    "host": os.getenv("DBHOST"),
    "dbname": os.getenv("DBNAME"),
    "user": os.getenv("DBUSER"),
    "password": os.getenv("DBPASSWORD")
}


# ===================================================
#                ROUTE HANDLERS
# ===================================================

@app.route("/")
def index():
    if not session:
        return redirect("/login")
    
    return render_template("index.html")


@app.route("/contact")
@login_required
def contact():
    return render_template("contact.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "GET":
        return render_template("login.html")
    
    username = request.form.get("usernameInput")
    password = request.form.get("passwordInput")

    if not username or not password:
        flash("You must fill in all fields.", "warning")
        return render_template("login.html")
    
    rows = db_execute("""
        SELECT *
        FROM users
        WHERE username ILIKE %s
    """, params=[username], return_value=True) # gets the user information

    if len(rows) != 1 or not check_password_hash(
        rows[0]["hash"], password # compares "hash" field with the typed password in hash function
    ):
        flash("Invalid username and/or password.", "warning")
        return render_template("login.html")
    
    session["user_id"] = rows[0]["id"] # creates a new active session with the user id

    return redirect("/")


@app.route("/logout", methods=["POST"])
@login_required
def logout():
    session.clear()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()

    if request.method == "GET":
        return render_template("register.html")
    
    username = request.form.get("usernameInput")
    password = request.form.get("passwordInput")
    confirm_password = request.form.get("confirmPasswordInput")

    if not username or not password or not confirm_password:
        flash("You must fill in all fields.", "warning")
        return render_template("register.html")
    
    if password != confirm_password:
        flash("Check if you confirmed your password correctly.", "warning")
        return render_template("register.html")
    
    username_is_already_taken = db_execute("""
        SELECT 1
        FROM users
        WHERE username = %s
    """, params=[username], return_value=True)

    if username_is_already_taken:
        flash("Sorry, this username is already taken. Please choose another.", "warning")
        return render_template("register.html")
    
    password_hash = generate_password_hash(password)

    db_execute("""
        INSERT INTO users (username, hash)
        VALUES (%s, %s)
    """, params=[username, password_hash])

    flash("Registration successful! You can now log in to your account.", "success")
    return render_template("login.html")


@app.route("/tester-login")
def tester_login():
    session.clear()
    session["user_id"] = 1
    
    return redirect("/")


# ===================================================
#                ERROR HANDLERS
# ===================================================

@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('errors/405.html'), 405


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html'), 500
    

# ===================================================
#                APP RUN CONFIGURATION
# ===================================================

if __name__ == "__main__":
    app.run(debug=True)
#           ^^^^^^^^^^ REMOVE THIS PARAMETER IN PRODUCTION