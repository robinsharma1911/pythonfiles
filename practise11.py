#enter values and show on lable..
from tkinter import Tk,Label,Button,Entry
window=Tk()
window.geometry("300x300+50+50")
window.title('mywindow')
entry1=Entry(window,text="",bd=5)
entry1.place(x=20,y=20)
entry2=Entry(window,text="",bd=5)
entry2.place(x=40,y=90)
arr="robin"
lable1=Label(window,text=arr)
lable1.place(x=20,y=130,height=250,width=200)

class myclass:
   def __init__(self,name,age):
      self.name=name
      self.age=age
      print("hello")   
   def myfunc(self):
      print(self.name,self.age)
      arr=self.name,self.age
      lable1.configure(text=arr)
      

def myfunc2():
   name=(entry1.get())
   age=(entry2.get())
   x=myclass(name,age)
   x.myfunc()

button1=Button(window,text="click",command=myfunc2)
button1.place(x=60,y=50)


window.mainloop()