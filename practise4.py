#create a window using tkinter
from tkinter import Tk,Label,Button,Entry,messagebox,scrolledtext,Menu
from tkinter import *
window = Tk()
window.title('likegeeks.com')
window.geometry('370x340+700+100')

#add a menu bar...
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
new_item.add_command(label='save')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

#work start...
lable1=Label(window,text="enter the text",width=10,foreground="yellow",background="blue")
lable1.place(x=50,y=20,height=25,width=80)
input1=Entry(window,width=20)
input1.place(x=140,y=20,height=25,width=120)
def myfunc():
    res=input1.get()
    lable2.configure(text=res)
    input1.delete()
button1=Button(window,text="click",foreground="yellow",background="blue" ,command=myfunc)
button1.place(x=280,y=20,height=25,width=45)
lable2=Label(window ,text="")
lable2.place(x=160,y=45,height=25,width=60)

#create a message box...
def myfunc1():

    box1=messagebox.askokcancel('do you want to exit','press ok for exit')
    
    if box1 == True:
        window.destroy()
    else:
        pass
button2=Button(window,text='exit',command=myfunc1)
button2.place(x=60,y=60,height=20,width=30)
#checkbox button....
chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.place(x=20,y=90,height=30,width=70)
chk_state = IntVar()
print(chk_state.set(0)) #uncheck
print(chk_state.set(1)) #check

#radio button...
selected = IntVar()
rad1 = Radiobutton(window,text='First', value=1, variable=selected)
rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
rad3 = Radiobutton(window,text='Third', value=3, variable=selected)
def clicked():
   no=selected.get()
   if no==1:
       messagebox.showinfo('radiobutton','first is selected')
   if no==2:
        messagebox.showinfo('radiobutton','second is selected')
   if no==3:
        messagebox.showinfo('radiobutton','third is selected')
btn = Button(window, text="Click Me", command=clicked)
rad1.place(x=20,y=110,height=70,width=60)
rad2.place(x=90,y=110,height=70,width=60)
rad3.place(x=160,y=110,height=70,width=60)
btn.place(x=20,y=170,height=20,width=50)

#scrolled text...
txt = scrolledtext.ScrolledText(window,width=30,height=10)
txt.place(x=220,y=200,height=100,width=130)
#txt.insert(INSERT,'enter your text')
#txt.delete(1.0,END)

#defualt value for spinbox...
var =IntVar()
var.set(1)
spin = Spinbox(window, from_=0, to=100, width=10, textvariable=var)
spin.place(x=40,y=200,height=20,width=30)



window.mainloop()