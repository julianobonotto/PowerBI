SELECT e1.*, e2.Fname AS SuperFname, e2.Minit AS SuperMinit, e2.Lname AS SuperLname, CONCAT(e2.Fname," ", e2.Minit, " ", e2.Lname) AS SuperName
FROM employee AS e1
LEFT JOIN employee AS e2 ON e1.Super_ssn = e2.Ssn;
