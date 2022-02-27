from project.setup_db import db

class FavoriteMovie(db.Model):
    __tablename__ = "favorite_movies"
    user = db.relationship("User")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    movie = db.relationship("Movie")
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))

