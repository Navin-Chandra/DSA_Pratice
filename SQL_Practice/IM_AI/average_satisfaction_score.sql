-- To calculate the average satisfaction score per department, rounded down to the nearest whole number
SELECT  
department_id, 
round(avg(satisfaction_score)) as avg_satisfaction_score
from employee_satisfaction
GROUP by department_id

-- ROUND() → nearest whole number
-- FLOOR() → always rounds down
-- CEIL() → always rounds up

-- FLOOR() — rounds it down to the nearest whole number.
SELECT department_id, ROUND(AVG(satisfaction_score))
FROM employee_satisfaction
GROUP BY department_id;


-- level up
-- To calculate the average satisfaction score per department and job category, rounded down, you just add job_category_id
-- to both the SELECT and the GROUP BY.

SELECT 
    department_id,
    job_category_id,
    FLOOR(AVG(satisfaction_score)) AS avg_satisfaction_score
FROM 
    employee_satisfaction
GROUP BY 
    department_id, 
    job_category_id;
