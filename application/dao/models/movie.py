from application.dao.models.base import BaseModel
from application.database import db

class Movie(BaseModel):
    __tablename__ = 'movie'

    title = db.Column(db.String(255))
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)

    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")






