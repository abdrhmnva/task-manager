class Task_History:
    def __init__(self, task_id, action):
        self.__task_id = task_id
        self.__action = action

    def get_task_id(self):
        return self.__task_id
    def set_task_id(self, task_id):
        self.__task_id = task_id

    def get_action(self):
        return self.__action
    def set_action(self, action):
        self.__action = action

    def __str__(self):
        return f"Task ID: {self.__task_id}, Action: {self.__action}"
