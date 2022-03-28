from typing import Dict, Any

from application.dao.models.genre import Genre


class GenresDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, uid: int):
        return self.session.query(Genre).get(uid)
    
    
    
    def update(self, uid: int, data: Dict[str, Any]):
        """Изменяем данные 1 жанра, возвращаем измененный жанр"""
        self.session.query(Genre).filter(Genre.id == uid).update(data)
        self.session.commit()
        return self.get_one(uid)

    def create(self, data: Dict[str, Any]):
        """Добавляем новый жанр, получаем его же"""
        new_genre = Genre(**data)
        self.session.add(new_genre)
        self.session.commit()

        return new_genre

    def delete(self, uid: int):
        delete_genre = self.get_one(uid)
        self.session.delete(delete_genre)
        self.session.commit()
        return ''