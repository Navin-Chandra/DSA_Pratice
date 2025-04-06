-- 1581. Customer Who Visited but Did Not Make Any Transactions
-- Write a solution to find the IDs of the users who visited without making any transactions
-- and the number of times they made these types of visits.
-- Return the result table sorted in any order.

-- subquery approch
SELECT customer_id, count(distinct visit_id) count_no_trans from visits 
where visit_id not in(

    SELECT visit_id from transactions
)
group by customer_id



-- left join
xSELECT customer_id, count(visits.visit_id) count_no_trans from visits left join transactions
on visits.visit_id=transactions.visit_id
where transactions.transaction_id is null
group by customer_id;


