#insert mutiple row at a time using tuple at a time...
import mysql.connector 
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="robin",
    database="mydatabase"
)
mycursor=mydb.cursor()
sql="INSERT INTO customers(name,address) VALUES(%s,%s)"
val=[
    ("robin","delhi"),
    ("lokesh","west delhi"),
    ("james","south delhi")
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount,"record inserted")