from dao.BaseDao import Dao
import sys

sys.path.append("/Users/argenkulzhanov/Desktop/Designer/nursezim/classes")
from classes.task_history import Task_History

class TaskHistoryDAO(Dao):
    def __init__(self, db_path):
        super().__init__(db_path)

    def insert(self, task_history: Task_History):
        query = "INSERT INTO TaskHistory (task_name, task_description, task_status) VALUES (?, ?, ?)"
        self._cursor.execute(query, (task_history.get_name(), task_history.get_description(), task_history.get_status()))
        self._connection.commit()
