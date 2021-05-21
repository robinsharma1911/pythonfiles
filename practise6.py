from tkinter import Tk,Label,Entry,messagebox
from tkinter import *
window = Tk()
window.title('School Form')
window.geometry('1500x800+0+0')

#start work...
lable1=Label(window,text='SCHOOL FORM',fg='blue',bg='yellow',font=50)
lable1.place(x=0,y=10,height=50,width=1364)
#student name lable and entry
stdname=Label(window,text='Name of student')
stdname.place(x=20,y=80,height=30,width=100)

stdfill=Entry(window,bd=5)
stdfill.place(x=125,y=80,height=30,width=150)

#roll no lable and entry
rollno=Label(window,text='Roll No')
rollno.place(x=400,y=80,height=30,width=100)

rollfill=Entry(window,bd=5)
rollfill.place(x=500,y=80,height=30,width=150)

#father name lable and entry
fatname=Label(window,text='Father name')
fatname.place(x=20,y=150,height=30,width=100)

fatfill=Entry(window,bd=5)
fatfill.place(x=125,y=150,height=30,width=150)

#mother name lable and entry
motname=Label(window,text='Mother name')
motname.place(x=400,y=150,height=30,width=100)

motfill=Entry(window,bd=5)
motfill.place(x=500,y=150,height=30,width=150)

#contactno lable and entry
contact=Label(window,text='Contact No.')
contact.place(x=20,y=220,height=30,width=100)

contactfill=Entry(window,bd=5)
contactfill.place(x=125,y=220,height=30,width=150)


#address lable and entry
address=Label(window,text='Address')
address.place(x=400,y=220,height=30,width=100)

addfill=Entry(window,bd=5)
addfill.place(x=500,y=220,height=30,width=150)

#radiobutton to select gender
selected=IntVar()
male=Radiobutton(window,text='male',value=1, variable=selected)

female=Radiobutton(window,text='female',value=2, variable=selected)

def clicked():
    no=selected.get()
    if no==1:
       messagebox.showinfo('radiobutton','first is selected')
    if no==2:
        messagebox.showinfo('radiobutton','second is selected')
btn = Button(window, text="Click Me", command=clicked)

male.place(x=30,y=300,height=70,width=60)
female.place(x=90,y=300,height=70,width=60)
btn.place(x=30,y=480,height=20,width=50)

#checkbox button....
chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.place(x=30,y=380,height=30,width=70)
chk_state = IntVar()
print(chk_state.set(0)) #uncheck
print(chk_state.set(1)) #check





window.mainloop()