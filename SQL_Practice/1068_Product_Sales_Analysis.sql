-- 1068. Product Sales Analysis I
-- Write a solution to report the product_name, year, and price for each sale_id in the Sales table.
-- Return the resulting table in any order.
-- The result format is in the following example.

select product.product_name, sales.year, sales.price from sales join product
on sales.product_id = product.product_id
