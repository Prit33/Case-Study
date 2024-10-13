class ProjectNotFoundException(Exception):
    def __init__(self, message="Project not found in the database"):
        self.message = message
        super().__init__(self.message)
