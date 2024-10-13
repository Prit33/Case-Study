from abc import ABC, abstractmethod

class IProjectRepository(ABC):
    
    @abstractmethod
    def createEmployee(self, emp):
        pass

    @abstractmethod
    def createProject(self, pj):
        pass

    @abstractmethod
    def createTask(self, task):
        pass

    @abstractmethod
    def assignProjectToEmployee(self, projectId, employeeId):
        pass

    @abstractmethod
    def assignTaskInProjectToEmployee(self, taskId, projectId, employeeId):
        pass

    @abstractmethod
    def deleteEmployee(self, userId):
        pass

    @abstractmethod
    def deleteProject(self, projectId):
        pass

    @abstractmethod
    def getAllTasks(self, empId, projectId):
        pass
