CREATE TABLE Employees(
    Employee_ID TEXT,
    First_Name TEXT,
    Last_Name TEXT,
    Department TEXT,
    Salary REAL
);

INSERT INTO Employees (Employee_ID, First_Name, Last_Name, Department, Salary) VALUES
('1', 'John', 'Doe', 'Sales', 55000.00),
('2', 'Jane', 'Smith', 'Marketing', 60000.00),
('3', 'Emily', 'Johnson', 'IT', 75000.00),
('4', 'Michael', 'Brown', 'HR', 50000.00),
('5', 'Jessica', 'Davis', 'Finance', 70000.00),
('6', 'Daniel', 'Wilson', 'IT', 80000.00);

SELECT COUNT(Employee_ID) AS Employee_Count
FROM Employees;

SELECT AVG(Salary) AS AVERAGE_SALARY
FROM Employees;

SELECT SUM(Salary) AS TOTAL_SALARY
FROM Employees;