class Project:
    def __init__(self, id=None, project_name=None, description=None, start_date=None, status=None):
        self.__id = id
        self.__project_name = project_name
        self.__description = description
        self.__start_date = start_date
        self.__status = status

    # Getter for id
    def get_id(self):
        return self.__id

    # Setter for id
    def set_id(self, id):
        self.__id = id

    # Getter for project_name
    def get_project_name(self):
        return self.__project_name

    # Setter for project_name
    def set_project_name(self, project_name):
        self.__project_name = project_name

    # Getter for description
    def get_description(self):
        return self.__description

    # Setter for description
    def set_description(self, description):
        self.__description = description

    # Getter for start_date
    def get_start_date(self):
        return self.__start_date

    # Setter for start_date
    def set_start_date(self, start_date):
        self.__start_date = start_date

    # Getter for status
    def get_status(self):
        return self.__status

    # Setter for status
    def set_status(self, status):
        self.__status = status
