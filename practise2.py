#create window ..from tkinter using tk()
from tkinter import Tk,Label,Entry,Button,messagebox
root=Tk()
root.title("mywindow")
root.geometry("300x200+70+70")
lable1=Label(root,text="this is my new window")
lable1.place(x=5,y=3)
mytext=Entry(root)
mytext.place(x=4,y=2)
def myfunc():
    print(mytext.get())
mybutton=Button(root,text="print text",command=myfunc)
mybutton.place(x=3,y=1)

#popup window for ask question...
def func1():
    answer=messagebox.askquestion('do you want to exit','press yes if you want to exit')
    if answer == 'yes':
        root.destroy
    else:
        print("welcome to your window screen ")

exitbutton=Button(root,text="exit",command=func1)       
exitbutton.place(x=80,y=40,height=50,width=50)

root.mainloop()