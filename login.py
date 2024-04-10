from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask import session
from db import db
from validate import login_to_account_valid

def login_to_account(username: str, password: str):
    valid = login_to_account_valid(username, password)
    return valid

    

