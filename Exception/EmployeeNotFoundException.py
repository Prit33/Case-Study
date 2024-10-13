class EmployeeNotFoundException(Exception):
    def __init__(self, message="Employee not found in the database"):
        self.message = message
        super().__init__(self.message)
