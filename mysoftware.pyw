#create program to take input...
from tkinter import Tk,Label,Entry,Button,scrolledtext,INSERT,Radiobutton
import mysql.connector 
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="robin",
    database="mydatabase"
)
mycursor=mydb.cursor()
#window work start...
window=Tk()
window.title("myform")
window.geometry("500x500+100+100")
lable1=Label(window,text="name")
lable1.place(x=10,y=10)
entry1=Entry(window,width=10,bd=5)
entry1.place(x=50,y=10)
lable2=Label(window,text="address")
lable2.place(x=10,y=50)
entry2=Entry(window,width=10,bd=5)
entry2.place(x=50,y=50)
#function to insert data into customers table...
def myfunc():
    person=entry1.get()
    add=entry2.get()
    if len(entry1.get())!=0 and len(entry2.get())!=0:
        sql="INSERT INTO customers1(name,address) VALUES(%s,%s)"
        val=(person,add)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.lastrowid,"record inserted",)
    entry1.delete("0","end")
    entry2.delete("0","end")
button1=Button(window,text="click",command=myfunc)
button1.place(x=10,y=100)
#scrolltext box...
txt = scrolledtext.ScrolledText(window,bg="skyblue",fg="black")
txt.place(x=10,y=180,height=250,width=300)
#function to show table data
def myfunc1():
    sql="SELECT * FROM customers1"
    mycursor.execute(sql)
    data=mycursor.fetchall()
    msg = ""
    for x in data:
        msg = "id=" +str(x[0]) +"\nname="+ str(x[1]) + "\n"+"address="+str(x[2])+"\n\n"
        txt.insert(INSERT,msg)
def myfunc2():
    sql="Drop table customers"
    mycursor.execute(sql)
    print("delete the table")
button2=Button(window,text="show",command=myfunc1,bg="blue",fg="skyblue")
button2.place(x=10,y=140,height=40,width=50)
button3=Button(window,text="clear",command=myfunc2,bg="blue",fg="skyblue")
button3.place(x=60,y=140,height=40,width=50)

entry3=Entry(window,width=20,bd=10)
entry3.place(x=320,y=200)
def myfunc3():
    id1=entry3.get()
    sql="DELETE FROM customers1 WHERE id=id1"
    mycursor.execute(sql)
    print("record successfully deleted")
    entry3.delete("0","end")
button4=Button(window,text="delete user",bg="blue",fg="skyblue",command=myfunc3)
button4.place(x=320,y=250,height=35,width=70)

radiobutton1=Radiobutton(window,text="hindi",variable=1)
radiobutton2=Radiobutton(window,text="englist",variable=2)
radiobutton1.place(x=320,y=300)
radiobutton2.place(x=320,y=340)

window.mainloop()