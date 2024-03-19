from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
from db import db

def check_user_exists(username):
    sql = text("SELECT id FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    return user


def create_account(username: str, password: str, password2: str):
    user = check_user_exists(username)
    sql = text("INSERT INTO users (username, password_hash) VALUES (:username, :password)")
    if not user and 0 < len(username) <= 20 :
        if password == password2 and 0 < len(password) <= 20:
            db.session.execute(sql, {"username":username, "password":generate_password_hash(password) })
            db.session.commit()
            return "Account was created successfully!"
        
        elif password == password2 and len(password) > 20:
            return "Password is too long!"
        
        elif password == password2 and len(password) == 0:
            return "Password can't be empty!"

        else:
            return "Passwords don't match!"

    elif not user and len(username) > 20:
        return "Username is too long!"
    
    elif not user and len(username) == 0:
        return "Username can't be empty!"
    
    else:
        return "Username already exists!"





