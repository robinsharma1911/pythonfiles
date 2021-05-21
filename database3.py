#create table in mydatabase
import mysql.connector 
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="robin",
    database="mydatabase"
)
mycursor=mydb.cursor()
'''
mycursor.execute("CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255))")
'''
#CHECK IF TABLE IS EXISTS...

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)