from dao.BaseDao import Dao
import sys

sys.path.append("/Users/argenkulzhanov/Desktop/Designer/nursezim/classes")
from classes.user import User

class UserDAO(Dao):
    def __init__(self, db_path):
        super().__init__(db_path)

    def insert(self, user: User):
        query = "INSERT INTO Users (username, password, email) VALUES (?, ?, ?)"
        self._cursor.execute(query, (user.get_username(), user.get_password(), user.get_email()))
        self._connection.commit()

    def find_by_username(self, username: str):
        query = "SELECT * FROM Users WHERE username = ?"
        row = self.fetch_one(query, (username,))
        if row:
            return User(row[1], row[2], row[3])
        else:
            return None

    def find_by_email(self, email: str):
        query = "SELECT * FROM Users WHERE email = ?"
        row = self.fetch_one(query, (email,))
        if row:
            return User(row[1], row[2], row[3])
        else:
            return None