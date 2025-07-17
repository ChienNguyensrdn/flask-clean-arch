from app.repositories.todo_repository import TodoRepository

class TodoService:
    def __init__(self):
        self.repository = TodoRepository()

    def get_all_todos(self):
        return self.repository.get_all()

    def get_todo_by_id(self, todo_id):
        return self.repository.get_by_id(todo_id)

    def create_todo(self, todo_data):
        return self.repository.create(todo_data)

    def update_todo(self, todo_id, todo_data):
        return self.repository.update(todo_id, todo_data)

    def delete_todo(self, todo_id):
        return self.repository.delete(todo_id)