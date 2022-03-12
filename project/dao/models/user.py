from project.setup_db import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    genre = db.relationship("Genre")
    favorite_genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"))
    # favorite_genre = db.Column(db.Integer)