#create a connection and create a new database....
import mysql.connector 
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="robin"
)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE login")