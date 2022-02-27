from project.dao.models.base import BaseMixin
from project.setup_db import db

class FavoriteMovie(BaseMixin, db.Model):
    __tablename__ = "favorite_movies"
    user = db.relationship("User")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    movie = db.relationship("Movie")
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))

