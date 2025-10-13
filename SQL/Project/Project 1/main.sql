CREATE TABLE Employes(
emp_id INT PRIMARY KEY ,
name  VARCHAR(40),
gender CHAR(1),
salary INT
);

INSERT INTO Employes (emp_id,name ,gender,salary) VALUES
(1,'Rahul','M',80000),
(2,'Kartik','M',60000),
(3,'Etan','M',70000),
(4,'Sree','F',90000),
(5,'Jileshan','M',75000);

SELECT * FROM Employes;