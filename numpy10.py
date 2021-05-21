#Slicing 2-D Array...
import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(arr[1,0:3])
#3rd coloum of both rows
print(arr[0:2,3])

#for both rows and coloums..
print(arr[0:2,1:3])