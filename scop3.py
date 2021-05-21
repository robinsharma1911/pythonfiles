#global keyword ...using global keyword variable belongs to the global scope
x=300
def myfunc():
    global x
    x=200
print(x)
myfunc()
print(x)

#if  create a new global variable in function...
def myfunc():
    global x
    x=500
print(x)
myfunc()
print(x)