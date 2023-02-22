1873. Calculate Special Bonus
https://leetcode.com/problems/calculate-special-bonus/

SELECT employee_id, 
IF (employee_id % 2 = 1 AND name NOT LIKE 'M%', salary, 0) AS bonus
FROM Employees