-- # Write your MySQL query statement below
select prd.product_name, sl.year, sl.price from product as prd right join sales as sl on prd.product_id = sl.product_id;

-- best 
-- # Write your MySQL query statement below
select P.product_name , S.year , S.price from Sales as S
join Product as P on S.product_id = P.product_id;