from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
from db import db


def check_user_exists(username):
    sql = text("SELECT id FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    return user


def create_account_valid(username: str, password: str, password2: str):
    user = check_user_exists(username)
    empty_fields = []
    message = ""
    success = False
    if len(username) == 0:
        empty_fields.append("username")

    elif len(password) == 0:
        empty_fields.append("password")
    
    elif len(password2) == 0:
        empty_fields.append("password2")

    
    if not user and 0 < len(username) <= 20 :
        if password == password2 and 0 < len(password) <= 20:
            success = True
            message = "Account was created successfully!"
            return  empty_fields, message, success
        
        elif password == password2 and len(password) > 20:
            message = "Password is too long!"
            return empty_fields, message, success
            
        elif password != password2:
            message = "Passwords don't match!"
            return empty_fields, message, success

        elif len(username) > 20:
            message = "Username is too long!"
            return empty_fields, message, success
        
        else:
            message = "Username already exists!"
            return empty_fields, message, success
    