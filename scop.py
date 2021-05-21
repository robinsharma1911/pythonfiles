# #local scope define inside a region...
# def myfunc():
#     x=300
#     print(x)
# myfunc()

#if function inside the function...
def myfunc():
    x=200
    def myfunc():
        print(x)
    myfunc()
myfunc()