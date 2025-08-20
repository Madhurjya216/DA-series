USE TEST;

CREATE TABLE sales_data (
    SaleID INT PRIMARY KEY AUTO_INCREMENT,
    SaleDate DATE,
    Region VARCHAR(50),
    Product VARCHAR(100),
    Category VARCHAR(50),
    Quantity INT,
    UnitPrice DECIMAL(10,2),
    Discount DECIMAL(5,2),   -- stored as percentage e.g. 10 = 10%
    CustomerID INT
);

INSERT INTO sales_data (SaleDate, Region, Product, Category, Quantity, UnitPrice, Discount, CustomerID) VALUES
('2024-01-15', 'North', 'Laptop Pro 15', 'Electronics', 5, 1200.00, 10.00, 101),
('2024-01-20', 'South', 'Wireless Mouse', 'Accessories', 20, 25.00, 0.00, 102),
('2024-02-03', 'East', 'Desk Chair', 'Furniture', 2, 180.00, 5.00, 103),
('2024-02-10', 'West', 'Laptop Pro 15', 'Electronics', 1, 1200.00, 15.00, 104),
('2024-02-14', 'North', 'Monitor 27"', 'Electronics', 8, 299.99, 12.00, 105),
('2024-03-01', 'South', 'Keyboard Mechanical', 'Accessories', 15, 89.99, 0.00, 101),
('2024-03-08', 'East', 'Laptop Air 13', 'Electronics', 3, 999.00, 8.00, 106),
('2024-03-12', 'West', 'Printer X200', 'Electronics', 4, 149.99, 10.00, 107),
('2024-04-05', 'North', 'Laptop Pro 15', 'Electronics', 6, 1200.00, 10.00, 102),
('2024-04-18', 'South', 'USB-C Hub', 'Accessories', 25, 39.99, 0.00, 108),
('2024-05-02', 'East', 'Office Desk', 'Furniture', 1, 250.00, 5.00, 109),
('2024-05-15', 'West', 'Monitor 27"', 'Electronics', 6, 299.99, 7.50, 110),
('2024-06-01', 'North', 'Laptop Pro 15', 'Electronics', 2, 1200.00, 10.00, 103),
('2024-06-18', 'South', 'Chair Ergonomic', 'Furniture', 4, 199.00, 0.00, 111),
('2024-07-09', 'East', 'Printer X200', 'Electronics', 1, 149.99, 5.00, 112),
('2024-07-20', 'West', 'Laptop Air 13', 'Electronics', 2, 999.00, 8.00, 113),
('2024-08-11', 'North', 'Mouse Pad', 'Accessories', 50, 4.99, 0.00, 114),
('2024-08-24', 'South', 'Laptop Pro 15', 'Electronics', 3, 1200.00, 12.00, 115),
('2024-09-02', 'East', 'Desk Chair', 'Furniture', 3, 180.00, 0.00, 116),
('2024-09-18', 'West', 'Monitor 27"', 'Electronics', 7, 299.99, 9.00, 117);



SELECT * FROM SALES_DATA
WHERE Region = 'north' and Quantity > 10;

select * from sales_data
where Product = 'Laptop pro 15'
order by SaleDate desc;



SELECT SUM(Quantity * UnitPrice * (1 - Discount/100)) AS total_revenue_after_discount
FROM sales_data;




Select * from sales_data;
















drop table customers;




