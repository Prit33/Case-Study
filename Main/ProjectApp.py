import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from DAO.ProjectRepositoryImpl import ProjectRepositoryImpl
from Model.Employee import Employee
from Model.Project import Project
from Model.Task import Task
from Exception.EmployeeNotFoundException import EmployeeNotFoundException
from Exception.ProjectNotFoundException import ProjectNotFoundException



def main():
    project_repo = ProjectRepositoryImpl()

    while True:
        print("\n===== Project Management Menu =====")
        print("1. Create Project")
        print("2. Add Employee")
        print("3. Add Task")
        print("4. Assign project to employee")
        print("5. Assign task within a project to employee")
        print("6. Delete Task")
        print("7. Delete Employee")
        print("8. List all tasks assigned to an employee in a project")
        print("9. Exit")

        choice = int(input("\nChoose an option: "))

        if choice == 1:
           # Add Project
            project_name = input("Enter project name: ")
            description = input("Enter project description: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            status = input("Enter project status (started/dev/build/test/deployed): ")
            pj = Project(project_name=project_name, description=description, start_date=start_date, status=status)

            if project_repo.createProject(pj):
                print(f"\nProject {project_name} added successfully.")
            else:
                print("\nProject creation failed !!")

        elif choice == 2:
             # Add Employee
            name = input("Enter employee name: ")
            designation = input("Enter designation: ")
            gender = input("Enter gender: ")
            salary = float(input("Enter salary: "))
            project_id = int(input("Enter project ID: "))
            emp = Employee(name=name, designation=designation, gender=gender, salary=salary, project_id=project_id)
            
            if project_repo.createEmployee(emp):
                print(f"\n Employee {name} added successfully.")
            else:
                print("\nEmployee creation failed !!")

        elif choice == 3:
            # Add Task
            task_name = input("Enter task name: ")
            project_id = int(input("Enter project ID: "))
            employee_id = int(input("Enter employee ID: "))
            status = input("Enter task status (assigned/started/completed): ")
            task = Task(task_name=task_name, project_id=project_id, employee_id=employee_id, status=status)

            if project_repo.createTask(task):
                print(f"\nTask {task_name} added successfully.")
            else:
                print("Task creation failed !!")

        elif choice == 4:
            # Assign project to employee
            project_id = int(input("Enter project ID: "))
            employee_id = int(input("Enter employee ID: "))

            if project_repo.assignProjectToEmployee(project_id, employee_id):
                print(f"\nProject {project_id} assigned to employee {employee_id} successfully.")
            else:
                print("\n Assignment project to employee failed !!")

        elif choice == 5:
            # Assign task in project to employee
            task_id = int(input("Enter task ID: "))
            project_id = int(input("Enter project ID: "))
            employee_id = int(input("Enter employee ID: "))

            if project_repo.assignTaskInProjectToEmployee(task_id, project_id, employee_id):
                print(f"\nTask {task_id} in project {project_id} assigned to employee {employee_id} successfully.")
            else:
                print("\n  Assignment task within a project to employee failed !!\n")

        elif choice == 6:
            # Delete Task
            task_id = int(input("Enter task ID to delete: "))
            (success, message)=project_repo.deleteTask(task_id)
            # print( success, message)

            if success:
                print(f"\nTask of id:{task_id} deleted successfully")
            else:
                print(f"\nDeletion of Task failed due to: {message} ")

        elif choice == 7:            
            # Delete Employee
            employee_id = int(input("Enter employee ID to delete: "))

            if project_repo.deleteEmployee(employee_id):
                print(f"\nEmployee of id:{employee_id} deleted successfully.")
            else:
                print("\n Deletion of Employee failed , try deleting task which is assigned to employee first!!\n")

        elif choice == 8:
            # List all tasks assigned to an employee in a project
            emp_id = int(input("Enter employee ID: "))
            project_id = int(input("Enter project ID: "))

            tasks = project_repo.getAllTasks(emp_id, project_id)
            if tasks:
                print("\n===== Tasks Assigned to Employee =====")
                for task in tasks:
                    print(f"\nTask ID: {task.task_id}, Task Name: {task.task_name}, Status: {task.status}")
            else:
                print("\nError in retrieving tasks")

        elif choice == 9:
            print("\nExiting application.")
            break

        else:
            print("\nInvalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
