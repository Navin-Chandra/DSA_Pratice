-- working # Write your MySQL query statement below
SELECT v.customer_id, COUNT(v.visit_id) as count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.transaction_id is NULL
GROUP BY v.customer_id

-- # Write your MySQL query statement below

-- select vs.customer_id as customer_id, count(vs.visit_id) as count_no_trans
-- from Visits as vs
-- left join Transactions as ts 
-- on vs.visit_id = ts.visit_id
-- where ts.amount is NULL
-- group by vs.customer_id;

-- SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans 
-- from Visits v 
-- LEFT JOIN Transactions t 
-- ON v.visit_id = t.visit_id  
-- WHERE t.amount IS NULL 
-- GROUP BY v.customer_id; 

-- # working
SELECT  customer_id, count(*) AS count_no_trans FROM Visits 
WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
GROUP BY customer_id