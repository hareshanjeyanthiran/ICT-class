CREATE TABLE IF NOT EXISTS STUDENT (
   ROLL_NO TEXT PRIMARY KEY,
   name TEXT NOT NULL,
   ADDRESS TEXT,
   PHONE TEXT,
   AGE INTEGER
);

INSERT INTO STUDENT (ROLL_NO, name, ADDRESS, PHONE, AGE) VALUES
('1', 'RAM', 'Delhi', '******', 18),
('2', 'Ramesh', 'Gurgaon', '******', 18),
('3', 'Sujit', 'Delhi', '*******', 18),
('4', 'Suresh', 'Delhi', '*******', 18),
('5', 'Aman', 'Rohtak', '********', 20),
('6', 'Harsh', 'Gurgaon', '******', 19);

SELECT * FROM STUDENT WHERE AGE = 18 AND ADDRESS = 'Delhi';

SELECT * FROM STUDENT WHERE AGE = 18 AND name = 'RAM';

SELECT * FROM STUDENT WHERE name = 'RAM' OR name = 'Sujit';

SELECT * FROM STUDENT WHERE name = 'RAM' OR AGE = 20;