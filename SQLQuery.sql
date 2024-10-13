create database Project_Management_System;

use Project_Management_System;


CREATE TABLE Employee (
    id INT PRIMARY KEY IDENTITY,
    name VARCHAR(100),
    designation VARCHAR(100),
    gender VARCHAR(10),
    salary DECIMAL(10, 2),
    project_id INT FOREIGN KEY REFERENCES Project(id)
);

CREATE TABLE Project (
    id INT PRIMARY KEY IDENTITY,
    project_name VARCHAR(100),
    description TEXT,
    start_date DATE,
    status VARCHAR(50)
);

CREATE TABLE Task (
    task_id INT PRIMARY KEY IDENTITY,
    task_name VARCHAR(100),
    project_id INT FOREIGN KEY REFERENCES Project(id),
    employee_id INT FOREIGN KEY REFERENCES Employee(id),
    status VARCHAR(50)
);


select * from Employee;
select * from Project;
select * from Task;

delete Employee ;
delete task ;
delete Project;

/*drop table Task;
drop table Project;
drop table Employee;*/



INSERT INTO dbo.Employee (name, designation, gender, salary, project_id) VALUES ('Amy', 'SDE-2', 'F', 1300000, 1);

INSERT INTO Project (project_name, description, start_date, status) VALUES ('Facebook', 'Facebook 2.0', '2020-10-10', 'dev');


SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Project';
SELECT TABLE_SCHEMA, TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME = 'Project';

