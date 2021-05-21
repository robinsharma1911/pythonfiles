import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="robin",
  database="record"
)
mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE customers(account INT PRIMARY KEY,name VARCHAR(255),amt INT)")
