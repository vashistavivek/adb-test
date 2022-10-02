
from datetime import datetime
import logging

from django.conf import settings

logger = logging.getLogger(__name__)
connection = settings.MONGO_DATABASE

class TodoHandler:

    def __init__(self) -> None:
        self.connection_obj = connection['todo']

    def get_all_todo(self):
        try:
            all_todos = self.connection_obj.find()
            all_todos = [todo['todo'] for todo in all_todos]
            return all_todos
        except Exception as e:
            logger.error(e, exc_info=True)
        return []

    def add_todo(self, todo):
        flag = False
        try:
            todo_dict = {"todo": todo, 'created_at': datetime.now()}
            self.connection_obj.insert_one(todo_dict)
            flag = True
        except Exception as e:
            logger.error(e, exc_info=True)
        return flag