#to read whole file use loop through lines
f=open("file1.py","r")
for x in f:
    print(x)

#to close the file
f=open("file1.py","r")
print(f.readline())
f.close()