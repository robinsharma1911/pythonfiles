#ternary search....
def ternarysearch(arr, low, high, x):
	if high >= low:
		m1 = low+(high-low)//3
		m2 = high-(high-low)//3	
    	
        
		if arr[m1] == x:
			return m1
		elif arr[m2] == x:
			return m2
		elif x < arr[m1]:
			return ternarysearch(arr,low,m1-1,x)
        	
		elif x > arr[m2]:
			return ternarysearch(arr, m2+1, high, x)   
		else:	
			return ternarysearch(arr, m1 + 1, m2 - 1, x)  	    
	return -1    

arr = [4 ,6, 8, 13, 26, 27, 32]
x = int(input("enter element to be search:"))
result = ternarysearch(arr, 0, len(arr)-1, x)
if result != -1:
	print("element is present in array at index", result)
else:
	print("element is not present in this array")