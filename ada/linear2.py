arr = [2,5,4,3,5,6]
x = 5
flag = 0
for i in range(len(arr)):
    if arr[i] == x:
        print('find element at location', i)
        flag = 1
        
if flag == 0:
    print("element is not found in array")