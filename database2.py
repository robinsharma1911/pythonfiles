#try connecting to database named mydatabase
import mysql.connector 
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="robin",
    database="mydatabase"
)
print(mydb)
#if no error occour mean's connection established