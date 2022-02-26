from project.setup_db import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, required=True)
    email = db.Column(db.String(255), unique=True, required=True)
    password = db.Column(db.String(255), required=True)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    favorite_genre = db.Column(db.String(255))