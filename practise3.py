#........................... minimal_tkinter.py.................................
from tkinter import Tk,Label,messagebox,Button,Entry
root = Tk()
#.........................title of my window...
root.title("mywindow")
# ..............Make window 300x150 and place at position (50,50).....
root.geometry("300x300+50+50")
# ...............Create a label as a child of root window...........
my_text = Label(root, text='Hello, world!')
text2=Label(root,text="welcome to my city")
#.....................create a button to for exit........................
mybutton=Button(root,text='exit',command=root.destroy)
my_text.pack()
text2.pack()
mybutton.pack()
#...................create a function for pop up window.........
def myfunc():
    #...................ask permission for yes no ..........
    dialog_title = 'Please answer'
    dialog_text = 'Do you like bacon?'
    answer = messagebox.askquestion(dialog_title, dialog_text)

    if answer == 'yes':
        print('I like bacon too!')
    else: 
        print('You must have clicked the wrong button by accident.')

#........................button for pop up window.........................
popup=Button(root,text='pop up',command=myfunc)
popup.pack()
#.......................enter or input from output window............................
mytext=Entry(root)
mytext.pack()
def entryfunc():
    print(mytext.get())
buttondisp=Button(root,text='print text',command=entryfunc)
buttondisp.pack()

root.mainloop()