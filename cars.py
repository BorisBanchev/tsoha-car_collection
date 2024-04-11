from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask import session
from db import db
import datetime
from user import get_user_id
from validate import add_car_valid

def remove_car_(car_id: int):
    sql = text("DELETE from cars where cars.id=:car_id")
    db.session.execute(sql, {"car_id":car_id})
    db.session.commit()

def add_car_(brand: str, model: str, prod_year: int, garage_id ):
    sql_to_insert_to_cars = text("INSERT INTO cars (brand, model, prod_year) VALUES (:brand, :model, :prod_year) RETURNING id")
    sql_to_insert_to_garagecars = text("INSERT INTO garagecars (garage_id, car_id) VALUES (:garage_id, :car_id)")
    user_id = get_user_id()
    car_id = db.session.execute(sql_to_insert_to_cars, {"brand":brand, "model":model, "prod_year":prod_year }).fetchone()[0]
    sql_to_insert_to_usercars = text("INSERT INTO usercars (user_id, car_id) VALUES (:user_id, :car_id)")
    data = add_car_valid(brand, model, prod_year, garage_id)
    if data[2]:
        db.session.commit()
        db.session.execute(sql_to_insert_to_garagecars,{"garage_id":garage_id,"car_id":car_id})
        db.session.commit()
        db.session.execute(sql_to_insert_to_usercars,{"user_id":user_id, "car_id":car_id})
        db.session.commit()
        return data
    return data
       
   
