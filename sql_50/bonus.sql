-- # Write your MySQL query statement below my solution
select e.name, b.bonus from Employee as e left join Bonus as b 
on e.empId = b.empId where b.bonus < 1000 or b.bonus is null;

-- #  anothe Write your MySQL query statement below
SELECT
    Employee.name,
    Bonus.bonus
FROM Employee
    LEFT JOIN Bonus ON
        Employee.empId = Bonus.empId
WHERE
    IFNULL(Bonus.bonus, 0) < 1000