from models.todo_model import TodoList
from models.todo_db import TodoDB

class TodoService:
    def __init__(self):
        self.todo_list = TodoList()
        self.todo_db = TodoDB()

    def get_tasks(self):
        return self.todo_list.get_tasks()

    def add_task(self, task):
        self.todo_list.add_task(task)
        self.todo_db.add(task)

    def delete_task(self, index):
        self.todo_list.delete_task(index)

    def complete_task(self, index):
        self.todo_list.complete_task(index)
        # self.todo_db.completed(self.todo_list.get_tasks()[index])