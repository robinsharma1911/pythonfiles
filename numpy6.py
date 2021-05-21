#indexing of arrays..
#for 1-D Array..
import numpy as np
arr=np.array([2,3,4,6,5])
print(arr[2])

#for 2-D Array...
print("indexing of 2-D Array")
arr2=np.array([[2,3,4],[5,6,7]])
print(arr2[0,1])

#you can also get 2 elements and add them form an array...*
print(arr2[0,1]+arr2[1,0])