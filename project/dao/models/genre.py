from project.dao.models.base import BaseMixin
from project.setup_db import db


class Genre(BaseMixin, db.Model):
    __tablename__ = "genres"

    name = db.Column(db.String(100), unique=True, nullable=False)
    users = db.relationship('User', back_populates='genre')

    def __repr__(self):
        return f"<Genre '{self.name.title()}'>"
