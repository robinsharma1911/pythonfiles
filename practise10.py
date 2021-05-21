import numpy as np 
from tkinter import Tk,Label,Button
window=Tk()
window.geometry("400x400+50+50")
window.title("show matrix")
lable1=Label(window,text=" ")
lable1.place(x=10,y=10,width=200,height=200)
def myfunc():
    arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[33,22,11]],[[12,24,36],[13,26,39]],[[14,28,42],[15,30,45]]])
    lable1.configure(text=arr)
    print(arr[3,1])
button1=Button(window,text="click",command=myfunc)
button1.place(x=10,y=220,height=30,width=30)




window.mainloop()