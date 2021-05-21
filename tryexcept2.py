#use else keyword ... try block dosn't generate any error
try:
    print("hello")
except:
    print("something went wrong")
else:
    print("nothng went wrong")

#use finally keyword... executed regardless if try block raise error or not 
try:
    print(x)
except:
    print("something went wrong")
finally:
    print("try except is finished")