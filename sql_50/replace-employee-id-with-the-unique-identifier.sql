-- # Write your MySQL query statement below
select COALESCE(b.unique_id,null) as unique_id, a.name from Employees a
left join EmployeeUNI b
on a.id = b.id

-- # Write your MySQL query statement below
select emu.unique_id, emp.name from Employees as emp left join EmployeeUNI as emu on emp.id=emu.id;