from flask_login import UserMixin
from .app import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

# class Article(db.Model):
#     __tablename__ = "articles"
#
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255))
#     text = db.Column(db.Text())
#     author = None
