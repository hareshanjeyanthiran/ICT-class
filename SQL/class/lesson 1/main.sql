CREATE TABLE  students(
student_id INT PRIMARY KEY ,
name  VARCHAR(40),
gender VARCHER(1),
grade INT
);

INSERT INTO students (student_id,name , gender, grade)
VALUES
(1,"Hareshan","M",8),
(2,"Rahul","M",6),
(3,"sree","F",7)

SELECT * FROM students;