import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

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
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("TODO index")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    user_id = session["user_id"][0]["id"]
    if request.method == "POST":

        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")
        lookup_amount= lookup(symbol)

        if not request.form.get("symbol"):
            return apology("Please enter a symbol",403)
        elif not request.form.get("shares"):
            return apology("Please enter an amout of shares",403)
        elif lookup_amount is None:
            return apology("Symbol doesn't exist", 403)

        try:
            if float(shares)  <= 0 :
                return apology("Please enter a positive integer for shares", 403)
        except ValueError:
            return apology("Please enter a valid number of shares", 403)

        rows = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash = int(rows[0]["cash"])
        price = lookup_amount["price"]
        shares_amount = float(shares) * float(price)
        print(shares_amount)
        print(cash)
        print()


        if shares_amount > cash:
            return apology("Sorry you do not have enough money", 403)
        else:
            cash_left = cash - shares_amount
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            db.execute("UPDATE users set cash = ? WHERE id = ?", cash_left,user_id)
            db.execute("INSERT INTO transactions(user_id,symbol,shares,price,date)VALUES(?,?,?,?,?)",user_id,symbol,shares,price,date)
            transactions = db.execute("SELECT * FROM transactions WHERE user_id= ? ORDER BY id DESC LIMIT 1", user_id)
            print(transactions)

            return render_template("/portfolio.html", transactions = transactions)

    else:
        return render_template("/buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO history")


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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not request.form.get("symbol"):
            return apology("Please enter a symbol",403)
        elif lookup(symbol) is None:
            return apology("Symbol doesn't exist", 403)

        if lookup(symbol):
            stock = lookup(symbol)
            stock_info= {
                "name": stock["name"],
                "price": stock["price"],
                "symbol": stock["symbol"]
            }
            return render_template("/quoted.html", stock_info = stock_info)
    else:
        return render_template("/quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # """Register user"""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not request.form.get("username"):
            return apology("Please enter a username",403)
        elif not request.form.get("password"):
            return apology("Please enter a password", 403)
        elif not request.form.get("confirmation"):
            return apology("Please enter a confirmation password", 403)

        if confirmation != password :
            return apology("Confirmation password does not match, try again", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) > 0 :
            return apology("Username already in use",400)

        hashed_password = generate_password_hash(password)
        db.execute("INSERT INTO users(username,hash) VALUES (?,?)", username,hashed_password)
        return redirect("/")

    else:
        return render_template("/register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():

    """Sell shares of stock"""
    return apology("TODO sell")
