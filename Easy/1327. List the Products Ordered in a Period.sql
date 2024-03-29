SELECT product_name, SUM(unit) AS unit
FROM Products 
LEFT JOIN Orders
USING(product_id)
WHERE MONTH(order_date) = 2 AND YEAR(order_date) = 2020
GROUP BY product_id
HAVING unit >= 100;
