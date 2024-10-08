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
    #get user session
    user_id = session["user_id"][0]["id"]

    #get all
    transactions = db.execute("SELECT symbol, SUM(shares) AS total_shares FROM transactions WHERE user_id = ? AND transaction_type = ? GROUP BY symbol", user_id, "Bought")

    #create empty list
    stocks = []
    #initilize variable to zero
    total_stocks_value = 0

    #loop through transactions
    for transaction in transactions:
        symbol = transaction['symbol']
        lookup_data = lookup(symbol)

        if lookup_data:
            current_price = lookup_data['price']
            total_value = transaction['total_shares'] * current_price

            stocks.append({                                             #append data to the stocks list
                'symbol': symbol,
                'shares': transaction['total_shares'],
                'price': current_price,
                'total_value': total_value
            })
            total_stocks_value += total_value

    #get users cash
    cash = db.execute("SELECT cash FROM users WHERE id=?", user_id)[0]['cash']

    #calculate total
    grand_total = cash + total_stocks_value


    return render_template("index.html", stocks=stocks, cash=cash, total_stocks_value=total_stocks_value, grand_total=grand_total)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    #get user session
    user_id = session["user_id"][0]["id"]
    date = datetime.now().strftime("%Y-%m-%d")
    if request.method == "POST":

        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")
        lookup_all = lookup(symbol)

        if not symbol:
            return apology("Please enter a symbol", 400)
        elif not shares:
            return apology("Please enter an amout of shares", 400)
        elif lookup_all is None:
            return apology("Symbol doesn't exist", 400)
        elif not shares.isdigit():
            return apology("Please enter an positive number of shares")

        try:
            if float(shares) <= 0:
                return apology("Please enter a positive integer for shares", 400)
        except ValueError:
            return apology("Please enter a valid number of shares", 400)

        rows = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash = int(rows[0]["cash"])
        price = lookup_all["price"]
        shares_amount = float(shares) * float(price)


        if shares_amount > cash:
            return apology("Sorry you do not have enough money", 400)
        else:
            cash_value_left = cash - shares_amount

            db.execute("UPDATE users set cash = ? WHERE id = ?", cash_value_left, user_id)

            existing_transaction = db.execute("SELECT shares FROM transactions WHERE user_id = ? AND symbol = ?", user_id, symbol)

            if existing_transaction:
                # Update the shares for the existing transaction
                new_shares = existing_transaction[0]['shares'] + float(shares)
                db.execute("UPDATE transactions SET shares = ?, price = ?, date = ? WHERE user_id = ? AND symbol = ?",
                           new_shares, price, date, user_id, symbol)
            else:
                # Insert a new transaction
                db.execute("INSERT INTO transactions (user_id, symbol, shares, price, transaction_type, date) VALUES (?, ?, ?, ?, ?, ?)",
                           user_id, symbol, shares, price, "Bought", date)

            # Insert into history
            db.execute("INSERT INTO history(user_id, symbol, shares, amount, transaction_type, date) VALUES (?, ?, ?, ?, ?, ?)",
                       user_id, symbol, shares, shares_amount, "Bought", date)

            # Calculate total value
            transactions = db.execute("SELECT transactions.*, users.* FROM transactions JOIN users ON transactions.user_id = users.id WHERE transactions.user_id = ? AND transaction_type = ? GROUP BY symbol", user_id, "Bought")
            total_value = sum(transaction['shares'] * transaction['price'] for transaction in transactions) + round(cash_value_left)


            return render_template("/portfolio.html", transactions=transactions, cash_value_left=cash_value_left, total_value=total_value)


    else:
        return render_template("/buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"][0]["id"]
    history = db.execute("SELECT * FROM history WHERE user_id = ? ",user_id)


    return render_template("/history.html", history=history)


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
        stock = lookup(symbol)

        if not symbol:
            return apology("Please enter a symbol", 400)
        elif stock is None:
            return apology("Symbol doesn't exist", 400)

        if lookup(symbol):
            stock_info = {
                "name": stock["name"],
                "price": stock["price"],
                "symbol": stock["symbol"]
            }
            print(stock_info)
            return render_template("/quoted.html", stock_info=stock_info)
    else:
        return render_template("/quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # """Register user"""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Please enter a username", 400)
        elif not password:
            return apology("Please enter a password", 400)
        elif not confirmation:
            return apology("Please enter a confirmation password", 400)

        if confirmation != password:
            return apology("Confirmation password does not match, try again", 400)

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) > 0:
            return apology("Username already in use", 400)

        hashed_password = generate_password_hash(password)
        db.execute("INSERT INTO users(username,hash) VALUES (?,?)", username, hashed_password)
        return redirect("/")

    else:
        return render_template("/register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"][0]["id"]
    date = datetime.now().strftime("%Y-%m-%d")

    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")
        lookup_all = lookup(symbol)

        # Validate inputs
        if not symbol:
            return apology("Please select a stock to sell", 400)
        elif not shares:
            return apology("Please enter an amount of shares", 400)
        elif lookup_all is None:
            return apology("Symbol doesn't exist", 403)
        elif not shares.isdigit() or int(shares) <= 0:
            return apology("Please enter a positive integer for shares", 400)

        # Check if user has enough shares to sell
        transactions_shares = db.execute("SELECT SUM(shares) as total_shares FROM transactions WHERE user_id = ? AND symbol = ? AND transaction_type = ? GROUP BY symbol", user_id, symbol, "Bought")

        total_shares = transactions_shares[0]['total_shares']
        print("total shares:",total_shares)

        if int(shares) > total_shares:
            return apology("You do not own that many shares", 400)

        # Get the current price of the stock
        price = lookup_all["price"]
        shares_amount = int(shares) * price

        # Update cash balance
        rows = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash_value_left = rows[0]["cash"] + shares_amount
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash_value_left, user_id)

        # Update transactions
        new_shares = total_shares - int(shares)
        if new_shares == 0:
            # If selling all shares, delete the transaction entry
            db.execute("DELETE FROM transactions WHERE user_id = ? AND symbol = ?", user_id, symbol)
        else:
            # Update the shares for the existing transaction
            db.execute("UPDATE transactions SET shares = ?, price = ? WHERE user_id = ? AND symbol = ?",
                       new_shares, price, user_id, symbol)

        # Log the sale in history
        db.execute("INSERT INTO history(user_id, symbol, shares, amount, transaction_type, date) VALUES (?, ?, ?, ?, ?, ?)",
                   user_id, symbol, -int(shares), shares_amount, "Sold", date )


        transactions = db.execute("SELECT transactions.*, users.* FROM transactions JOIN users ON transactions.user_id = users.id WHERE transactions.user_id = ? AND transaction_type = ? GROUP BY symbol", user_id, "Bought")
        total_value = sum(transaction['shares'] * transaction['price'] for transaction in transactions) + cash_value_left

        return render_template("/sold.html", transactions=transactions, cash_value_left=cash_value_left, total_value=total_value)

    else:
        rows = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
        return render_template("/sell.html", rows=rows)


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    user_id = session["user_id"][0]["id"]
    if request.method == "POST":
        old_password = request.form.get("old_password")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not old_password:
            return apology("Please enter your password", 400)
        elif not request.form.get("password"):
            return apology("Please enter a new password", 400)
        elif not request.form.get("confirmation"):
            return apology("Please enter password again for confirmation", 400)

        rows= db.execute("SELECT * FROM users WHERE id =?", user_id)
        if not check_password_hash(
            rows[0]["hash"], request.form.get("old_password")
        ):
            return apology("Invalid password", 400)


        if confirmation != password:
            return apology("Confirmation password does not match, try again", 400)

        hashed_password = generate_password_hash(password)
        db.execute("UPDATE users SET hash = ? WHERE id =?", hashed_password,user_id)

        return redirect("/")

    else:
        username = db.execute("SELECT username FROM users WHERE id =?", user_id)[0]["username"].upper()
        return render_template("/account.html", username=username)
