class Task:
    def __init__(self, tag, date, description, status):
        self.__tag = tag
        self.__date = date
        self.__description = description
        self.__status = status

    def get_tag(self):
        return self.__tag
    def set_tag(self, tag):
        self.__tag = tag

    def get_date(self):
        return self.__date
    def set_date(self, date):
        self.__date = date

    def get_description(self):
        return self.__description
    def set_description(self, description):
        self.__description = description

    def get_status(self):
        return self.__status
    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return f"Tag: {self.__tag}, Date: {self.__date}, Description: {self.__description}, Status: {self.__status}"
