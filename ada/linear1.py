arr = [2,5,4,3,6]
x = 4
flag = 0
for i in range(len(arr)):
    if arr[i] == x:
        print('find element at location ', i)
        flag = 1
        break

if flag == 0:
    print("element not found in array")