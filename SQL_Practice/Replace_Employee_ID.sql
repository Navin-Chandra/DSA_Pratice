-- # Write a solution to show the unique ID of each user, 
-- If a user does not have a unique ID replace just show null.
select unique_id, name from employees as emp
left join EmployeeUNI as euni
on emp.id = euni.id