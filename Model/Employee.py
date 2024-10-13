class Employee:
    def __init__(self, id=None, name=None, designation=None, gender=None, salary=None, project_id=None):
        self.__id = id
        self.__name = name
        self.__designation = designation
        self.__gender = gender
        self.__salary = salary
        self.__project_id = project_id

    # Getter for id
    def get_id(self):
        return self.__id

    # Setter for id
    def set_id(self, id):
        self.__id = id

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for designation
    def get_designation(self):
        return self.__designation

    # Setter for designation
    def set_designation(self, designation):
        self.__designation = designation

    # Getter for gender
    def get_gender(self):
        return self.__gender

    # Setter for gender
    def set_gender(self, gender):
        self.__gender = gender

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary
    def set_salary(self, salary):
        self.__salary = salary

    # Getter for project_id
    def get_project_id(self):
        return self.__project_id

    # Setter for project_id
    def set_project_id(self, project_id):
        self.__project_id = project_id
