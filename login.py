from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask import session
from db import db


def login_to_account(username: str, password: str):
    sql = text("SELECT username, password_hash FROM users WHERE username=:username")
    user = db.session.execute(sql, {"username":username}).fetchone()
    if user:
        hash_value = user.password_hash
        if check_password_hash(hash_value, password):
            session["username"] = username

        else:
            return "Incorrect password!"
    else:
        return "Incorrect username!"
    