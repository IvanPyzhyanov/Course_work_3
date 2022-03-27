from project.setup_db import db

favorite = db.Table('favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(50), nullable=True)
    surname = db.Column(db.String(50), nullable=True)
    favourite_genre = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=True)
    genre = db.relationship('Genre', back_populates='users')
    favorites = db.relationship(
        'Movie',
        secondary=favorite,
        lazy='subquery',
        backref=db.backref('movies', lazy=True),
    )