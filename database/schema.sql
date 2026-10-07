CREATE DATABASE IF NOT EXISTS sales_db;
USE sales_db;

CREATE TABLE IF NOT EXISTS sales_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    sale_month INT NOT NULL,
    sales_amount DECIMAL(12,2) NOT NULL
);

INSERT INTO sales_data (sale_month, sales_amount) VALUES
(1, 12000),(2, 13500),(3, 14200),(4, 15000),(5, 16800),(6, 17500),
(7, 18100),(8, 19500),(9, 20300),(10, 21400),(11, 22800),(12, 24000);
