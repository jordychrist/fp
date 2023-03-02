import os
import time
import random

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///TL.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    # Show information on tickets held
    if request.method == "GET":
        user_id = session["user_id"]
        events = db.execute("SELECT date, time, name, price, SUM(qty) as all_tickets FROM events WHERE user_id = ? GROUP BY name HAVING all_tickets > 0", user_id)
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        # This shows cash remaining after ticket prices subtracted
        total = int(cash)
        
        # Multiply ticket price by qty for all events
        for event in events:
            total -= int(event["price"]) * int(event["all_tickets"])
    
        # Check user for purchased tickets, and flash a message.
        check = db.execute("SELECT COUNT(qty) FROM events WHERE user_id = ?", user_id)

        # If user has a ticket, send a flash message
        if check[0]["COUNT(qty)"] >= 1:
            flash("message")

        return render_template("index.html", events=events, total=usd(total), usd=usd)
    else:
        user_id = session["user_id"]
        loan = request.form.get("loan")

        # Confirm valid information provided for loan request
        if not loan:
            return apology("Enter a loan amount")
        if int(loan) > 10000:
            return apology("Maximum loan amount $10,000")

        # Provides the additional requested money to the users account
        if int(loan) <= 10000:
            cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
            cash += int(loan)
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, user_id)

        return redirect("/")


@app.route("/drawing", methods=["GET", "POST"])
@login_required
def drawing():
    # Lottery drawing page
    if request.method == "GET":
        user_id = session["user_id"]
    
        # Check what events the user is part of
        try:
            events = db.execute("SELECT name, qty FROM events WHERE user_id = ? GROUP BY name", user_id)[0]
        # If none, send them to event page
        except:
            return redirect("/events")
        
        # If event found label id for img pulling
        events1 = events["name"].upper()
        if events1 == "BURNING MAN":
            id = 5
        elif events1 == "TAYLOR SWIFT":
            id = 6
        elif events1 == "ULTRA":
            id = 7
        elif events1 == "EDC":
            id = 8
        
        # Compares user id to username
        user_events = events["name"]
        people = db.execute("SELECT user_id, SUM(qty) as total FROM events WHERE name = ? GROUP BY user_id HAVING total > 0", user_events)
        names = db.execute("SELECT id, username FROM users")

        ids = []
        name_list = []

        # Provide user ids to the list from the database
        for person in people:
          ids.append(person["user_id"])
        
  
        # Create a username list of all ticket holders
        for name in names:
            for id1 in ids:
                if id1 == name["id"]:
                    name_list.append(name["username"])

        # Choose a random winner
        rng = random.randint(1 , len(name_list))
        winner = name_list[rng-1]

        return render_template("drawing.html", events1=events1, id=id, winner=winner, name_list=name_list)
    else:
        return apology("temp")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]

    # Get all historical data for current user
    events = db.execute("SELECT date, time, name, price, SUM(qty) as all_tickets FROM events WHERE user_id = ? GROUP BY name HAVING all_tickets > 0", user_id)

    return render_template("history.html", events=events, usd=usd)

@app.route("/home")
def home():
    """Homepage"""
    
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/events", methods=["GET", "POST"])
@login_required
def events():
    """Lookup events."""
    if request.method == "POST":
        event = request.form.get("event").lower()

        if not event:
            return apology("must enter an event")
        
        # Lookup event info
        info = db.execute("SELECT id, date, time, location, price FROM pending WHERE name = ?", event)
        
        # Check if user has any tickets to events
        try:
            id = info[0]["id"]
        except:
            return apology("Event not found")
        date = info[0]["date"]
        time = info[0]["time"]
        loc = info[0]["location"]
        price = int(info[0]["price"])

        db.execute("DELETE FROM slush")
        db.execute("INSERT INTO slush (name) VALUES (?)", event)
        return render_template("event_results.html", id=id, name=event.upper(), date=date, time=time, loc=loc, price=usd(price))

    else:
        return render_template("events.html")
    

@app.route("/event_results", methods=["GET", "POST"])
@login_required
def event_results():
    """Event results and buy"""
    if request.method == "POST":
        qty = str(request.form.get("qty"))
        name1 = db.execute("SELECT name FROM slush")[0]
        name = name1["name"]

        user_id = session["user_id"]

        if not qty:
            return apology("must enter a number of tickets")
        
        pending = db.execute("SELECT date, time, price, location FROM pending WHERE name = ?", name)[0]
        time = pending["time"]
        price = pending["price"]
        date = pending["date"]
        location = pending["location"]

        db.execute("INSERT INTO events (name, date, price, qty, time, user_id, location) VALUES (?, ?, ?, ?, ?, ?, ?)", name, date, price, qty, time, user_id, location)

        return redirect("/")
    else:
        return render_template("events.html")





@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Confirm user provides all information
        if not email:
            return apology("You must enter a valid email")
        if not username:
            return apology("You must type a username")
        if not password:
            return apology("You must type a password")
        if password != confirmation:
            return apology("Passwords do not match")

        # Hash the password for security
        hashed = generate_password_hash(password)

        # Add new user to the database if they don't exist.
        try:
            db.execute("INSERT INTO users (email, username, hash) VALUES (?, ?, ?)", email, username, hashed)
        except:
            return apology("Username already exists")

        return redirect("/login")

    else:
        return render_template("register.html")