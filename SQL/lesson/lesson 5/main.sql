-- Create Salesman table
CREATE TABLE Salesman (
    Salesman_id INTEGER PRIMARY KEY,
    Name TEXT,
    City TEXT,
    Commission REAL
);

INSERT INTO Salesman (Salesman_id, Name, City, Commission)
VALUES
(5001, 'James Hoog', 'New York', 0.15),
(5002, 'Nail Knite', 'Paris', 0.13),
(5005, 'Pit Alex', 'London', 0.11),
(5006, 'Mc Lyon', 'Paris', 0.14),
(5007, 'Paul Adam', 'Rome', 0.13),
(5003, 'Lauson Hen', 'San Jose', 0.12);


CREATE TABLE Customer (
    Customer_id INTEGER PRIMARY KEY,
    Cust_Name TEXT,
    City TEXT,
    Grade INTEGER,
    Salesman_id INTEGER,
    FOREIGN KEY (Salesman_id) REFERENCES Salesman(Salesman_id)
);

INSERT INTO Customer (Customer_id, Cust_Name, City, Grade, Salesman_id)
VALUES
(3002, 'Nick Rimando', 'New York', 100, 5001),
(3007, 'Brad Devis', 'New York', 200, 5001),
(3005, 'Graham Zusi', 'California', 200, 5002),
(3008, 'Julian Green', 'London', 300, 5002),
(3004, 'Fabian Johnson', 'Paris', 300, 5006),
(3009, 'Geoff Camron', 'Berlin', 100, 5003),
(3003, 'Jorzy Altridor', 'Moscow', 200, 5007),
(3001, 'Brad Guzan', 'London', 300, 5005);


CREATE TABLE Orders (
    Ord_no INTEGER PRIMARY KEY,
    Purch_amt REAL,
    Ord_date DATE,
    Customer_id INTEGER,
    Salesman_id INTEGER,
    FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id),
    FOREIGN KEY (Salesman_id) REFERENCES Salesman(Salesman_id)
);

INSERT INTO Orders (Ord_no, Purch_amt, Ord_date, Customer_id, Salesman_id)
VALUES
(7001, 150.5, '2012-10-05', 3005, 5002),
(7009, 270.65, '2012-09-10', 3001, 5001),
(7002, 65.26, '2012-10-05', 3002, 5003),
(7004, 110.5, '2012-08-17', 3009, 5007),
(7007, 948.5, '2012-09-10', 3005, 5005),
(7005, 2400.6, '2012-07-27', 3007, 5006);

-------------------------------------------------
-- QUERIES
-------------------------------------------------

-- 1. Matching customers and salesmen by city
SELECT Customer.Cust_Name, Salesman.Name, Salesman.City
FROM Customer
JOIN Salesman ON Customer.City = Salesman.City;

-- 2. Linking customers to their salesmen
SELECT Customer.Cust_Name, Salesman.Name
FROM Customer
JOIN Salesman ON Customer.Salesman_id = Salesman.Salesman_id;

-- 3. Orders where customer's city does not match salesman's city
SELECT Orders.Ord_no, Customer.Cust_Name, Orders.Customer_id, Orders.Salesman_id
FROM Orders
JOIN Customer ON Orders.Customer_id = Customer.Customer_id
JOIN Salesman ON Orders.Salesman_id = Salesman.Salesman_id
WHERE Customer.City <> Salesman.City;

-- 4. Customers with salesmen where commission is between 0.12 and 0.14
SELECT 
    Customer.Cust_Name AS Customer,
    Customer.City AS City,
    Salesman.Name AS Salesman,
    Salesman.Commission
FROM Customer
JOIN Salesman ON Customer.Salesman_id = Salesman.Salesman_id
WHERE Salesman.Commission BETWEEN 0.12 AND 0.14;

-- 5. Calculating commissions for orders where customer grade is 200 or more
SELECT 
    Orders.Ord_no,
    Customer.Cust_Name,
    Salesman.Commission AS "Commission%",
    Orders.Purch_amt * Salesman.Commission AS Commission
FROM Orders
JOIN Salesman ON Orders.Salesman_id = Salesman.Salesman_id
JOIN Customer ON Orders.Customer_id = Customer.Customer_id
WHERE Customer.Grade >= 200;

-- 6. Orders on a specific date
SELECT * 
FROM Customer
JOIN Orders ON Customer.Customer_id = Orders.Customer_id
WHERE Orders.Ord_date = '2012-10-05';
