#arbitary keyword argument,**kwargs
def myfunc(**kid):
    print("his last name is"+kid["lname"])
myfunc(fname="robin",lname="sharma")