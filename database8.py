#Get inserted id ...
import mysql.connector 
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="robin",
    database="mydatabase"
)
mycursor=mydb.cursor()
sql="INSERT INTO customers(name,address) VALUES(%s,%s)"
val=("mohit","palwal")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.lastrowid,"record inserted",)