import unittest
from unittest.mock import MagicMock
from model import Model
from classes.user import User

class TestModel(unittest.TestCase):
    def setUp(self):
        # Create a mock UserDAO
        self.mock_dao = MagicMock()
        self.model = Model()
        self.model.dao = self.mock_dao

    def test_is_strong_password(self):
        self.assertTrue(self.model.is_strong_password("Strong1!"))
        self.assertFalse(self.model.is_strong_password("weak"))
        self.assertFalse(self.model.is_strong_password("NoNumber!"))
        self.assertFalse(self.model.is_strong_password("nonumber1"))
        self.assertFalse(self.model.is_strong_password("NONUMBER1!"))

    def test_is_valid_email(self):
        self.assertTrue(self.model.is_valid_email("test@example.com"))
        self.assertFalse(self.model.is_valid_email("invalid-email"))
        self.assertFalse(self.model.is_valid_email("test@.com"))
        self.assertFalse(self.model.is_valid_email("test@com"))

    def test_is_valid_username(self):
        self.assertTrue(self.model.is_valid_username("valid_username123"))
        self.assertFalse(self.model.is_valid_username("invalid username!"))
        self.assertFalse(self.model.is_valid_username("invalid-username"))

    def test_create_account_success(self):
        self.mock_dao.find_by_username.return_value = None
        self.mock_dao.find_by_email.return_value = None

        result, message = self.model.create_account("validuser", "Strong1!", "test@example.com")
        self.assertTrue(result)
        self.assertEqual(message, "Your account has been created successfully.")
        self.mock_dao.insert.assert_called_once()

    def test_create_account_existing_username(self):
        self.mock_dao.find_by_username.return_value = User("validuser", "Strong1!", "test@example.com")
        self.mock_dao.find_by_email.return_value = None

        result, message = self.model.create_account("validuser", "Strong1!", "test@example.com")
        self.assertFalse(result)
        self.assertEqual(message, "This username already exists.")

    def test_create_account_existing_email(self):
        self.mock_dao.find_by_username.return_value = None
        self.mock_dao.find_by_email.return_value = User("validuser", "Strong1!", "test@example.com")

        result, message = self.model.create_account("newuser", "Strong1!", "test@example.com")
        self.assertFalse(result)
        self.assertEqual(message, "This email already exists.")

    def test_validate_login_success(self):
        mock_user = User("validuser", "Strong1!", "test@example.com")
        self.mock_dao.find_by_username.return_value = mock_user

        result, message = self.model.validate_login("validuser", "Strong1!")
        self.assertTrue(result)
        self.assertEqual(message, "Login successful.")

    def test_validate_login_user_not_found(self):
        self.mock_dao.find_by_username.return_value = None

        result, message = self.model.validate_login("invaliduser", "Strong1!")
        self.assertFalse(result)
        self.assertEqual(message, "User not found.")

    def test_validate_login_incorrect_password(self):
        mock_user = User("validuser", "Strong1!", "test@example.com")
        self.mock_dao.find_by_username.return_value = mock_user

        result, message = self.model.validate_login("validuser", "WrongPassword!")
        self.assertFalse(result)
        self.assertEqual(message, "Incorrect password.")

if __name__ == "__main__":
    unittest.main()