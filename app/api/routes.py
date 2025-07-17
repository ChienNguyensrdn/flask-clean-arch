from flask.views import MethodView
from flask_smorest import Blueprint
from app.schemas.todo_schema import TodoSchema
from app.repositories.todo_repository import TodoRepository

blp = Blueprint('todos', 'todos', url_prefix='/todos', description='Todo operations')
repo = TodoRepository()

@blp.route('/')
class TodoList(MethodView):
    @blp.response(200, TodoSchema(many=True))
    def get(self):
        """List all todos"""
        return repo.get_all_todos()

    @blp.arguments(TodoSchema)
    @blp.response(201, TodoSchema)
    def post(self, new_todo):
        """Create a new todo"""
        repo.add_todo(new_todo)
        return new_todo

@blp.route('/<int:todo_id>')
class TodoResource(MethodView):
    @blp.response(200, TodoSchema)
    def get(self, todo_id):
        """Get a todo by ID"""
        todo = repo.get_todo(todo_id)
        if not todo:
            blp.abort(404, message="Todo not found")
        return todo

    @blp.arguments(TodoSchema)
    @blp.response(200, TodoSchema)
    def put(self, updated_todo, todo_id):
        """Update a todo"""
        repo.update_todo(todo_id, updated_todo)
        return repo.get_todo(todo_id)

    def delete(self, todo_id):
        """Delete a todo"""
        repo.delete_todo(todo_id)
        return '', 204