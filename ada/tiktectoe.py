#***********Tik Tac Toe Game By Robin Sharma************

from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.geometry ("400x450+700+100")
screen.title ('Tiktoe Game')
screen.config (bg='brown')

# variable used to show "x" and "0" 
zero= StringVar()
zero.set(" ")


#    ==========textvariables for each button===============
B1var = StringVar()
B1var.set(" ")
B2var= StringVar()
B2var.set(" ")
B3var= StringVar()
B3var.set(" ")
B4var= StringVar()
B4var.set(" ")
B5var= StringVar()
B5var.set(" ")
B6var= StringVar()
B6var.set(" ")
B7var= StringVar()
B7var.set(" ")
B8var= StringVar()
B8var.set(" ")
B9var= StringVar()
B9var.set(" ")


#     ==============functions===============

#to restart game after win or draw
def restart():
        B1var.set(" ")
        B1.configure(bg="grey")
        B2var.set(" ")
        B2.configure(bg="grey")
        B3var.set(" ")
        B3.configure(bg="grey")
        B4var.set(" ")
        B4.configure(bg="grey")
        B5var.set(" ")
        B5.configure(bg="grey")
        B6var.set(" ")
        B6.configure(bg="grey")
        B7var.set(" ")
        B7.configure(bg="grey")
        B8var.set(" ")
        B8.configure(bg="grey")
        B9var.set(" ")
        B9.configure(bg="grey")

#condition to check game draw....
def draw():
    if B1.cget('bg') == "green" and B2.cget('bg') == "green" and B3.cget('bg') == "green" and B4.cget('bg') == "green" and B5.cget('bg') == "green" and B6.cget('bg') == "green" and B7.cget('bg') == "green" and B8.cget('bg') == "green" and B9.cget('bg') == "green":
        messagebox.showinfo("Tik Tac Toe","Match Draw")
        restart()

#condition to check win....
def checkgame():
    flag = True
    if B1var.get() == "x" and B5var.get() == "x" and B9var.get() == "x" :
        flag = False
    elif B3var.get() == "x" and B5var.get() == "x" and B7var.get() == "x" :
        flag = False
    elif B2var.get() == "x" and B5var.get() == "x" and B8var.get() == "x" :
        flag = False
    elif B6var.get() == "x" and B5var.get() == "x" and B4var.get() == "x" :
        flag = False
    elif B1var.get() == "x" and B2var.get() == "x" and B3var.get() == "x" :
        flag = False
    elif B3var.get() == "x" and B6var.get() == "x" and B9var.get() == "x" :
        flag = False
    elif B9var.get() == "x" and B8var.get() == "x" and B7var.get() == "x" :
        flag = False
    elif B7var.get() == "x" and B4var.get() == "x" and B1var.get() == "x" :
        flag = False

    elif B1var.get() == "0" and B5var.get() == "0" and B9var.get() == "0" :
        flag = False
    elif B3var.get() == "0" and B5var.get() == "0" and B7var.get() == "0" :
        flag = False
    elif B2var.get() == "0" and B5var.get() == "0" and B8var.get() == "0" :
        flag = False
    elif B6var.get() == "0" and B5var.get() == "0" and B4var.get() == "0" :
        flag = False
    elif B1var.get() == "0" and B2var.get() == "0" and B3var.get() == "0" :
        flag = False
    elif B3var.get() == "0" and B6var.get() == "0" and B9var.get() == "0" :
        flag = False
    elif B9var.get() == "0" and B8var.get() == "0" and B7var.get() == "0" :
        flag = False
    elif B7var.get() == "0" and B4var.get() == "0" and B1var.get() == "0" :
        flag = False
    else:
        draw()

    if flag == False:
        messagebox.showinfo("Tik Tac Toe","Match Win")  
        restart()
        

#change state of box by "x" or "0"
def changestate(textname=" ",Bno =" "):
    if Bno.cget('bg') == "grey":
        if zero.get() == "x":
            zero.set("0")
        else:
            zero.set("x")
        textname.set(zero.get())
        Bno.configure(bg="green")
        checkgame()
    
#  ================GUI Interface =================

window = Frame(screen, bd=5,bg="blue" )
window.grid()

B1 = Button( window, bg='grey', bd = 1 ,textvariable=B1var, width=15, height= 8, command=lambda: changestate(B1var,B1))      
B1.grid(row=0, column=0, padx=4, pady=4, ipadx=5, ipady=4)               
B2 = Button( window, bg='grey',bd = 1, textvariable=B2var, width=15, height= 8, command=lambda: changestate(B2var,B2)  )      
B2.grid(row=0, column=1, padx=4, pady=4, ipadx=5, ipady=4)
B3 = Button( window, bg='grey',bd = 1 ,textvariable=B3var, width=15, height= 8, command=lambda: changestate(B3var,B3))      
B3.grid(row=0, column=2, padx=4, pady=4, ipadx=5, ipady=4)
B4 = Button( window, bg='grey',bd = 1 ,textvariable=B4var, width=15, height= 8, command=lambda: changestate(B4var,B4))      
B4.grid(row=1, column=0, padx=4, pady=4, ipadx=5, ipady=4)
B5 = Button( window, bg='grey',bd = 1 ,textvariable=B5var, width=15, height= 8, command=lambda: changestate(B5var,B5))      
B5.grid(row=1, column=1, padx=4, pady=4, ipadx=5, ipady=4)
B6 = Button( window, bg='grey',bd = 1 ,textvariable=B6var, width=15, height= 8, command=lambda: changestate(B6var,B6))      
B6.grid(row=1, column=2, padx=4, pady=4, ipadx=5, ipady=4)
B7 = Button( window, bg='grey',bd = 1 ,textvariable=B7var, width=15, height= 8, command=lambda: changestate(B7var,B7))      
B7.grid(row=2, column=0, padx=4, pady=4, ipadx=5, ipady=4)
B8 = Button( window, bg='grey',bd = 1 ,textvariable=B8var, width=15, height= 8, command=lambda: changestate(B8var,B8))      
B8.grid(row=2, column=1, padx=4, pady=4, ipadx=5, ipady=4)
B9 = Button( window, bg='grey',bd = 1 ,textvariable=B9var, width=15, height= 8, command=lambda: changestate(B9var,B9))      
B9.grid(row=2, column=2, padx=4, pady=4, ipadx=5, ipady=4)

window.mainloop()