-- Write a solution to report the name and bonus amount of each employee
-- with a bonus less than 1000.
-- Return the result table in any order.
-- The result format is in the following example.
-- # Write your MySQL query statement below

select employee.name, bonus.bonus
from employee left join bonus 
on employee.empid = bonus.empid
where bonus.bonus < 1000 or bonus.bonus is null 
