import mysql.connector

def db_init():
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1"
    )
    cursor = mydb.cursor()

    cursor.execute("DROP DATABASE IF EXISTS assignment")
    cursor.execute("CREATE DATABASE assignment")
    cursor.close()

    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="assignment"
    )
    cursor = mydb.cursor()

    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS tokens")
    cursor.execute("CREATE TABLE users (id int NOT NULL AUTO_INCREMENT, username VARCHAR(255), password VARCHAR(255), type VARCHAR(255), PRIMARY KEY(id))")
    cursor.execute("CREATE TABLE tokens (id int NOT NULL AUTO_INCREMENT, token_value VARCHAR(255), PRIMARY KEY(id))")
    cursor.execute("INSERT INTO users (username,password,type) VALUES ('admin','adminP@ssw0rd','0')")
    cursor.execute("INSERT INTO users (username,password,type) VALUES ('johnny','t0rt0iss3','1')")
    mydb.commit()
    cursor.close()
    return 'init database'


if __name__ == "__main__":
    db_init()
