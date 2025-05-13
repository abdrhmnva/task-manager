import re
from classes.user import User  # твой класс User
from dao.user_dao import UserDAO

class Model:
    def __init__(self):
        self.dao = UserDAO("/Users/argenkulzhanov/Desktop/Designer/madina/task_manager.sqlite")

    def is_strong_password(self, password):
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char in "!@#$%^&*()-_=+[]{};:,.<>?/" for char in password):
            return False
        return True

    def is_valid_email(self, email):
        return re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", email)

    def is_valid_username(self, username):
        return re.match(r"^[A-Za-z0-9_]+$", username)

    def create_account(self, username, password, email):
        # Проверки
        if not username or not email or not password:
            return False, "Please fill in all fields."

        if not self.is_valid_username(username):
            return False, "Username must contain only English letters and digits."

        if not self.is_valid_email(email):
            return False, "Please enter a valid email address."

        if not self.is_strong_password(password):
            return False, "Password must be at least 8 characters and include uppercase, lowercase, number, and symbol."

        if self.dao.find_by_username(username):
            return False, "This username already exists."

        if self.dao.find_by_email(email):
            return False, "This email already exists."

        # Создание пользователя
        user = User(username, password, email)
        self.dao.insert(user)
        return True, "Your account has been created successfully."

    def validate_login(self, username, password):
        if not username or not password:
            return False, "Please fill in both fields."

        user = self.dao.find_by_username(username)
        if not user:
            return False, "User not found."

        if user.get_password() != password:
            return False, "Incorrect password."

        return True, "Login successful."