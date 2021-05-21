#import module or use of try except statements...and use module.py
import module as a
x=input("enter the value of a ")
y=input("enter the value of b ")
try:
    a.myfunc(int(x),int(y))
except:
    print("wrong choice use integers only")