#to create/write files
#append content to the file
f=open("file2.txt","a")
f.write("print('a and b')")
f.close()

#open and read file after appending
f=open("file2.txt","r")
print(f.read())