class Task:
    def __init__(self, tag, date, time, task, status):
        self.__tag = tag
        self.__date = date
        self.__time = time
        self.__task = task
        self.__status = status

    def get_tag(self):
        return self.__tag
    def set_tag(self, tag):
        self.__tag = tag

    def get_date(self):
        return self.__date
    def set_date(self, date):
        self.__date = date

    def get_time(self):
        return self.__time
    def set_time(self, time):
        self.__time = time

    def get_task(self):
        return self.__task
    def set_task(self, description):
        self.__task = description

    def get_status(self):
        return self.__status
    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return f"Tag: {self.__tag}, Date: {self.__date}, Task: {self.__task}, Status: {self.__status}"
