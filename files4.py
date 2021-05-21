#to create/write files
#append content to the file
f=open("file2.py","w")
f.write("print('a and b')")
f.close()

#open and read file after appending
f=open("file2.py","r")
print(f.read())