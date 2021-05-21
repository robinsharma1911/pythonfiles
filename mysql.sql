import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="robin",
    pass="james123"
)
mycoursor=mydb.cursor()
mycoursor.execute("CREATE DATABASE mydatabase")                 