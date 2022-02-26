from project.setup_db import db

class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), required=True)
    description = db.Column(db.String(255), required=True)
    trailer = db.Column(db.String(255), required=True)
    year = db.Column(db.Integer, required=True)
    rating = db.Column(db.Float, required=True)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")

