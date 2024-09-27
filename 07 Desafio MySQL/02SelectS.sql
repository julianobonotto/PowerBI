-- localhost:3306
-- azure_company

select * from employee;

select * from departament;

select * from works_on;

select * from employee;

select * from dependent;

SELECT d.*, e.Fname FROM departament AS d
LEFT JOIN employee AS e ON  d.Mgr_ssn = e.Ssn