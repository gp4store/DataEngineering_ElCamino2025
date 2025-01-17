-- Part 1: DDL (Data Definition Language)

--     Create a Customers_yourinitial table with the following columns:
--         CustomerID Primary Key Identity (1,1)
--         FirstName
--         LastName
--         Email
--         Phone

USE pt-students-07-31-24;

DROP TABLE IF EXISTS dbo.Customers_GP 

CREATE TABLE dbo.Customers_GP (
    Customer_id INT PRIMARY KEY IDENTITY (1,1), 
    FirstName varchar(30),
    LastName varchar(30),
    Email varchar(30),
    Phone varchar(14)
);

--     Create a Products_yourinitial table with the following columns:
--         ProductID Primary Key Identity (1,1)
--         ProductName
--         Price
--         StockQuantity

USE pt-students-07-31-24;

DROP TABLE IF EXISTS dbo.Products_GP 

CREATE TABLE dbo.Products_GP (
    Product_id INT PRIMARY KEY IDENTITY (1,1), 
    ProductName varchar(30),
    Price float,
    StockQuantity varchar(30)
);

--     Create an Orders_yourinitial table with the following columns:
--         OrderID Primary Key Identity (1,1)
--         CustomerID (Foreign Key referencing Customers)
--         ProductID (Foreign Key referencing Products)
--         OrderDate
--         Quantity

USE pt-students-07-31-24;

DROP TABLE IF EXISTS dbo.Orders_GP 

CREATE TABLE dbo.Orders_GP (
    Order_id INT PRIMARY KEY IDENTITY (1,1),
    Customer_id int,
    FOREIGN KEY(Customer_id) REFERENCES Customers_GP(Customer_id), 
    Product_id int, 
    FOREIGN KEY(Product_id) REFERENCES Products_GP(Product_id),
    OrderDate date,
    Quantity varchar(99)
);

--     Alter the Customers table to add a column called DateOfBirth.

USE pt-students-07-31-24;

ALTER TABLE Customers_GP
ADD DateOfBirth date;

--     Alter the Products table to add a column called Category.

USE pt-students-07-31-24;

ALTER TABLE Products_GP
ADD Category varchar(99);

-- Part 2: Stored Procedures

--     Write a stored procedure to insert a new customer into the Customers table.

CREATE PROCEDURE sp_insert_customer_GP
AS
BEGIN
    INSERT INTO Customers_GP(FirstName, LastName, Email, Phone, DateOfBirth)
    VALUES ('John', 'Doe', 'xxxx@xxxx.com', '999-999-9999', '0000/00/00')
END;

EXEC sp_insert_customer_GP;