#many exceptions...
#print one message if try block raise a NameError and another for others
try:
    print(x)
except NameError:
    print("x is not defined")
except:
    print("something else went wrong")
    