# COURSERA 'Identifying Security Vulnerabilities' Course:
## Week 2: Mitigating SQL Injection Using Stored Procedures
### SQL INJECTIONS

![SQL Injection](https://bobby-tables.com/img/xkcd.png)

SQL injection is the placement of malicious code in SQL statements, via web page input.
SQL injection usually occurs when you ask a user for input, like their username/userid, and instead of a name/id, 
the user gives you an SQL statement that you will unknowingly run on your database.

## SQL Injection – Basic Concepts

There are two types of SQL Injection

• SQL Injection into a String/Char parameter
  Example: SELECT * from table where example = 'Example'

• SQL Injection into a Numeric parameter
  Example: SELECT * from table where id = 123


### Do parameters prevent SQL injection?

This method, _parametrized queries_, makes it possible for the database to recognize the code and distinguish it from input data. The user input is automatically quoted and the supplied input will not cause the change of the intent, so this coding style helps mitigate an SQL injection attack.

A Parameterized Query is a query in which placeholders are used for parameters and the parameters' values are supplied at the execution time, it is one of the simplest and most useful advanced queries you can create. This allows you to place parameters in an SQL query instead of putting in a constant or fixed value.


## Advice:

- “placeholders” which sanitize dynamic data for you. As long as you use those instead of dynamically constructing your own SQL strings, you should be fine




Look at the following example which creates a SELECT statement by adding a variable (txtUserId) to a select string. The variable is fetched from user input (getRequestString):
**Example**:

`txtUserId = getRequestString("UserId");
txtSQL = "SELECT * FROM Users WHERE UserId = " + txtUserId;`





# Prevention:

### Primary Defenses:

   - Option 1: Use of Prepared Statements (with Parameterized Queries)
   - Option 2: Use of Properly Constructed Stored Procedures
   - Option 3: Allow-list Input Validation
    -Option 4: Escaping All User Supplied Input

### Additional Defenses:

   - Also: Enforcing Least Privilege
   - Also: Performing Allow-list Input Validation as a Secondary Defense
   
   Make sure unvalidated user input doesn't end up in the query. Please note, this is a symptom of poor design and a full rewrite should be considered if time allows.
   

### Primary Defenses in More Detail:

Defense Option 1: Prepared Statements (with Parameterized Queries)

The use of prepared statements with variable binding (aka parameterized queries) is how all developers should first be taught how to write database queries. They are simple to write, and easier to understand than dynamic queries. Parameterized queries force the developer to first define all the SQL code, and then pass in each parameter to the query later. This coding style allows the database to distinguish between code and data, regardless of what user input is supplied.

Prepared statements ensure that an attacker is not able to change the intent of a query, even if SQL commands are inserted by an attacker. In the safe example below, if an attacker were to enter the userID of tom' or '1'='1, the parameterized query would not be vulnerable and would instead look for a username which literally matched the entire string tom' or '1'='1.


Defense Option 2: Stored Procedures

Stored procedures are not always safe from SQL injection. However, certain standard stored procedure programming constructs have the same effect as the use of parameterized queries when implemented safely which is the norm for most stored procedure languages.

They require the developer to just build SQL statements with parameters which are automatically parameterized unless the developer does something largely out of the norm. The difference between prepared statements and stored procedures is that the SQL code for a stored procedure is defined and stored in the database itself, and then called from the application. Both of these techniques have the same effectiveness in preventing SQL injection so your organization should choose which approach makes the most sense for you.

Defense Option 3: Allow-list Input Validation

Various parts of SQL queries aren't legal locations for the use of bind variables, such as the names of tables or columns, and the sort order indicator (ASC or DESC). In such situations, input validation or query redesign is the most appropriate defense. For the names of tables or columns, ideally those values come from the code, and not from user parameters.

Defense Option 4: Escaping All User-Supplied Input¶

This technique should only be used as a last resort, when none of the above are feasible. Input validation is probably a better choice as this methodology is frail compared to other defenses and we cannot guarantee it will prevent all SQL Injection in all situations.

This technique is to escape user input before putting it in a query. It is very database specific in its implementation. It's usually only recommended to retrofit legacy code when implementing input validation isn't cost effective.




### **Unsafe Example:**

### _How to Locate Potentially Vulnerable Code_

- A secure way to build SQL statements is to construct all queries with PreparedStatement instead of Statement and/or to use parameterized stored procedures. Parameterized stored procedures are compiled before user input is added, making it impossible for a hacker to modify the actual SQL statement.

- The account used to make the database connection must have “Least privilege.” If the application only requires read access then the account must be given read access only.

- Avoid disclosing error information: Weak error handling is a great way for an attacker to profile SQL injection attacks. Uncaught SQL errors normally give too much information to the user and contain things like table names and procedure names

**SQL injection flaws typically look like this:**

The following (Java) example is UNSAFE, and would allow an attacker to inject code into the query that would be executed by the database. The unvalidated "customerName" parameter that is simply appended to the query allows an attacker to inject any SQL code they want. Unfortunately, this method for accessing databases is all too common.

`String query = "SELECT account_balance FROM user_data WHERE user_name = "
             + request.getParameter("customerName");
try {
    Statement statement = connection.createStatement( ... );
    ResultSet results = statement.executeQuery( query );
}
...`


In rare circumstances, prepared statements can harm performance. When confronted with this situation, it is best to either a) strongly validate all data or b) escape all user supplied input using an escaping routine specific to your database vendor.


![Strategies for SQL Injection Attacks](https://github.com/emreYbs/Picus-Security-Bootcamp/blob/main/Week%202/Coursera/Identifying%20Security%20Vulnerabilities/Strategies%20Against%20SQL%20Injection%20Attacks.png)





## Key Words to Know:
- **Parametrization**, _also spelled parameterization_, _parametrisation_ or _parameterisation_, is the process of defining or choosing parameters. 
- use input validation or proper escaping
- 


### Resources:
- https://www.w3schools.com/sql/sql_injection.asp
- https://download.oracle.com/oll/tutorials/SQLInjection/index.htm
- https://wiki.owasp.org/index.php/Reviewing_Code_for_SQL_Injection
