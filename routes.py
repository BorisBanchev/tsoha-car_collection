
from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask import render_template, redirect, request, session
from os import getenv
from signup import check_user_exists, create_account
from login import login_to_account
from garages import create_garage_
from db import db

app.secret_key = getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods = ["POST", "GET"])
def signup():
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password2 = request.form["password2"]

        message = create_account(username, password, password2)
        
        return render_template("signup.html", message=message)
        

    if request.method == "GET":
        return render_template("signup.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        message2 = login_to_account(username, password)
        
        if message2 != None:
            return render_template("login.html", message2 = message2)
        
        else:
            return redirect("/profile")
        
    if request.method == "GET":
       return  render_template("login.html")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/profile")
def profile():
    try:
        if session["username"]:
            sql1 = text("SELECT id from users WHERE username=:username")
            sql2 = text("SELECT garages.id, garages.name, garages.capacity FROM users JOIN usergarages ON users.id = usergarages.user_id JOIN garages ON usergarages.garage_id = garages.id WHERE users.id=:user_id")
            user_id = db.session.execute(sql1, {"username":session["username"]}).fetchone()[0]
            garages = db.session.execute(sql2, {"user_id":user_id}).fetchall()
            return render_template("profile.html", garages=garages)
    except:
        return render_template("error.html", message = "You have to be logged in to view car collection!")

@app.route("/create_garage", methods = ["POST", "GET"])
def create_garage():
    try:
        if session["username"]:
            if request.method == "POST":
                name = request.form["garage_name"]
                capacity = int(request.form["capacity"])
                message = create_garage_(name, capacity)
                return render_template("create_garage.html", message=message)
            
            elif request.method == "GET":
                return render_template("create_garage.html")
    
    except:
        return render_template("error.html", message = "You have to be logged in to create a garage!")

@app.route("/add_car")
def add_car_to_garage():
    pass 

@app.route("/remove_car")
def remove_car_from_garage():
    pass 

