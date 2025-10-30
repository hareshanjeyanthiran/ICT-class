CREATE TABLE Salesman(
    Salesman_id NUMBER PRIMARY KEY,
    NAME TEXT,
    CITY TEXT,
    Commission TEXT
);

INSERT INTO Salesman(Salesman_id,NAME,CITY,Commission)
VALUES
(5001,'James Hoog','New york','0.15'),
(5002,'Nail Knite','Paris','0.13'),
(5005,'Pit Alex','London','0.11'),
(5006,'Mc Lyon','Paris','0.14'),
(5007,'Paul Adam','Rome','0.13'),
(5003,'Lauson Hen','San Jose','0.12');

CREATE TABLE Customer(
    Customer_ID NUMBER PRIMARY KEY,
    Cust_Name TEXT,
    City TEXT,
    Grade NUMBER,
    Salesman_id NUMBER
);

INSERT INTO Customer(Customer_id,Cust_Name,City,Grade,Salesman_id)
VALUES
(3002,'Nick Rimando','New york',100,5001),
(3007,'Brad Devis','New york',200,5001),
(3005,'Graham Zusi','California',200,5002),
(3008,'Julian Green','London',300,5002),
(3004,'Fabian Johnson','Paris',300,5006),
(3009,'Geoff Camron','Berlin',100,5003),
(3003,'Jorzy Altridor','Moscow',200,5007),
(3001,'Brad Guzan','London',300,5005);

CREATE TABLE Orders(
    ord_no NUMBER PRIMARY KEY,
    putch_amt NUMBER,
    ord_date DATE,
    Customor_id NUMBER,
    Salesman_id NUMBER
);


INSERT INTO Orders(ord_no,putch_amt,ord_date,Customor_id,Salesman_id)
VALUES
(7001,150.5,'2012-10-05',3005,5002),
(7009,270.65,'2012-09-10',3001,5001),
(7002,65.26,'2012-10-05',3002,5003),
(7004,110.5,'2012-08-17',3009,5007),
(7007,948.5,'2012-09-10',3005,5005),
(7005,2400.6,'2012-07-27',3007,5006)

