#use same function to make both function in same program...
def myfunc(n):
    return lambda a: a*n
mydoubler=myfunc(2)
mytripler=myfunc(3)
print(mydoubler(11))
print(mytripler(11))