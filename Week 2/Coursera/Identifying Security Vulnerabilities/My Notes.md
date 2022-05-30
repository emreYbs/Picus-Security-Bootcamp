# COURSERA 'Identifying Security Vulnerabilities' Course:
## Week 2: Mitigating SQL Injection Using Stored Procedures
### SQL INJECTIONS

SQL injection is the placement of malicious code in SQL statements, via web page input.
SQL injection usually occurs when you ask a user for input, like their username/userid, and instead of a name/id, 
the user gives you an SQL statement that you will unknowingly run on your database.


Look at the following example which creates a SELECT statement by adding a variable (txtUserId) to a select string. The variable is fetched from user input (getRequestString):
**Example**:

`txtUserId = getRequestString("UserId");
txtSQL = "SELECT * FROM Users WHERE UserId = " + txtUserId;`











## Key Words to Know:
- **Parametrization**, _also spelled parameterization_, _parametrisation_ or _parameterisation_, is the process of defining or choosing parameters. 



### Resources:
- https://www.w3schools.com/sql/sql_injection.asp
- 
