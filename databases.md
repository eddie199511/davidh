# Working With Databases

1. The next topic we'll talk about is creating, inserting into, and querying a table in SQL Server.
2. You can download a free SQL Server developer edition for use with this [here](https://www.microsoft.com/en-us/sql-server/sql-server-downloads).
3. If you're using a Mac or Linux, then download MySQL [here](https://dev.mysql.com/downloads/mysql/). Let me know if you're on a Mac or Linux and I'll update the example.
4. This example assumes you have some user environment variables set:
    1. PYMSSQL_TEST_SERVER = localhost
    2. PYMSSQL_TEST_USERNAME = your database username
    3. PYMSSQL_TEST_PASSWORD = your database password
    4. PYMSSQL_TEST_DATABASE = the database you wish to connect to
5. Have a look at the [source code](src/database_query.py)
6. As always, you can run the code like this:
    ```bash
      cd src
      python database_query.py
   ```
[Back to README](README.md)   