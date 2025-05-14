from classes.task_history import Task_History
import sqlite3
from datetime import datetime

class TaskHistoryDAO:
    def __init__(self, db_path):
        self.db_path = db_path
        
    def insert(self, task_history):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        date_added = task_history.get_date_added() or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute(
            """
            INSERT INTO task_history (task_description, date_added, tag, operation, user_id)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                task_history.get_task_description(),
                date_added,
                task_history.get_tag(),
                task_history.get_operation(),
                task_history.get_user_id()
            )
        )
        
        last_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        task_history.set_id(last_id)
        return task_history
        
    def get_all_history(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            """
            SELECT id, task_description, date_added, tag, operation, user_id
            FROM task_history
            ORDER BY date_added DESC
            """
        )
        
        rows = cursor.fetchall()
        history_list = []
        
        for row in rows:
            history = Task_History(
                task_description=row[1],
                date_added=row[2],
                tag=row[3],
                operation=row[4],
                user_id=row[5],
                id=row[0]
            )
            history_list.append(history)
            
        conn.close()
        return history_list
        
    def get_history_by_user_id(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            """
            SELECT id, task_description, date_added, tag, operation, user_id
            FROM task_history
            WHERE user_id = ?
            ORDER BY date_added DESC
            """,
            (user_id,)
        )
        
        rows = cursor.fetchall()
        history_list = []
        
        for row in rows:
            history = Task_History(
                task_description=row[1],
                date_added=row[2],
                tag=row[3],
                operation=row[4],
                user_id=row[5],
                id=row[0]
            )
            history_list.append(history)
            
        conn.close()
        return history_list