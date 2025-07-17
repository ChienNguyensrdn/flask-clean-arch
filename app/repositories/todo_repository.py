class TodoRepository:
    def __init__(self):
        self.todos = {}

    def get_todo(self, todo_id):
        return self.todos.get(todo_id)

    def get_all_todos(self):
        return list(self.todos.values())

    def add_todo(self, todo):
        self.todos[todo['id']] = todo

    def update_todo(self, todo_id, updated_todo):
        if todo_id in self.todos:
            self.todos[todo_id].update(updated_todo)

    def delete_todo(self, todo_id):
        if todo_id in self.todos:
            del self.todos[todo_id]