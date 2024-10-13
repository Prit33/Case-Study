
from DAO.IProjectRepository import IProjectRepository
from Exception.ProjectNotFoundException import ProjectNotFoundException
from Exception.EmployeeNotFoundException import EmployeeNotFoundException
import pyodbc
from Util.PropertyUtil import PropertyUtil

class ProjectRepositoryImpl(IProjectRepository):

    def __init__(self):
        self.conn = self.getConnection()

    def getConnection(self):
        connection_string = PropertyUtil.getPropertyString()
        return pyodbc.connect(connection_string)

    def createEmployee(self, emp):
        try:
            cursor = self.conn.cursor()

            cursor.execute("SELECT id FROM Project WHERE id = ?", (emp.get_project_id(),))
            project = cursor.fetchone()

            if project is None: # raising exception if project id in not found
                raise ProjectNotFoundException(f"Project with ID {emp.get_project_id()} not found, please check project id again")
            
            cursor.execute("INSERT INTO Employee (name, designation, gender, salary, project_id) VALUES (?, ?, ?, ?, ?)", (emp.get_name(), emp.get_designation(), emp.get_gender(), emp.get_salary(), emp.get_project_id()))
            self.conn.commit()
            return True
        except ProjectNotFoundException as e:
            print(f"\nError: {e}")  
            return False
        except Exception as e:
            print(f"Error creating employee: {e}")
            return False

    def createProject(self, pj):
        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO Project (project_name, description, start_date, status) VALUES (?, ?, ?, ?)"            
            cursor.execute(query, (pj.get_project_name(), pj.get_description(), pj.get_start_date(), pj.get_status()))
            self.conn.commit()            
            return True

        except Exception as e:
            print(f"\nError creating project: {e}")
            return False
        finally:
            cursor.close()

    def createTask(self, task):
        try:
            cursor = self.conn.cursor()
            
            check_employee_query = "SELECT id FROM Employee WHERE id = ?"
            cursor.execute(check_employee_query, (task.get_employee_id(),))
            employee = cursor.fetchone()

            # If employee does not exist, raise UserNotFound exception
            if not employee:
                raise EmployeeNotFoundException(f"Employee with ID {task.get_employee_id()} does not exist")
            
            check_project_query = "SELECT id FROM Project WHERE id = ?"
            cursor.execute(check_project_query, (task.get_project_id()))
            project = cursor.fetchone()

            if not project:
                raise ProjectNotFoundException(f"Project with ID {task.get_project_id()} does not exist")
            
            query = "INSERT INTO Task (task_name, project_id, employee_id, status) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (task.get_task_name(), task.get_project_id(), task.get_employee_id(), task.get_status()))
            self.conn.commit()
            return True
        except EmployeeNotFoundException as e:
            print(f"\nError: {e}")  
            return False
        except ProjectNotFoundException as e:
            print(f"\nError: {e}")  
            return False
        except Exception as e:
            print(f"\nError creating task: {e}")
            return False
        finally:
            cursor.close()
        
    def assignProjectToEmployee(self, projectId, employeeId):
        try:
            cursor = self.conn.cursor()
            query = "UPDATE Employee SET project_id = ? WHERE id = ?"
            cursor.execute(query, (projectId, employeeId))
            
            if cursor.rowcount == 0:
                raise EmployeeNotFoundException(f"Employee with ID {employeeId} not found.")
            
            self.conn.commit()
            return True
        except EmployeeNotFoundException as e:
            print(f"\nError: {e}")  
            return False
        except Exception as e:
            print(f"\nError in assigning project to employee: {e}")
            return False
        finally:
            cursor.close()

    def assignTaskInProjectToEmployee(self, taskId, projectId, employeeId):
        try:
            cursor = self.conn.cursor()
            query = "UPDATE Task SET employee_id = ? WHERE task_id = ? AND project_id = ?"
            cursor.execute(query, (employeeId, taskId, projectId))
            
            if cursor.rowcount == 0:
                raise ProjectNotFoundException(f"Task with ID {taskId} in Project {projectId} not found.")
            
            self.conn.commit()
            return True
        except ProjectNotFoundException as e:
            print(f"\nError: {e}")  
            return False
        except Exception as e:
            print(f"\nError in assigning task within a project to employee: {e}")
            return False
        finally:
            cursor.close()

    def deleteEmployee(self, userId):
        try:
            cursor = self.conn.cursor()
            query = "DELETE FROM Employee WHERE id = ?"
            cursor.execute(query, (userId,))
            
            if cursor.rowcount == 0:
                raise EmployeeNotFoundException(f"Employee with ID {userId} not found.")
            
            self.conn.commit()
            return True
        except EmployeeNotFoundException as e:
            # raise # uncomment it in unit-testing
            print(f"\nError: {e}") 
            return False
        except Exception as e:
            print(f"\nError in deleting employee:\n {e}")
            return False
        finally:
            cursor.close()
         
    def deleteProject(self, projectId):
        try:
            cursor = self.conn.cursor()
            query = "DELETE FROM Project WHERE id = ?"
            cursor.execute(query, (projectId,))
            
            if cursor.rowcount == 0:
                raise ProjectNotFoundException(f"Project with ID {projectId} not found.")
            
            self.conn.commit()
            return True
        except ProjectNotFoundException as e:
            raise # uncomment it in unit-testing
            print(f"\nError: {e}")  
            return False
        except Exception as e:
            print(f"\nError in deleting employee: {e}")
            return False
        finally:
            cursor.close()

    def deleteTask(self, task_id):
        try:
            cursor = self.conn.cursor()
            query = "DELETE FROM Task WHERE task_id = ?"
            cursor.execute(query, (task_id))
            if cursor.rowcount == 0:
                return False, f"Task with ID {task_id} not found"
            self.conn.commit()
            return True, ""
        except Exception as e:
            print(f"\nError deleting task: {e}")
            return False, ""
        

    def getAllTasks(self, empId, projectId):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM Task WHERE employee_id = ? AND project_id = ?"
            cursor.execute(query, (empId, projectId))
            
            tasks = cursor.fetchall()
            if not tasks:
                raise EmployeeNotFoundException(f"No tasks found for employee ID {empId} in project {projectId}.")
            return tasks
        except EmployeeNotFoundException as e:
            print(f"\nError: {e}")  
            return False
        except Exception as e:
            print(f"\nError in fetching all tasks: {e}")
            return False
        finally:
            cursor.close()
