import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="test")
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM PLAYER")
mycursor.execute(
    "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
print(mydb)
