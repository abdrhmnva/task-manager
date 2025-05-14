from dao.BaseDao import Dao
import sys

sys.path.append("/nursezim/classes")
from classes.task import Task

class TaskDAO(Dao):
    def __init__(self, db_path):
        super().__init__(db_path)

    def insert(self, task: Task):
        query = "INSERT INTO tasks (tag, date, time, task, status) VALUES (?, ?, ?, ?, ?)"
        self._cursor.execute(query, (task.get_tag(), task.get_date(), task.get_time(), task.get_task(), task.get_status()))
        self._connection.commit()

    def get_tasks_by_date(self, date):
        query = "SELECT * FROM tasks WHERE date = ?"
        self._cursor.execute(query, (date,))
        rows = self._cursor.fetchall()
        tasks = []
        for row in rows:
            task = Task(row[1], row[2], row[3], row[4], row[5])
            tasks.append(task)
        return tasks

    def delete_task_by_description_and_date(self, task, date):
        query = "DELETE FROM tasks WHERE task = ? AND date = ?"
        self._cursor.execute(query, (task, date))
        self._connection.commit()

    def update_task_by_description_and_date(self, original_description, original_date, tag, date, time, description, status):
        query = """
            UPDATE tasks
            SET tag = ?, date = ?, time = ?, task = ?, status = ?
            WHERE task = ? AND date = ?
        """
        self._cursor.execute(query, (tag, date, time, description, status, original_description, original_date))
        self._connection.commit()

        return True

    def get_tasks_by_date(self, date):
        query = "SELECT * FROM tasks WHERE date = ?"
        self._cursor.execute(query, (date,))
        rows = self._cursor.fetchall()
        tasks = []
        for row in rows:
            task = Task(row[1], row[2], row[3], row[4], row[5])
            tasks.append(task)
        return tasks
