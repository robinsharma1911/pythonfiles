#higher dimansional arrays... using ndmin array
import numpy as np 
arr=np.array([1,2,3,4,5],ndmin=5)
print(arr)
print('number of dimensions',arr.ndim)