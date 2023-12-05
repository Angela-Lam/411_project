""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database

#### Angela's Homepage code
# @app.route("/",methods=['GET'])
# def homepage():
#     """ returns rendered homepage """
#     users = db_helper.fetch_users()
#     return render_template("index.html", users=users)

### Old Index / homepage
# @app.route("/")
# def homepage():
#     items = database.fetch_homepage()
#     return render_template("index.html", items=items)

@app.route("/home")
def home():
    name = "Guest"
    return render_template("home.html", name=name)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/signup", methods=['GET'])
def signup():
    return render_template("signup.html")

@app.route("/handle_signup", methods=['POST'])
def handle_signup():
    username, password, confirm = request.form['username'], request.form['password'], request.form['password1']
    taken_usernames = database.get_usernames() + ["Guest", "guest"]
    if username in taken_usernames or password != confirm:
        return render_template("signup.html")
    else:
        database.add_user(username, password)
        return render_template("home.html", name=username)

@app.route("/handle_login", methods=['GET', 'POST'])
def handle_login():
    username, password = request.form['username'], request.form['password']
    if (username, password) in database.get_users():
        return render_template("home.html", name=username)
    else:
        return render_template("login.html")

@app.route("/history")
def history():
    """ returns rendered history """
    items = database.fetch_history()
    return render_template("history.html", items=items)

@app.route("/search")
def search():
    """ Returns rendered favorites page """
    favorite_items = database.fetch_fav()  
    return render_template("search.html", items=favorite_items)

@app.route("/favorites")
def favorites():
    """ Returns rendered favorites page """
    favorite_items = database.fetch_fav()  
    return render_template("fav.html", items=favorite_items)


@app.route("/handle_search")
def handle_search():
    video_length = request.form.get('video Length')
    start_date = request.form.get('start-date')
    end_date = request.form.get('end-date')
    category = request.form.get('category')

    if start_date:
        # Process start date (e.g., convert to datetime, validate, etc.)
        pass  # Replace with your logic

    if end_date:
        # Process end date
        pass  # Replace with your logic

    # Continue with processing the search with the dates (if provided)
    # ...

    return render_template('search_results.html') 