class Task_History:
    def __init__(self, task_description, date_added, tag, operation, user_id=None, id=None):
        self._id = id
        self._task_description = task_description
        self._date_added = date_added
        self._tag = tag
        self._operation = operation
        self._user_id = user_id

    def get_id(self):
        return self._id
        
    def get_task_description(self):
        return self._task_description
        
    def get_date_added(self):
        return self._date_added
        
    def get_tag(self):
        return self._tag
        
    def get_operation(self):
        return self._operation
        
    def get_user_id(self):
        return self._user_id

    def set_id(self, id):
        self._id = id
        
    def set_task_description(self, task_description):
        self._task_description = task_description
        
    def set_date_added(self, date_added):
        self._date_added = date_added
        
    def set_tag(self, tag):
        self._tag = tag
        
    def set_operation(self, operation):
        self._operation = operation
        
    def set_user_id(self, user_id):
        self._user_id = user_id