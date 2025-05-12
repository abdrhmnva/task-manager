class User:
    def __init__(self, username, password, email):
        self.__username = username
        self.__password = password
        self.__email = email

    def get_username(self):
        return self.__username
    def set_username(self, username):
        self.__username = username

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

    def get_password(self):
        return self.__password
    def set_password(self, password):
        self.__password = password