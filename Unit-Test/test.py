import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest.mock import Mock, patch, call
from DAO.ProjectRepositoryImpl import ProjectRepositoryImpl
from Model.Employee import Employee
from Model.Task import Task
from Exception.EmployeeNotFoundException import EmployeeNotFoundException
from Exception.ProjectNotFoundException import ProjectNotFoundException


class TestProjectRepositoryImpl(unittest.TestCase):

    @patch('DAO.ProjectRepositoryImpl.PropertyUtil.getPropertyString')
    @patch('DAO.ProjectRepositoryImpl.pyodbc.connect')
    def setUp(self, mock_connect, mock_get_property_string):            # arranging all properties
        mock_get_property_string.return_value = "mock_connection_string"
        self.mock_connection = Mock()
        mock_connect.return_value = self.mock_connection
        self.repo = ProjectRepositoryImpl()

    def test_create_employee_success(self):
       
        emp = Employee(name="John", designation="SDE-1", gender="Male", salary=50000, project_id=1, role="employee")
        mock_cursor = Mock()
        self.repo.conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = (1)  # Simulate that the project exists
        
        result = self.repo.createEmployee(emp)
        
        self.assertTrue(result)
        expected_calls = [
            call('SELECT id FROM Project WHERE id = ?', (1)),
            call('INSERT INTO Employee (name, designation, gender, salary, project_id, role) VALUES (?, ?, ?, ?, ?, ?)', 
                 ('John', 'SDE-1', 'Male', 50000, 1, "employee"))
        ]
        mock_cursor.execute.assert_has_calls(expected_calls, any_order=False)
        self.assertEqual(mock_cursor.execute.call_count, 2) # verifies execute was called exactly twice.
        self.repo.conn.commit.assert_called_once()
        

    def test_get_all_tasks_for_employee_in_project(self):   # needs employee id and project id
        emp_id = 1
        project_id = 1
        mock_tasks = [                      #sample task
            (1, "Task 1", 1, 1, "assigned"),
            (2, "Task 2", 1, 1, "started")
        ]
        self.repo.conn.cursor().fetchall.return_value = mock_tasks  # when fetchall() calls, mock_tasks should be returned 
        
        tasks = self.repo.getAllTasks(emp_id, project_id)
        
        self.assertEqual(len(tasks), 2)
        self.repo.conn.cursor().execute.assert_called_once()
        self.repo.conn.cursor().fetchall.assert_called_once()

    def test_employee_not_found_exception(self):
        self.repo.conn.cursor().rowcount = 0        # condition for getting  EmployeeNotFound 
        
        with self.assertRaises(EmployeeNotFoundException):  #starts a context manager that asserts the code inside it should raise an EmployeeNotFoundException
            self.repo.deleteEmployee(999)
        
    def test_project_not_found_exception(self):
        self.repo.conn.cursor().rowcount = 0       # condition for getting  ProjectNotFoundException 
        
        with self.assertRaises(ProjectNotFoundException):
            self.repo.deleteProject(999)

if __name__ == '__main__':
    unittest.main()