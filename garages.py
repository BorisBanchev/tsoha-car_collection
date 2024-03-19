from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask import session
from db import db

def create_garage_(name: str, capacity: int):
    sql1 = text("INSERT INTO garages (name, capacity) VALUES (:name, :capacity) RETURNING id")
    sql2 = text("SELECT id from users WHERE username=:username")
    sql3 = text("INSERT INTO usergarages (user_id, garage_id) VALUES (:user_id, :garage_id)")

    if capacity > 0 and len(name) != 0:
        garage_id = db.session.execute(sql1, {"name":name, "capacity":capacity}).fetchone()[0]
        db.session.commit()
        user_id = db.session.execute(sql2, {"username":session["username"]}).fetchone()[0]
        db.session.commit()
        db.session.execute(sql3, {"user_id":user_id, "garage_id":garage_id})
        db.session.commit()
        return "Garage created successfully!"
    
    elif capacity <= 0:
        return "Capacity can't be negative or zero!"
    
    elif len(name) == 0:
        return "Garage must have a name!"
    
def user_garages():
    pass

def add_car_to_garage():
    pass