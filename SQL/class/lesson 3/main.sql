CREATE TABLE PRODUCTS(
    PRODUCT_ID TEXT,
    PRODUCT_NAME TEXT,
    SUPPLIER_ID TEXT,
    UNIT TEXT,
    PRICE REAL
);

INSERT INTO PRODUCTS (PRODUCT_ID, PRODUCT_NAME, SUPPLIER_ID, UNIT, PRICE) VALUES
('1', 'Chai', '1', '10 boxes x 20 bags', 18.00),
('2', 'Chang', '1', '24 - 12 oz bottles', 19.00),
('3', 'Aniseed Syrup', '1', '12 - 550 ml bottles', 10.00),
('4', 'Chef Anton''s Cajun Seasoning', '2', '48 - 6 oz jars', 22.00),
('5', 'Chef Anton''s Gumbo Mix', '2', '36 boxes', 21.35),
('6', 'Grandma''s Boysenberry Spread', '3', '12 - 8 oz jars', 25.00);

SELECT COUNT(PRODUCT_ID) AS Product_Count 
FROM PRODUCTS;

SELECT AVG(PRICE) AS AVERAGE_PRICE 
FROM PRODUCTS;