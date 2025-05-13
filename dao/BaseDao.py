import sqlite3

class Dao:
    def __init__(self, db_path):
        self._connection = sqlite3.connect(db_path)
        self._cursor = self._connection.cursor()

    def execute_query(self, query, params=None):
        self._cursor.execute(query, params or [])
        self._connection.commit()
        return self._cursor

    def fetch_all(self, query, params=None):
        self._cursor.execute(query, params or [])
        return self._cursor.fetchall()

    def fetch_one(self, query, params=None):
        self._cursor.execute(query, params or [])
        return self._cursor.fetchone()