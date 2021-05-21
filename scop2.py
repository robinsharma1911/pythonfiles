#naming variable...function print local x ,then code print global x
x=300
def myfunc():
    x=200
    print(x)
    
print(x)
myfunc()
print(x)