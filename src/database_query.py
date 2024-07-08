from os import getenv
import pymssql

server = getenv("PYMSSQL_TEST_SERVER")
user = getenv("PYMSSQL_TEST_USERNAME")
password = getenv("PYMSSQL_TEST_PASSWORD")
database = getenv("PYMSSQL_TEST_DATABASE")

with pymssql.connect(server, user, password, database) as conn:
    with conn.cursor(as_dict=True) as cursor:
        sql = """
              IF OBJECT_ID('persons', 'U') IS NOT NULL
              DROP TABLE persons
              CREATE TABLE persons (
                id INT NOT NULL,
                name VARCHAR(100),
                salesrep VARCHAR(100),
                PRIMARY KEY(id)
        )"""

        cursor.execute(sql)

        sql = "INSERT INTO persons VALUES (%d, %s, %s)"

        cursor.executemany(sql, [(1, 'John Smith', 'John Doe'),
                                 (2, 'Jane Doe', 'Joe Dog'),
                                 (3, 'Mike T.', 'Sarah H.')])

        conn.commit()

        cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'Joe Dog')

        for row in cursor:
            print("ID=%d, Name=%s" % (row['id'], row['name']))

