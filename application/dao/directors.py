from typing import Dict, Any

from application.dao.models.director import Director


class DirectorsDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, uid: int):
        return self.session.query(Director).get(uid)
    
    
    def update(self, uid: int, data: Dict[str, Any]):
        """Изменяем данные 1 режиссера, возвращаем измененного режиссера"""
        self.session.query(Director).filter(Director.id == uid).update(data)
        self.session.commit()
        return self.get_one(uid)

    def create(self, data: Dict[str, Any]):
        """Добавляем новый режиссер, получаем его же"""
        new_director = Director(**data)
        self.session.add(new_director)
        self.session.commit()

        return new_director

    def delete(self, uid: int):
        delete_director = self.get_one(uid)
        self.session.delete(delete_director)
        self.session.commit()
        return ''
    
    
