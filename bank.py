from bankdb import *
from tkinter import *
gui=Tk()
gui.geometry("800x700+300+5")
'''
def showpersons():
    mycursor.execute("SELECT * FROM customers")
    x=mycursor.fetchall()
    for z in x:
        print(z)
'''



class bank:
    global amt
    def __init__ (self,acc,name,amt):
        self.name=name
        self.acc=acc
        self.amt=amt
    def personal(self):
        print("name is="+self.name+"\naccountno is=",self.acc,"\namount",self.amt)

    def draw(self,amount):
        self.amount=amount
        if(self.amt>self.amount):
            self.amt=self.amt-self.amount
            print("after withdraw",self.amt)
            

    def check(self):
        print("total balance",self.amt)

    def deposite(self,amount):
        self.amount=amount
        self.amt=self.amount+self.amt
        print("after deposite",self.amt)
    
    def transfer(self,amount):
        self.amount=amount
        
        self.amt=self.amt-self.amount
        print("transfer succesfull",self.amount)


def logi():
    val=accentry.get()
    sql_query="SELECT * FROM customers WHERE account=%s"
    mycursor.execute(sql_query,(val,))
    global acc,name,amt
    acc=x[0]
    name=x[1]
    amt=x[2]
    
btndesp=Button(gui,text="deposite",command=lambda: deposite(300))
btndesp.place(x=550,y=20,height=40,width=60)
   
        
banklbl=Label(gui,text="Mybank",bd=0,fg="blue",bg="red",justify=CENTER,font=("Times New Roman",40,"bold"))
banklbl.place(x=200,y=20,height=60,width=300)

acclbl=Label(gui,text="Account No.",bd=15,bg="blue",font=("Times New Roman",20))
acclbl.place(x=50,y=100,height=40,width=150)

accentry=Entry(gui,text=" ")
accentry.place(x=210,y=100,height=40,width=180)

passlbl=Label(gui,text="Password",bd=15,bg="blue",font=("Times New Roman",20))
passlbl.place(x=50,y=150,height=40,width=150)

unameentry=Entry(gui,text=" ")
unameentry.place(x=210,y=150,height=40,width=180)

logbtn=Button(gui,text="login",bd=5,command=logi)
logbtn.place(x=140,y=200,height=40,width=60)


gui.mainloop()