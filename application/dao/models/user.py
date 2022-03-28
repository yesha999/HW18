from application.dao.models.base import BaseModel
from application.database import db

class User(BaseModel):
    __tablename__ = 'user'

    username = db.Column(db.String(255))
    password = db.Column(db.String(100))
    role = db.Column(db.String(10))
