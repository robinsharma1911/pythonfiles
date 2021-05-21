#if table already exist use ALTER TABLE keyword...
#create primary key on an existing table customer....
import mysql.connector 
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="robin",
    database="mydatabase"
)
mycursor=mydb.cursor()
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")