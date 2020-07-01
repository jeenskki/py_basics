INSERT INTO departments (department_id, department_name, manager_id, location_id)
                 VALUES (300, 'BigData Analytics', null, 1700);
                 
SELECT * FROM departments;

CREATE TABLE emps AS SELECT * FROM employees;

SELECT employee_id, first_name, salary
FROM emps
WHERE employee_id = 103;

-- UPDATE는 반드시 WHERE와 함께 할 것!!! 까먹으면 데이터를 전체에 덮어쓰기 때문에 지옥행 티켓 GET
UPDATE emps
SET salary = salary * 1.1
WHERE employee_id = 103;

UPDATE emps
SET (job_id, salary, manager_id) =
    (SELECT job_id, salary, manager_id
     FROM emps
     WHERE employee_id = 108)
WHERE employee_id = 109;

DROP TABLE emps

DELETE FROM emps
WHERE employee_id = 109;
COMMIT; 

-- 제약조건이 걸린(ex. 참조) 데이터는 제거 불가. 데이터가 꼬이는 현상이 발생할 수도 있음.







