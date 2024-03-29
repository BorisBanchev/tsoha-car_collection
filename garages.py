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
    
def remove_garage_(garage_id: int):
    sql = text("DELETE from garages where garages.id=:garage_id")
    db.session.execute(sql, {"garage_id":garage_id})
    db.session.commit()

def open_garage(garage_id: int):
    sql1 = text("SELECT garages.name from garages where id=:garage_id")
    sql2 = text("SELECT cars.brand, cars.model, cars.prod_year from cars join garagecars on cars.id = garagecars.car_id join garages on garages.id = garagecars.garage_id where garagecars.garage_id=:garage_id")
    garage_name = db.session.execute(sql1, {"garage_id":garage_id}).fetchone()[0]
    cars = db.session.execute(sql2, {"garage_id":garage_id}).fetchall()
    return (garage_name, cars)


def add_car_(brand: str, model: str, prod_year: int, garage_id: int ):
    sql_to_insert_to_cars = text("INSERT INTO cars (brand, model, prod_year) VALUES (:brand, :model, :prod_year) RETURNING id")
    sql_to_insert_to_garagecars = text("INSERT INTO garagecars (garage_id, car_id) VALUES (:garage_id, :car_id)")
    sql_to_get_user_id = text("SELECT id from users WHERE username=:username")
    user_id = db.session.execute(sql_to_get_user_id, {"username":session["username"]}).fetchone()[0]
    sql_to_insert_to_usercars = text("INSERT INTO usercars (user_id, car_id) VALUES (:user_id, :car_id)")
    sql_for_capacity = text("SELECT garages.capacity FROM garages JOIN usergarages ON garages.id = usergarages.garage_id WHERE usergarages.user_id =:user_id AND garages.id=:garage_id")
    capacity = db.session.execute(sql_for_capacity, {"user_id":user_id, "garage_id":garage_id}).fetchone()[0]
    sql_cars_in_garage = text("SELECT COUNT(*) FROM garagecars WHERE garagecars.garage_id=:garage_id")
    cars_in_garage = db.session.execute(sql_cars_in_garage, {"garage_id":garage_id}).fetchone()[0]
    print(capacity)
    if cars_in_garage < capacity and prod_year >= 1886 and len(brand) > 0 and len(model) > 0:
        car_id = db.session.execute(sql_to_insert_to_cars, {"brand":brand, "model":model, "prod_year":prod_year }).fetchone()[0]
        db.session.commit()
        db.session.execute(sql_to_insert_to_garagecars,{"garage_id":garage_id,"car_id":car_id})
        db.session.commit()
        db.session.execute(sql_to_insert_to_usercars,{"user_id":user_id, "car_id":car_id})
        db.session.commit()
        return "Car added to garage!"
    elif len(brand) == 0:
        return "Car must have a brand!"
    elif len(model) == 0:
        return "Car must have a model!"
    elif cars_in_garage < capacity and 0 <= prod_year < 1886:
        return "Invalid production year, Cars had not been invented yet!"
    elif cars_in_garage < capacity and prod_year < 0:
        return "Production year can't be negative!"
    elif cars_in_garage >= capacity: 
        return "Garage is full!"
    
    