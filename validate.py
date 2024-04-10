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

    if len(empty_fields) != 0:
        data = empty_fields, message, success
        return data
    

    if user:
        message = "Username already exists!"
        data = empty_fields, message, success
        return  data


    if not user and 0 < len(username) <= 20 :
        if password == password2 and 0 < len(password) <= 20:
            success = True
            message = "Account was created successfully!"
            data = empty_fields, message, success
            return  data
        
        elif password == password2 and len(password) > 20:
            message = "Password is too long!"
            data = empty_fields, message, success
            return  data
            
        elif password != password2:
            message = "Passwords don't match!"
            data = empty_fields, message, success
            return  data

        elif len(username) > 20:
            message = "Username is too long!"
            data = empty_fields, message, success
            return  data
    

def login_to_account_valid(username: str, password: str):
    sql = text("SELECT username, password_hash FROM users WHERE username=:username")
    user = db.session.execute(sql, {"username":username}).fetchone()
    empty_fields = []
    message = ""
    success = False
    if len(username) == 0:
        empty_fields.append("username")

    elif len(password) == 0:
        empty_fields.append("password")

    if len(empty_fields) != 0:
        data = empty_fields, message, success
        return data

    
    if not user:
        message = "Invalid username or password!"
        data = empty_fields, message, success
        return data
    
    if user:
        hash_value = user.password_hash
        if check_password_hash(hash_value, password) and user.username == username:
            success = True
            data = empty_fields, message, success
            return data
        else:
            message = "invalid username or password!"
            data = empty_fields, message, success
            return data
        
        
    

