#create table in mydatabase
import mysql.connector 
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="robin",
    database="mydatabase"
)
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE customers1(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),address VARCHAR(255))")
