#Binary Search program using recursive method...
def binarysearch(arr, low, high, x):
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binarysearch(arr, low, mid-1, x)
		else:
			return binarysearch(arr, mid+1, high, x)
	else:	
		return -1

arr = [4 ,6, 8, 13, 26, 27, 32]

print("array elements is:\n", arr)
x = int(input("enter element to be search:"))
result = binarysearch(arr, 0, len(arr)-1, x)
if result != -1:
	print("element is present in array at index", result)
else:
	print("element is not present in this array")
