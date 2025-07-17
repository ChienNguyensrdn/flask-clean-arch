from sqlalchemy import Column, Integer, String
from app import db

class Todo(db.Model):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    task = Column(String(200), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id}: {self.task}>'

    def to_dict(self):
        return {
            'id': self.id,
            'task': self.task
        }