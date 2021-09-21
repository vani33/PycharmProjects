import mysql.connector

mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    password="root",
    database="hcl"
)

print(mydb)

myCursor = mydb.cursor()

myCursor.execute("CREATE DATABASE pythonprograms")
myCursor.execute("SHOW DATABASES")
myCursor.execute("CREATE TABLE pythonMysql (name VARCHAR, age INTEGER)")
myCursor.execute("SHOW TABLES")

myCursor.execute("SELECT * FROM pythonMysql")
myResultset = myCursor.fetchall() #fetchone()
for x in myResultset:
    print(x)

















