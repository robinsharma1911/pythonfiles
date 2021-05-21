#use lambda...and try except satements 
x=input("enter the value of a ")
y=input("enter the value of b ")
try:
    a=lambda x,y:x+y
    print(a(int(x),int(y)))
except:
    print("wrong choice use integers only")