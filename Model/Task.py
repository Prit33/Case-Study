class Task:
    def __init__(self, task_id=None, task_name=None, project_id=None, employee_id=None, status=None):
        self.__task_id = task_id
        self.__task_name = task_name
        self.__project_id = project_id
        self.__employee_id = employee_id
        self.__status = status

    # Getter for task_id
    def get_task_id(self):
        return self.__task_id

    # Setter for task_id
    def set_task_id(self, task_id):
        self.__task_id = task_id

    # Getter for task_name
    def get_task_name(self):
        return self.__task_name

    # Setter for task_name
    def set_task_name(self, task_name):
        self.__task_name = task_name

    # Getter for project_id
    def get_project_id(self):
        return self.__project_id

    # Setter for project_id
    def set_project_id(self, project_id):
        self.__project_id = project_id

    # Getter for employee_id
    def get_employee_id(self):
        return self.__employee_id

    # Setter for employee_id
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter for status
    def get_status(self):
        return self.__status

    # Setter for status
    def set_status(self, status):
        self.__status = status
